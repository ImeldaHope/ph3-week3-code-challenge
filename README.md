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

1. Install dependencies:
   ```bash
   pip install sqlalchemy alembic
   ```

2. Setup Alembic for migrations:
   ```bash
   alembic init migrations
   ```

3. Configure your `alembic.ini` and `env.py` for database connection and migrations.

---

## Database Migrations

### Migration for `Concerts` Table

Before proceeding with the deliverables, you need to create the `concerts` table. A `Concert` belongs to a `Band` and a `Venue`, and the table should have the following columns:

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