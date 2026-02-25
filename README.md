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
