# Inventory Management System (Flask REST API + OpenFoodFacts)

## Overview

This project is a Flask-based REST API Inventory Management System designed for managing retail inventory items. It supports full CRUD operations, integrates with the OpenFoodFacts API for real product data, and includes a CLI interface for interacting with the system.

The system uses an in-memory Python list as a mock database and demonstrates RESTful API design, external API integration, testing, and Git feature branching workflow.

---

## Features

- Flask REST API with full CRUD functionality
- In-memory inventory storage (Python list)
- External API integration (OpenFoodFacts)
- CLI-based user interface
- Unit testing with pytest
- Git feature branch workflow

---

## Project Structure

inventory-api/
│
├── app.py              # Flask REST API
├── models.py           # Mock database (inventory list)
├── services.py         # External API integration
├── cli.py              # Command-line interface
├── test_app.py        # Unit tests
├── requirements.txt    # Dependencies
├── README.md
└── .gitignore

---

## Setup Instructions

### 1. Clone Repository

git clone https://github.com/YOUR_USERNAME/inventory-api.git
cd inventory-api

### 2. Install Dependencies

pip install -r requirements.txt

---

## Running the Application

### Start Flask API

python app.py

Server runs at:
http://127.0.0.1:5555

---

### Run CLI Application

python cli.py

The CLI allows you to:
- View inventory
- Add items
- Update items
- Delete items
- Fetch product data from OpenFoodFacts API

---

## API Endpoints

GET /inventory

GET /inventory/<id>

POST /inventory

Example request:
{
  "product_name": "Organic Almond Milk",
  "brand": "Silk",
  "price": 3.99,
  "stock": 10,
  "barcode": "3017620422003"
}

PATCH /inventory/<id>

Example:
{
  "price": 5.99
}

DELETE /inventory/<id>

GET /inventory/enrich/<barcode>

Example:
GET /inventory/enrich/3017620422003

This endpoint retrieves real product data from OpenFoodFacts.

---

## OpenFoodFacts API

https://world.openfoodfacts.org/data

Used to retrieve real-world product data using barcodes.

---

## Running Tests

pytest

Expected output:
4 passed

Tests include:
- GET inventory
- POST inventory
- PATCH inventory
- DELETE inventory
- External API integration

---

## Git Workflow

This project was developed using feature branches:

- feature/flask-api
- feature/openfoodfacts-api
- feature-cli-interface
- feature-testing

All branches were merged into main after completion.

---

## Version Control

Optional version tag:
git tag v1.0
git push origin --tags

---

## Future Improvements

- Add persistent database (SQLite/PostgreSQL)
- Add authentication system
- Add frontend dashboard
- Improve CLI UX
- Add Docker support

---

## Author

Inventory Management System Project