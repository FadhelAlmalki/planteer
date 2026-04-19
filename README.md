## Planteer

Planteer is a Django web application for managing plants and handling visitor contact messages.
It includes:

- A home page with the latest added plants
- Plant CRUD operations (create, read, update, delete)
- Plant search and filtering by category and edible status
- Contact form and contact message listing
- Image upload support for plants

## Tech Stack

- Python 3
- Django 6.0.4
- SQLite (default database)
- Pillow (image handling)

## Installation and Setup

### 1. Clone the repository

```bash
git clone <https://github.com/FadhelAlmalki/Planteer.git>
cd Planteer
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

### 4. Go to the Django project directory

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

Open in browser:

http://127.0.0.1:8000/

## Main Routes

### Core

- `/` -> Home page
- `/admin/` -> Django admin

### Main app

- `/contact/` -> Contact form
- `/contact/messages/` -> Contact messages list

### Plants app

- `/plants/all/` -> List all plants
- `/plants/new/` -> Add a new plant
- `/plants/search/` -> Search plants
- `/plants/<plant_id>/detail/` -> Plant details
- `/plants/<plant_id>/update/` -> Update plant
- `/plants/<plant_id>/delete/` -> Delete plant

## Data Models

### Plant

- `name` (CharField)
- `about` (TextField)
- `used_for` (TextField)
- `image` (ImageField, uploaded to `images/`)
- `category` (choices: `flower`, `tree`, `herb`)
- `is_edible` (BooleanField)
- `created_at` (DateTimeField)

### Contact

- `first_name` (CharField)
- `last_name` (CharField)
- `email` (EmailField)
- `message` (TextField)
- `created_at` (DateTimeField)

## Static and Media Files

- Static URL: `static/`
- Media URL: `media/`
- Media root is configured in settings and served in development.

Plant images are stored under:

- `Planteer/media/images/`

