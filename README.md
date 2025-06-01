# CS6620_CodySnow

This repository serves as the foundation for semester‐long assignments.

---

## Current Assignment: CI/CD Pipeline (Part 1)

**Goal:**  
Create a repository with application code, corresponding tests, a dependency‐management file, and a GitHub Actions workflow that runs on commits/PRs to `main` (or manually on demand).

---

## Table of Contents

1. [Program Overview](#program-overview)  
2. [Repository Structure](#repository-structure)  
3. [Dependency Management](#dependency-management)  
4. [CI/CD Workflow](#cicd-workflow)  
5. [Cloning & Setup](#cloning--setup)  
6. [Running Tests](#running-tests)  

---

## Program Overview

### Check for Primes

- **Description:**  
  A simple utility to check whether a given integer is prime.
- **Key Class:**  
  - `PrimeChecker` (located in `primes/PrimeChecker.py`)  
    - Method: `is_prime(n)` → returns `True` if `n` is prime; otherwise `False`.

---

## Repository Structure

    CS6620_CodySnow/
    ├── primes/
    │   ├── PrimeChecker.py
    │   └── primes_test.py
    ├── requirements.txt
    └── .github/
        └── workflows/
            └── python-app.yml

- **primes/**  
  - `PrimeChecker.py` – Implements the prime‐checking logic.  
  - `primes_test.py` – pytest suite for `PrimeChecker`.  
- **requirements.txt** – Lists required Python packages (e.g., `pytest`).  
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

## Running Tests

Since `PrimeChecker` is not an executable, run the pytest suite:

1. Change into the `primes` directory:  
       cd primes  
2. Execute pytest:  
       pytest primes_test.py  

You should see output indicating which tests passed/failed.

---

## Additional Resources

- **GitHub “Cloning a repository” guide:**  
  https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository  
