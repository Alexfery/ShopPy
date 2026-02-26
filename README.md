# MossArt Shop (Django)

E-commerce simplu pentru „Tablouri din licheni”:
- core: home/about/contact
- catalog: categorii + produse (slugs, filtrare, sortare, paginare)
- cart: coș în session (add/remove/update, total)
- orders: checkout + order + order items + admin

## Cerințe
- Python 3.12+
- Django 5+

## Setup rapid

```bash
python -m venv .venv
# Windows:
# .venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

pip install -r requirements.txt
```

## Config ENV
Creează `.env` (poți porni din `.env.example`):

```bash
cp .env.example .env
```

Setează minim:
- SECRET_KEY
- DEBUG=1
- ALLOWED_HOSTS=127.0.0.1,localhost

Optional Postgres:
- DATABASE_URL=postgres://user:pass@localhost:5432/mossshop

## Migrare + admin
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Seed demo content
```bash
python manage.py seed
```

## Run
```bash
python manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Media (imagini)
În admin poți încărca imagini pe produse. În development sunt servite automat când DEBUG=1.

MossArt Shop

MossArt Shop is a minimalist e‑commerce project for selling handmade, eco‑friendly moss art.
It demonstrates how to build a clean, responsive online store with Django 5 and modern CSS.

Features

Home – a landing page highlighting best sellers with sleek design.

Catalog – browse moss art by category or search across names and descriptions; supports pagination and sorting by price or newest.

Categories & Products – relational models for categories and products with slug‑based URLs, stock management and currency support.

Cart – session‑based cart with add, update and remove; displays subtotals and total price.

Checkout & Orders – collect customer details, create orders and order items; deduct stock automatically.

Admin Interface – manage categories, products and orders using Django’s built‑in admin.

Responsive Design – built with Tailwind CSS and a custom design palette for a clean aesthetic.

Prerequisites

Python 3.12+ and Django 5+.

A virtual environment is recommended.

Installation

Clone the repository and enter the project directory.

Create a virtual environment:

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

Environment Configuration

Copy the sample environment file and edit it:

cp .env.example .env


Set at least:

SECRET_KEY – a random secret for Django.

DEBUG=1 during development.

ALLOWED_HOSTS=127.0.0.1,localhost.

Optionally, set DATABASE_URL for PostgreSQL.

Database Setup

Generate and apply migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Optionally seed the database with demo categories and products:

python manage.py seed:contentReference[oaicite:3]{index=3}

Running the Server

Start the development server:

python manage.py runserver


The site will be available at http://127.0.0.1:8000/ with an admin interface at http://127.0.0.1:8000/admin/ .

Project Structure
core/        – landing page, about, contact views
catalog/     – product and category models, list/detail views
cart/        – cart logic, session storage and views
orders/      – checkout form, order models and views
moss_shop/   – project configuration (settings, URLs, WSGI/ASGI)
templates/   – base layout, components and page templates
static/      – CSS and assets

Development Notes

Migrations are not committed; run makemigrations before migrate.

Images uploaded via the admin are served automatically when DEBUG=1.

Customize the colour palette in static/css/styles.css to suit your brand.

License

This project is licensed for educational purposes. Feel free to fork and adapt it for your own moss art or similar projects. Contributions and improvements are welcome via pull requests.
