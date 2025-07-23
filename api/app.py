import os
import uuid
from botocore.exceptions import ClientError
from flask import Flask, request, jsonify
import boto3

# initialize app and env variables
app = Flask(__name__)
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT", "http://dynamodb-local:8000")
REGION = os.getenv("REGION", "eu-west-1")
TABLE_NAME = "Users"
BUCKET = "users-cache-bucket"

# dynamodb/s3 setup
dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=DYNAMODB_ENDPOINT,
    region_name=REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)
s3 = boto3.resource(
    "s3",
    endpoint_url=os.getenv("S3_ENDPOINT"),
    region_name=REGION,
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

# define routes 
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    # I created a query parameter called "cache" to let the client indicate whether
    # they want the s3 file data or the data from DynamoDB users table
    use_cache = request.args.get("cache", "false").lower() == "true"

    if use_cache:
        # attempt to find in s3
        obj = s3.Object(BUCKET, f"{user_id}.txt")
        try:
            body = obj.get()["Body"].read().decode("utf-8")
            data = body.strip()
            resp = {"userId": user_id, "info": data, "source": "s3"}
            return jsonify(resp), 200
        except ClientError as e:
            code = e.response.get("Error", {}).get("Code")
            if code in ("NoSuchKey", "404"):
                return jsonify({"error": "Not found in cache"}), 404
            else:
                return jsonify({"error": "S3 error", "details": code}), 500
            
    # otherwise get from DynamoDB 
    table = dynamodb.Table(TABLE_NAME)
    resp = table.get_item(Key={"userId": user_id})    
    if "Item" in resp:
        resp["Item"]["userId"] = user_id
        resp["Item"]["source"] = "dynamodb"
        return jsonify(resp["Item"]), 200
    return jsonify({"error": "Not found in DynamoDB"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    user_id = str(uuid.uuid4())
    item = {"userId": user_id, "info": data.get("info", "")}
    dynamodb.Table(TABLE_NAME).put_item(Item=item)

    # create s3 object wth user_id as filename
    key = user_id + ".txt"
    body = data.get("info", "")
    obj = s3.Object(BUCKET, key)
    obj.put(Body=body)

    return jsonify(item), 201

@app.route("/users/<user_id>", methods=["PUT"])
def put_user(user_id):
    data = request.get_json() or {}
    table = dynamodb.Table(TABLE_NAME)
    item = {"userId": user_id, "info": data.get("info", "")}
    table.put_item(Item=item)
    # find/update s3 object with user_id as filename
    key = user_id + ".txt"
    body = data.get("info", "")
    obj = s3.Object(BUCKET, key)
    obj.put(Body=body)
    return jsonify(item), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    # delete from dynamodb
    table = dynamodb.Table(TABLE_NAME)
    table.delete_item(Key={"userId": user_id})

    # delete from s3
    key = user_id + ".txt"
    obj = s3.Object(BUCKET, key)
    try:
        obj.delete()
    except ClientError as e:
        code = e.response.get("Error", {}).get("Code")
        if code == "NoSuchKey":
            return jsonify({"error": "Not found in cache"}), 404
        else:
            return jsonify({"error": "S3 error", "details": code}), 500

    return jsonify({"message": "User deleted"}), 200

# app main
if __name__ == "__main__":
    if not BUCKET or not TABLE_NAME:
        raise ValueError("BUCKET and TABLE_NAME must be set in environment variables")
    # create s3 bucket 
    try:
        s3.create_bucket(Bucket=BUCKET)
    except ClientError as e:
        if e.response["Error"]["Code"] != "BucketAlreadyOwnedByYou":
            print(f"Error creating bucket: {e}")        
    # create dynamoDB table
    try:
        dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{"AttributeName": "userId", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "userId", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1},
        )
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        print(f"Table {TABLE_NAME} already exists.")
    except ClientError as e:
        print(f"Error creating table: {e}")

    app.run(host="0.0.0.0", port=8080)
