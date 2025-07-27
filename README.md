# CS6620_CodySnow

This repository holds submissions for semester assignments.

---

## Current Assignment: CI/CD Pipeline (Part 2)

**Goal:**  
  - Create a APIs with endpoints for GET, POST, PUT, and DELETE verbs, S3 and DynamoDB instances in a localstack container, and tests for each endpoint
---

## Table of Contents

1. [Program Overview](#program-overview)  
2. [Repository Structure](#repository-structure)  
3. [CI/CD Workflow](#cicd-workflow)  
4. [Cloning & Setup](#cloning--setup)  
5. [Running the APIs in Docker](#running-the-docker-container)
5. [Running Tests](#running-tests)  

---

## Program Overview

### CRUD APIs

- **Description:**  
  A more complex demo of RESTful APIs running in a docker container that connect to an S3 instance and a DynamoDB instance in a localstack container. 

---

## Repository Structure

    CS6620_CodySnow/
    ├── archive/
        ├── primes (assignment 1)
        ├── REST_API (assignment 2)
        ├── tests (assignment 2)
    ├── api/
        └── app.py
        └── Dockerfile
        └── requirements.txt
    ├── tests/
        └── test_app.py
        └── Dockerfile
        └── requirements.txt
    ├── .github/
        └── workflows/
            └── python-app.yml
            └── flask-api.yml
    └── docker-compose.yml
    └── run_api.sh
    └── run_tests.sh

- **api/**  
  - `app.py` – Implements the APIs
  - `Dockerfile` – container build script  
  - `requirements.txt` - app-specific requirements for the Docker image
- **tests/**
  - `test_app.py` – Tests the APIs
  - `requirements.txt` – requirements for running APIs and running the tests
- **.github/workflows/flask-api.yml** – GitHub Actions workflow that installs dependencies and runs tests.
---

## CI/CD Workflow

- **Workflow file:** `.github/workflows/flask-api.yml`  
- **Triggers:**  
  - Pushes or pull‐requests targeting the `main` branch  
  - Manual trigger via GitHub Actions UI  
- **Behavior:**  
  1. Set up Python environment.  
  2. Install dependencies (`pip install -r requirements.txt`).  
  3. Run tests (`pytest primes_test.py`).  
  4. Report pass/fail status on the commit/PR.

### Manually Running the Workflow

1. Go to the GitHub repository on the web.  
2. Click **Actions** in the top menu.  
3. Select **Python Application** from the left‐hand pane.  
4. Click **Run workflow** (button at the top right).  
5. Choose the branch (`main`) and click **Run workflow** again.

---

## Cloning & Setup

1. **Clone the repository** (if you haven’t already):  
       git clone https://github.com/YourUsername/CS6620_CodySnow.git  
       cd CS6620_CodySnow  
2. **Create and activate a virtual environment** (recommended):  
       python -m venv .venv  
       source .venv/bin/activate   # Windows: .venv\Scripts\activate  
3. **Install dependencies**:  
       pip install -r requirements.txt  

---

## Running the Docker container

1. Ensure docker and python are installed on your system
2. From the root folder of the repository, run the script `run_api.sh` via the command `sh run_api.sh`
3. The docker container will build and launch

---

## Running Tests

1. Ensure docker and python are installed on your system
2. From the root folder of the repository, run the script `run_tests.sh` via the command `sh run_tests.sh`
3. The docker-compose file will build and launch the docker containers 
4. The test container will execute its tests against the app container and then exit
5. The docker-compose file will tear down the containers

You should see output displaying test outcomes in the terminal output.

---

## Additional Resources

- **GitHub “Cloning a repository” guide:**  
  https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository  

### Repo Change Log
- 6/23: Archived "Check for Primes" toy program from Pipeline Assignment Part 1 and added new API container for Pipeline Assignment Part 2
- 7/26: Archived REST_API contents from Pipeline Assignment Part 2

### AI Use Disclaimer
- Some AI tools were used in the completion of this assignment: 
  - Visual Studio Code CoPilot intellicode plugin, which provides code suggestions while typing (a.k.a. code completion)
  - ChatGPT/Claude/Google Search with AI. Prompts used: 
    - "For this dynamoDB docker example template, what do I replace "location-of-your-dynamodb-demo-app:latest" with? (I pasted in the docker template from dynamoDB's docker site)"
    - Let's modify the following GET to take in a boolean query parameter called 'cache' (provided it with my GET api code)"
    - various error messages to get ideas for debugging