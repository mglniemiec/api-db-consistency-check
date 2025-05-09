# API–DB Consistency Check

A small QA project that checks whether data submitted to a mock API is correctly stored in a database — useful for validating end-to-end data flow in test environments.

---

## 📋 Table of Contents

- [Overview](#overview)
- [app.py (Mock API)](#apppy-mock-api)
- [setup.sql (Database Schema)](#setupsql-database-schema)
- [test_api_db.py (Pytest File)] (#test-api-db)
- [How to Use](#how-to-use)
- [Requirements](#requirements)

---

## Overview

This project simulates a basic user API using Flask and stores incoming user data into a local SQLite database. It's meant to help testers validate whether user-submitted data is correctly persisted.

---

## app.py (Mock API)

A Flask application that exposes a single POST endpoint for submitting user data (name and email). It inserts the data into a local SQLite database and returns appropriate status codes.

### Features

- Accepts JSON data with `name` and `email`
- Stores user records in SQLite
- Returns appropriate HTTP status codes:
  - `201 Created` on success
  - `400 Bad Request` if required fields are missing
  - `409 Conflict` for duplicate emails

---

## setup.sql (Database Schema)

Defines a single `users` table with:
- `id` (auto-increment primary key)
- `name` (text)
- `email` (unique text)

Initialize the database with:

sqlite3 db/test_data.sqlite < sql/setup.sql

## test_api_db.py (Pytest File)

This file contains automated tests to verify the end-to-end functionality of the mock API and its connection to the SQLite database.

### Features

- Uses [Pytest](https://docs.pytest.org/) for simple and readable test structure
- Automatically starts with a clean database state before each test
- Sends POST requests to the `/users` endpoint using Flask's test client
- Verifies the response code and ensures the submitted data is actually written to the database

### Current Tests

- ✅ `test_create_user_success`: Checks that valid name/email submissions return `201 Created` and are inserted into the database
- ✅ `test_missing_fields_returns_400`: Verifies the API returns `400 Bad Request` when required fields are missing
- ✅ `test_duplicate_email_returns_409`: Ensures a `409 Conflict` is returned when attempting to insert a duplicate email

These tests help ensure that the data flow between the API and database is reliable, making it easier to catch regressions and validate test environments automatically.

## How to Use

1. Install dependencies
pip install -r requirements.txt

2. Initialize SQLite database 
sqlite3 db/test_data.sqlite < sql/setup.sql

3. Start the Flask App
python3 app.py

4. In another terminal window run:
pytest

To stop Flask press CTRL + C

## Requirements

Python 3.x
Flask
requests
pytest
