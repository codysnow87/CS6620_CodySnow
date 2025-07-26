import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from REST_API.app import app
import REST_API.app as application_module

# This fixture runs before every test, clearing out global state
@pytest.fixture(autouse=True)
def reset_added_name():
    application_module.added_name = ""
    app.config['TESTING'] = True

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_greet(client):
    response = client.get('/greet/John')
    assert response.status_code == 404
    assert response.json == {
        "error": "Name not found. Please add it first using a POST request."
    }

def test_add_name(client):
    response = client.post('/greet', json={"name": "John"})
    assert response.status_code == 201
    assert response.json == {"message": "Name 'John' saved."}

def test_add_name_twice(client):
    response = client.post('/greet', json={"name": "John"})
    assert response.status_code == 201
    response = client.post('/greet', json={"name": "John"})
    assert response.status_code == 400
    assert response.json == {
        "error": "Invalid name or name is already saved. Use PUT to update, or DELETE to remove!"
    }

def test_update_name(client):
    client.post('/greet', json={"name": "John"})
    response = client.put('/greet', json={"name": "Jane"})
    assert response.status_code == 200
    assert response.json == {"message": "Name updated to 'Jane'."}
    response = client.get('/greet/Jane')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Jane!"}
    response = client.get('/greet/John')
    assert response.status_code == 404
    assert response.json == {
        "error": "Name not found. Please add it first using a POST request."
    }

def test_delete_name(client):
    client.post('/greet', json={"name": "John"})
    response = client.delete('/greet')
    assert response.status_code == 200
    assert response.json == {"message": "Name 'John' deleted."}
    response = client.get('/greet/John')
    assert response.status_code == 404
    assert response.json == {
        "error": "Name not found. Please add it first using a POST request."
    }
    response = client.delete('/greet')
    assert response.status_code == 400
    assert response.json == {"error": "No name to delete."}