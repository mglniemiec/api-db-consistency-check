import requests
import sqlite3
import os
import pytest

DB_PATH = "db/test_data.sqlite"
API_URL = "http://127.0.0.1:5000/users"

@pytest.fixture(autouse=True)
def reset_db():
    # Clean up the users table before each test
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()

def test_user_creation():
    payload = {"name": "Anna Tester", "email": "anna@example.com"}
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 201

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users WHERE email = ?", (payload["email"],))
    result = cursor.fetchone()
    conn.close()

    assert result == (payload["name"], payload["email"])

def test_missing_name():
    payload = {"email": "no_name@example.com"}
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 400
    assert "Missing name or email" in response.text

def test_missing_email():
    payload = {"name": "Nameless User"}
    response = requests.post(API_URL, json=payload)
    assert response.status_code == 400
    assert "Missing name or email" in response.text

def test_duplicate_email():
    payload = {"name": "First Entry", "email": "dupe@example.com"}
    response1 = requests.post(API_URL, json=payload)
    response2 = requests.post(API_URL, json=payload)

    assert response1.status_code == 201
    assert response2.status_code == 409
    assert "Email already exists" in response2.text

