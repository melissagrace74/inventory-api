# Inventory Management System (Flask + OpenFoodFacts)

## Setup
pip install -r requirements.txt

## Run API
python app.py

## Run CLI
python cli.py

## Run Tests
pytest

---

## Features
- Flask REST API (CRUD)
- External API integration (OpenFoodFacts)
- CLI interface
- Unit tests

---

## API Endpoints

GET /inventory  
GET /inventory/<id>  
POST /inventory  
PATCH /inventory/<id>  
DELETE /inventory/<id>  
GET /inventory/enrich/<barcode>