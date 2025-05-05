# API–DB Consistency Check

A small QA project that checks whether data submitted to a mock API is correctly stored in a database — useful for validating end-to-end data flow in test environments.

---

## 📋 Table of Contents

- [Overview](#overview)
- [app.py (Mock API)](#apppy-mock-api)
- [setup.sql (Database Schema)](#setupsql-database-schema)
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

```bash
sqlite3 db/test_data.sqlite < sql/setup.sql

## How to Use

1. Install dependencies
pip install -r requirements.txt

2. Initialize the SQLite database
sqlite3 db/test_data.sqlite < sql/setup.sql

3. Start the Flask server
python3 app.py

4. Send a POST request to test it
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Max Mustermann", "email": "max@example.com"}'

5. Verify the data is in the database
sqlite3 db/test_data.sqlite
sqlite> SELECT * FROM users;

To exit SQLite:
.exit


## Requirements


Python 3.x
Flask
SQLite (included with Python)

