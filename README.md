# 🚆 ICF Wheel Specifications API

This project is a backend service built with **FastAPI**, **Python 3.13.5**, and **PostgreSQL**, enabling the submission and retrieval of ICF Wheel Specification forms. It offers full Swagger/OpenAPI docs, input validation, and async database support.

---

## ⚙️ Tech Stack

* **Language:** Python 3.13.5
* **Platform:** Windows 11 (PowerShell 7+)
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy (async)
* **Validation:** Pydantic v2
* **Environment Config:** pydantic-settings
* **Docs:** Swagger UI (`/docs`), ReDoc (`/redoc`)

---

## 📁 Project Structure

```
|-- .env
|-- .env.example
|-- .gitignore
|-- app
|  |-- __init__.py
|  |-- config.py
|  |-- database.py
|  |-- main.py
|  |-- methods
|  |  |-- __init__.py
|  |  |-- get_wheel_specification_form.py
|  |  |-- post_wheel_specification_form.py
|  |-- models
|  |  |-- __init__.py
|  |  |-- wheel_specification_form.py
|  |-- routes
|  |  |-- __init__.py
|  |  |-- get_wheel_specification_form.py
|  |  |-- post_wheel_specification_form.py
|  |-- schemas
|  |  |-- __init__.py
|  |  |-- get_wheel_specification_form.py
|  |  |-- post_wheel_specification_form.py
|  |-- utils
|  |  |-- __init__.py
|-- README.md
|-- requirements.txt
|-- run.py
```

---

## 🚀 Getting Started

### 1. 🔽 Clone Repository

```powershell
git clone <your-repo-url>
cd <repo-folder>
```

### 2. ⚗️ Set Up Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. 📦 Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. ⚒️ Configure Environment Variables

Rename `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Then **remove the inline comments** and fill with valid values. Example:

```env
DB_HOST=demodb-anubhabs-demo-1.c.aivencloud.com
DB_PORT=15477
DB_USER=avnadmin
DB_PASS=AVNS_Ve9sTiqPUltXb4D3vKE
DB_NAME=defaultdb
DB_CONNLMT=15
```

> ⚠️ These credentials are for **development only**. Do not use in production.

### 5. ▶️ Run the App

```powershell
python run.py
```

Then open:

* Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧬 Auto DB Initialization

The database table `wheel_specification_forms` is auto-created on startup using SQLAlchemy's metadata. No migrations required.

---

## ✅ API Reference

### 1. `POST /api/forms/wheel-specifications`

Submit a new ICF wheel specification form.

#### Request Body:

```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)"
	...
  }
}
```

#### Success Response `201 Created`

```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}
```

#### Error Responses:

* `400`: `{ "detail": "Missing required fields" }`
* `409`: `{ "detail": "Form with this number already exists" }`
* `500`: `{ "detail": "Database error during form creation" }`

---

### 2. `GET /api/forms/wheel-specifications`

Fetch submitted forms using filters.

#### Query Params:

* `formNumber` (optional)
* `submittedBy` (optional)
* `submittedDate` (optional, `YYYY-MM-DD`)

#### Success Response `200 OK`

```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)"
      }
    }
  ]
}
```

#### Error Responses:
- `400`: `{ "detail": "Missing required fields" }`
- `400`: `{ "detail": "Invalid date format. Use YYYY-MM-DD." }`
- `409`: `{ "detail": "Form with this number already exists" }`
- `500`: `{ "detail": "Database error during form creation" }`
- `500`: `{ "detail": "<unexpected error message>" }`

---

## 📊 Testing

* Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
* Postman: `KPA_form data.postman_collection.json` (In the repo)

---

## 📅 Deliverables

* ✅ Source Code
* ✅ Working APIs (tested with Postman & Swagger)
* ✅ README (this file)
* ✅ Screen Recording

---

## 👨‍💼 Author

**Anubhab Dey**
📧 [anubhabdey2017@gmail.com](mailto:anubhabdey2017@gmail.com)
📱 7003696514
🔗 [github.com/Anubhab-Dey](https://github.com/Anubhab-Dey)
