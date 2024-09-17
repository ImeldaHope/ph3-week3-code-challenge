# ph3-week3-code-challenge

## Concerts Management System - SQLAlchemy

This project aims to manage and query concerts, bands, and venues using SQLAlchemy. The system will model relationships between bands, venues, and concerts, and provide methods for querying and aggregating data.

## Topics Covered

1. **SQLAlchemy Migrations** - Setup and manage database schema changes.
2. **SQLAlchemy Relationships** - Define and query relationships between models.
3. **Class and Instance Methods** - Create methods to handle custom behaviors and queries.
4. **SQLAlchemy Querying** - Perform complex database queries using SQLAlchemy.

---

## Setup

### Prerequisites

- Python 3.x
- SQLAlchemy
- Alembic (for migrations)

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:ImeldaHope/ph3-week3-code-challenge.git
   ```

2. Navigate into the project directory:
   ```bash
   cd ph3-week3-code-challenge
   ```

3. Install dependencies using Pipenv:
   ```bash
   pipenv install sqlalchemy alembic
   ```
   
4. Activate the Pipenv virtual environment:
   ```bash
   pipenv shell
   ```

5. Setup Alembic for migrations:
   ```bash
   alembic init migrations
   ```

6. Configure your `alembic.ini` and `env.py` for database connection and migrations.

---

## Database Migrations

### Migration for `Concerts` Table

A `Concert` belongs to a `Band` and a `Venue`, and the table should have the following columns:

- `id`: Primary key
- `band_id`: Foreign key to `Band` table
- `venue_id`: Foreign key to `Venue` table
- `date`: Stores the concert date as a string

Create the migration:
```bash
alembic revision --autogenerate -m "Create concerts table"
alembic upgrade head
```

---

## Conclusion

This project uses SQLAlchemy to model and query relationships between bands, concerts, and venues. The provided methods allow querying and performing aggregate functions efficiently, and SQLAlchemy's ORM features make it easy to interact with the database.

