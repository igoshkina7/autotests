Notes App Test Automation Framework

Automation framework for the Notes App built with Python, Pytest, Playwright, and Requests.

The project demonstrates a scalable automation architecture combining UI and API testing using the Page Object Model (POM) and reusable API clients.

Tech Stack
Python
Pytest
Playwright
Requests
Faker
Page Object Model
Factory Pattern
Project Structure
api/
config/
core/
data/
pages/
tests/
utils/

conftest.py
pytest.ini
requirements.txt
README.md
Features
UI automation with Playwright
API automation with Requests
Page Object Model
Reusable API clients
Test data factories
Structured logging
Environment configuration
Playwright tracing
Screenshot capture on failure
Test Coverage
API
User registration
Login
Create note
Edit note
Delete note
UI
Create note
Edit note
Delete note
Complete note
Search
Category filtering
Run tests

Install

pip install -r requirements.txt
playwright install

Run all tests

pytest

Run only API

pytest tests/api

Run only UI

pytest tests/integration
Architecture

The project follows several automation best practices:

Page Object Model
Component Objects
Factory Pattern
API Client Pattern
Pytest Fixtures
Test Isolation
Explicit waits
Reusable test data
Future Improvements
GitHub Actions
HTML reports
Parallel execution (pytest-xdist)
Docker support