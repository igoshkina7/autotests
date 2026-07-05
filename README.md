# UI Test Automation Framework

A UI test automation framework built with **Python**, **Pytest**, and **Playwright** using the **Page Object Model (POM)** design pattern.

The project demonstrates a scalable test architecture with reusable page components, fixtures, test hooks, screenshots, tracing, and clean project organization.

---

## Tech Stack

* Python 3.11
* Pytest
* Playwright
* Requests
* Page Object Model (POM)

---

## Project Structure

```
autotests/

├── artifacts/
│   ├── screenshots/
│   ├── traces/
│   └── reports/
│
├── config/
├── core/
├── data/
├── logs/
├── pages/
│   ├── components/
│
├── tests/
│   └── ui/
│
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Features

* Page Object Model
* Reusable page components
* Pytest fixtures
* Test hooks
* Automatic screenshots on test failure
* Playwright trace generation
* Environment configuration
* Structured logging

---

## Test Coverage

Current UI scenarios include:

* Login
* Inventory page
* Shopping cart
* Add/remove products
* Navigation
* Cart validation

---

## Run Tests

Install dependencies

```bash
pip install -r requirements.txt
```

Run all UI tests

```bash
pytest
```

Run smoke tests

```bash
pytest -m smoke
```

---

## Artifacts

Failed tests automatically generate:

* Screenshot
* Playwright Trace

Artifacts are stored in:

```
artifacts/
```

---

## Project Goals

This project is being continuously improved to include:

* API testing
* UI + API integration
* CI/CD (GitHub Actions)
* HTML reports
* Parallel execution
* Production-like automation architecture
