from flask import Flask, jsonify, request

app = Flask(__name__)

# module‐level storage
added_name = ""

@app.route('/greet/<string:name>', methods=['GET'])
def greet(name):
    if name != added_name:
        return jsonify(error="Name not found. Please add it first using a POST request."), 404
    return jsonify(message=f"Hello, {name}!")

@app.route('/greet', methods=['POST'])
def add_name():
    global added_name
    name = request.json.get('name')
    if name and added_name == "":
        added_name = name
        return jsonify(message=f"Name '{name}' saved."), 201
    return jsonify(error="Invalid name or name is already saved. Use PUT to update, or DELETE to remove!"), 400

@app.route('/greet', methods=['PUT'])
def update_name():
    global added_name
    name = request.json.get('name')
    if name:
        added_name = name
        return jsonify(message=f"Name updated to '{name}'."), 200
    return jsonify(error="Invalid name."), 400

@app.route('/greet', methods=['DELETE'])
def delete_name():
    global added_name
    if added_name:
        deleted = added_name
        added_name = ""
        return jsonify(message=f"Name '{deleted}' deleted."), 200
    return jsonify(error="No name to delete."), 400

if __name__ == '__main__':
    app.run(debug=True)