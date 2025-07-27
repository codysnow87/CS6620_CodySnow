import os, sys, requests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from api.app import app
import api.app as application_module

# This fixture runs before every test, clearing out global state
@pytest.fixture(autouse=True)
def reset_added_name():
    application_module.added_name = ""
    app.config['TESTING'] = True

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Base URL for accessing the API container
BASE = os.getenv("BASE_URL", "http://app-python:8080")

# tests

# Sending a POST request results in the JSON body being stored as an item in the database, and an object in an S3 bucket
# Sending a GET request with appropriate parameters returns expected JSON from the database
def test_create_get_successful():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell is a steely eyed missile man"})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # get (from DynamoDB)
    r2 = requests.get(f"{BASE}/users/{user_id}?cache=false")
    assert r2.status_code == 200
    assert r2.json()["userId"] == user_id

def test_create_get_s3_successful():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell"})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # get (from S3)
    r2 = requests.get(f"{BASE}/users/{user_id}?cache=true")
    assert r2.status_code == 200
    assert r2.json()["userId"] == user_id
    assert r2.json()["source"] == "s3"

# Sending a GET request that finds no results returns the appropriate response
def test_get_nonexistent_user():
    user_id = "notarealuserid"
    r = requests.get(f"{BASE}/users/{user_id}?cache=false")
    assert r.status_code == 404
    assert r.json() == {"error": "Not found in database"}

# Sending a GET request with no parameters returns the appropriate response
def test_get_no_parameters():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell..."})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # get defaults to fetch from DynamoDB when no cache parameter is provided
    r = requests.get(f"{BASE}/users/{user_id}")
    assert r.status_code == 200
    assert r.json()["userId"] == user_id
    assert r.json()["source"] == "dynamodb"

# Sending a GET request with incorrect parameters returns the appropriate response
def test_get_incorrect_parameters():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell"})
    assert r.status_code == 201
    user_id = r.json()["userId"]
    # cache parameter must be 'true' or 'false'
    r = requests.get(f"{BASE}/users/{user_id}?cache=biscuits")
    # cache parameter is invalid, so it defaults to false but still returns from DynamoDB
    user_id = r.json()["userId"]
    assert r.status_code == 200
    assert r.json()["source"] == "dynamodb"

# Sending a duplicate POST request returns the appropriate response
def test_create_duplicate_user():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell"})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # create again with same info
    r2 = requests.post(f"{BASE}/users", json={"info": "Rich Purnell"})
    assert r2.status_code == 201
    assert r2.json()["userId"] != user_id # new userId generated despite same info
    assert r2.json()["info"] == "Rich Purnell"

# Sending a PUT request that targets an existing resource results in updates to the appropriate item in the database and object in the S3 bucket
def test_put_user():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell is a steely eyed missile man"})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # put (update)
    r2 = requests.put(f"{BASE}/users/{user_id}", json={"info": "Rich Purnell has been sacked"})
    assert r2.status_code == 200
    assert r2.json()["userId"] == user_id
    assert r2.json()["info"] == "Rich Purnell has been sacked"

# Sending a PUT request with no valid target returns the appropriate response
def test_put_invalid_user():
    user_id = "notarealuserid"
    r = requests.put(f"{BASE}/users/{user_id}", json={"info": "Rich Purnell"})
    assert r.status_code == 200  # PUT does not fail if userId does not exist, it just creates a new one
    assert "userId" in r.json()
    assert r.json()["info"] == "Rich Purnell"
    
# Sending a DELETE request results in the appropriate item being removed from the database and object being removed from the S3 bucket
def test_delete_user():
    # create 
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell"})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # get from s3 (to verify it exists)
    r2 = requests.get(f"{BASE}/users/{user_id}?cache=true")
    assert r2.status_code == 200
    assert r2.json()["userId"] == user_id
    assert r2.json()["source"] == "s3"
    assert r2.json()["info"] == "Rich Purnell" 

    # get from dynamodb (to verify it exists)
    r3 = requests.get(f"{BASE}/users/{user_id}?cache=false")
    assert r3.status_code == 200
    assert r3.json()["userId"] == user_id
    assert r3.json()["source"] == "dynamodb"
    assert r3.json()["info"] == "Rich Purnell" 

    # delete
    rDel = requests.delete(f"{BASE}/users/{user_id}")
    assert rDel.status_code == 200
    assert rDel.json() == {"message": "User deleted"}

    # verify deletion
    rVerifyDB = requests.get(f"{BASE}/users/{user_id}?cache=false")
    assert rVerifyDB.status_code == 404
    assert rVerifyDB.json() == {"error": "Not found in database"}
    rVerifyS3 = requests.get(f"{BASE}/users/{user_id}?cache=true")
    assert rVerifyS3.status_code == 404
    assert rVerifyS3.json() == {"error": "Not found in cache"}

# Sending a DELETE request with no valid target returns the appropriate response
def test_delete_invalid_user():
    user_id = 123
    r = requests.delete(f"{BASE}/users/{user_id}")
    assert r.status_code == 404
    assert r.json() == {"error": "Not found in database"}