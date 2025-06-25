# CS6620_CodySnow

This repository holds submissions for semester assignments.

---

## Current Assignment: CI/CD Pipeline (Part 2)

**Goal:**  
Create a REST API with endpoints for GET, POST, PUT, and DELETE verbs, and tests for each endpoint
---

## Table of Contents

1. [Program Overview](#program-overview)  
2. [Repository Structure](#repository-structure)  
3. [CI/CD Workflow](#cicd-workflow)  
4. [Cloning & Setup](#cloning--setup)  
5. [Running Tests](#running-tests)  

---

## Program Overview

### CRUD APIs

- **Description:**  
  A simple demo of RESTful APIs running in a docker container.
- **Key Class:**  
  - `app.py` (located in `REST_API/app.py`)  
    - Method: `is_prime(n)` → returns `True` if `n` is prime; otherwise `False`.
    - Method: `is_prime(n)` → returns `True` if `n` is prime; otherwise `False`.
    - Method: `is_prime(n)` → returns `True` if `n` is prime; otherwise `False`.
    - Method: `is_prime(n)` → returns `True` if `n` is prime; otherwise `False`.
TODO^^^ add GET POST PUT DELETE


---

## Repository Structure

    CS6620_CodySnow/
    ├── archive/
        ├── primes/
        │   ├── PrimeChecker.py
        │   └── primes_test.py
    ├── REST_API/
        └── app.py
        └── Dockerfile
        └── requirements.txt
    └── .github/
        └── workflows/
            └── python-app.yml

- **REST_API/**  
  - `app.py` – Implements the RESTful APIs
  - `Dockerfile` – container build script  
  - `requirements.txt` - app-specific requirements for the Docker image
- **requirements.txt** – Lists Python test package (`pytest`).  
- **.github/workflows/python-app.yml** – GitHub Actions workflow that installs dependencies and runs tests.

---

## CI/CD Workflow

- **Workflow file:** `.github/workflows/python-app.yml`  
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

1. TODO
2. 

---

## Running Tests 

1. TODO
2. 

You should see output indicating which tests passed/failed.

---

## Additional Resources

- **GitHub “Cloning a repository” guide:**  
  https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository  

### Repo Change Log
- 6/23: Archived "Check for Primes" toy program from Pipeline Assignment Part 1 and added new API container for Pipeline Assignment Part 2