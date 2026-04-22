# Planteer

Planteer is a Django web application for managing plants and collecting visitor contact messages.

## Features

- Home page with latest plants
- Plant CRUD (add, view, update, delete)
- Plant search by keyword
- Plant filtering by category, country, and edible status
- Plant detail page with related plants
- Comment system per plant
- Contact form and contact message listing
- Image upload support for plants

## Tech Stack

- Python 3
- Django 6.0.4
- SQLite (default database)
- Pillow (image handling)
- Bootstrap 5 (CDN)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/FadhelAlmalki/planteer.git
cd planteer
```

### 2. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows (Git Bash):

```bash
python -m venv venv
source venv/Scripts/activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Move to Django project directory

```bash
cd Planteer
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open in browser: http://127.0.0.1:8000/

### Optional: create admin user

```bash
python manage.py createsuperuser
```

Admin URL: http://127.0.0.1:8000/admin/

## Routes

### Core

- `/` - Home page
- `/admin/` - Django admin

### Main app

- `/contact/` - Contact form
- `/contact/messages/` - Contact messages list

### Plants app

- `/plants/all/` - List all plants
- `/plants/new/` - Add a new plant
- `/plants/search/` - Search plants
- `/plants/<plant_id>/detail/` - Plant details
- `/plants/<plant_id>/update/` - Update plant
- `/plants/<plant_id>/delete/` - Delete plant
- `/plants/comments/add/<plant_id>/` - Add comment to plant
- `/plants/country/<country_id>/` - Plants by country

## Data Models

### Plant

- `name` (CharField)
- `about` (TextField)
- `used_for` (TextField)
- `image` (ImageField, uploaded to `images/`)
- `category` (choices: `flower`, `tree`, `herb`)
- `is_edible` (BooleanField)
- `created_at` (DateTimeField)
- `countries` (ManyToManyField -> Country)

### Country

- `name` (CharField)
- `flag` (ImageField, uploaded to `flags/`)

### Comment

- `plant` (ForeignKey -> Plant)
- `author` (CharField)
- `text` (TextField)
- `created_at` (DateTimeField)

### Contact

- `first_name` (CharField)
- `last_name` (CharField)
- `email` (EmailField)
- `message` (TextField)
- `created_at` (DateTimeField)

## Static and Media

- Static URL: `static/`
- Media URL: `media/`
- Media files are served in development mode via project URL configuration.
- Uploaded plant images are stored under `Planteer/media/images/`.
- Uploaded flag images are stored under `Planteer/media/flags/`.