# Restaurant API

A small REST API for managing restaurant customers, menu items, and orders. It is built with Flask and Flask-SQLAlchemy and stores data in a local SQLite database.

## Requirements

- Python 3.10 or newer
- pip

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install Flask Flask-SQLAlchemy Flask-Migrate
```

On macOS or Linux, activate the environment with `source venv/bin/activate`.

Create the database tables:

```powershell
python create_db.py
```

Start the development server:

```powershell
python run.py
```

The API will be available at `http://127.0.0.1:5000`. The SQLite database is stored at `instance/restaurant.db`.

## API

All request and response bodies use JSON. Routes are prefixed with `/api`.

### Customers

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/customers` | List customers |
| POST | `/api/customers` | Create a customer |

Create customer body:

```json
{"name":"Ada Lovelace","phone":"555-0100","email":"ada@example.com"}
```

`name`, `phone`, and `email` are required; email addresses must be unique.

### Menu

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/menu` | List menu items |
| POST | `/api/menu` | Create a menu item |

Create menu item body:

```json
{"name":"Soup","price":12,"category_id":1}
```

The referenced category must already exist. Categories are represented in the database, but this API currently has no category management route.

### Orders

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/orders` | List orders |
| POST | `/api/orders` | Create an order |
| GET | `/api/orders/{id}` | Get one order |
| PUT | `/api/orders/{id}` | Update an order's quantity or status |
| DELETE | `/api/orders/{id}` | Delete an order |

Create order body:

```json
{"customer_id":1,"item_id":1,"quantity":2}
```

An order starts with status `pending`. The customer and menu item must exist. An update can include either or both of `quantity` and `status`:

```json
{"quantity":3,"status":"preparing"}
```

### Reports

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/reports/daily-sales` | Return today's sales total and date |
| GET | `/api/reports/top-items` | Return up to five menu items ordered by quantity sold |

Prices and sales totals use integer values in the units supplied by the API; no currency is specified in the code.

## Database migrations

The project is configured with Flask-Migrate/Alembic. To create and apply migrations after activating the virtual environment:

```powershell
flask --app run.py db migrate -m "describe schema change"
flask --app run.py db upgrade
```

For a fresh local database, `python create_db.py` creates the current model tables directly.
