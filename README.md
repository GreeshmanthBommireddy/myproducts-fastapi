# Product Management System (FastAPI + React)

A full-stack product inventory management application with a **FastAPI** backend, **PostgreSQL** database (via SQLAlchemy), and a **React** frontend.

---

## Architecture & Tech Stack

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/) for REST API endpoints and automatic Swagger documentation
  - [SQLAlchemy](https://www.sqlalchemy.org/) ORM with `psycopg2` driver
  - [Pydantic](https://docs.pydantic.dev/) for request/response validation
  - [PostgreSQL](https://www.postgresql.org/) for persistent storage
  - CORS middleware enabled for `http://localhost:3000`
- **Frontend:**
  - [React](https://react.dev/) 18 (bootstrapped with Create React App)
  - [Axios](https://axios-http.com/) for HTTP requests
  - Features: Product listing, live filtering, column-based sorting, add/edit/delete operations, and status toast messages

---

## Project Structure

```text
fastapi-rec/
├── database.py           # Database connection & SQLAlchemy session configuration
├── database_models.py    # SQLAlchemy database schema (Product table)
├── models.py             # Pydantic schemas for data validation
├── main.py               # FastAPI application, route handlers, and DB initialization
└── frontend/             # React single-page application
    ├── public/
    ├── src/
    │   ├── App.js         # Core inventory management UI and state
    │   ├── App.css        # Dashboard styling
    │   ├── TaglineSection.js / TaglineSection.css
    │   └── index.js
    └── package.json
```

---

## Prerequisites

- **Python** 3.10+
- **Node.js** 18+ and **npm**
- **PostgreSQL** server running locally on port `5432`

---

## Getting Started

### 1. Database Setup

Ensure PostgreSQL is running and create the target database:

```sql
CREATE DATABASE fastapi_db;
```

> **Environment Configuration:**
> Copy the template file `.env.example` to `.env` and set your credentials:
> ```bash
> cp .env.example .env
> ```
> In `.env`:
> ```env
> DATABASE_URL=postgresql+psycopg2://<username>:<password>@localhost:5432/fastapi_db
> ```
> *(The `.env` file is excluded from git via `.gitignore` to protect sensitive credentials.)*

---

### 2. Backend Setup & Launch

1. Open a terminal in the project root:
   ```bash
   cd fastapi-rec
   ```

2. Activate your virtual environment:
   - **Windows (PowerShell):**
     ```powershell
     .\myenv\Scripts\Activate.ps1
     ```
   - **Linux / macOS:**
     ```bash
     source myenv/bin/activate
     ```
   *(Or create a new one using `python -m venv venv`)*

3. Install required backend packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI development server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

The backend server will run at `http://localhost:8000`.  
Interactive API docs will be accessible at:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

> **Seed Data:** On the initial run, if the `product` table is empty, default sample records (Tv, Mobiles, Remotes) are automatically seeded.

---

### 3. Frontend Setup & Launch

1. Open a second terminal window and navigate to the frontend folder:
   ```bash
   cd fastapi-rec/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The client dashboard will automatically launch at `http://localhost:3000`.

---

## API Endpoints Reference

| Method | Endpoint | Description | Request Body |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Health check / greeting | None |
| `GET` | `/products/` | Fetch all products | None |
| `GET` | `/products/{id}/` | Get a specific product by ID | None |
| `POST` | `/products/` | Add a new product | `{"id": int, "name": str, "price": int, "quantity": int}` |
| `PUT` | `/products/{id}/` | Update an existing product | `{"id": int, "name": str, "price": int, "quantity": int}` |
| `DELETE` | `/products/{id}/` | Delete a product by ID | None |

---

## Features

- **CRUD Operations:** Create, read, update, and delete products directly from the interface or API.
- **Client-Side Filtering & Sorting:** Instant search across ID, name, or description; sortable columns by ascending or descending order.
- **Auto-Dismiss Alerts:** Temporary success and error status banners for user feedback.
- **CORS Configured:** Seamless communication between the React dev server (`:3000`) and the FastAPI backend (`:8000`).
