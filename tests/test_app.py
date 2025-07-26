import os, sys, requests, uuid
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
def test_create_get_successful():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell..."})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # get (from DynamoDB)
    r2 = requests.get(f"{BASE}/users/{user_id}")
    assert r2.status_code == 200
    assert r2.json()["userId"] == user_id

def test_create_get_s3_successful():
    # create
    r = requests.post(f"{BASE}/users", json={"info": "Rich Purnell..."})
    assert r.status_code == 201
    user_id = r.json()["userId"]

    # get (from S3)
    r2 = requests.get(f"{BASE}/users/{user_id}?cache=true")
    assert r2.status_code == 200
    assert r2.json()["userId"] == user_id
    assert r2.json()["source"] == "s3"

def test_get_nonexistent_user():
    r = requests.get(f"{BASE}/users/nonexistent")
    assert r.status_code == 404
    assert r.json() == {"error": "Not found in DynamoDB"}


# Sending a GET request with appropriate parameters returns expected JSON from the database
# Sending a GET request that finds no results returns the appropriate response
# Sending a GET request with no parameters returns the appropriate response
# Sending a GET request with incorrect parameters returns the appropriate response
# Sending a POST request results in the JSON body being stored as an item in the database, and an object in an S3 bucket
# Sending a duplicate POST request returns the appropriate response
# Sending a PUT request that targets an existing resource results in updates to the appropriate item in the database and object in the S3 bucket
# Sending a PUT request with no valid target returns the appropriate response
# Sending a DELETE request results in the appropriate item being removed from the database and object being removed from the S3 bucket
# Sending a DELETE request with no valid target returns the appropriate response