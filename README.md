# BloodVault

> A blood bank donor management system built with Django — full CRUD operations for registering, viewing, updating, and removing donor records.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-3.1-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-7952B3?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-Unlicense-blue)

## Screenshot

![BloodVault UI](https://i.ibb.co/ngRmdjw/image-2021-09-27-02-54-34.png)

### Features

- **Add Donors** — Register new blood donors with name, email, and blood group
- **View Donors** — Browse all registered donors in a tabular format
- **Edit Donors** — Update any donor's information
- **Remove Donors** — Delete donor records from the database
- **Admin Panel** — Manage records through Django's built-in admin interface

## Tech Stack

| Layer     | Technology            |
|-----------|-----------------------|
| Backend   | Python 3.9+, Django 3.1 |
| Frontend  | HTML5, Bootstrap 5.1  |
| Database  | SQLite3               |
| Pattern   | MVT (Model-View-Template) |

## Project Structure

```
bloodvault/
├── manage.py                       # Django management utility
├── bloodvault/                     # Project configuration
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Root URL routing
│   ├── wsgi.py                     # WSGI entry point
│   └── asgi.py                     # ASGI entry point
└── donor/                          # Blood donor app
    ├── models.py                   # Member model (name, email, group)
    ├── views.py                    # CRUD view functions
    ├── forms.py                    # ModelForm with Bootstrap widgets
    ├── admin.py                    # Admin panel registration
    ├── migrations/                 # Database migrations
    └── templates/donor/            # HTML templates
        ├── base.html               # Base layout with Bootstrap CDN
        ├── insertandread.html      # Home — add & list donors
        └── update.html             # Edit donor form
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/isobeyan/BloodVault.git
   cd BloodVault
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   cd bloodvault
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Open the app** — navigate to `http://127.0.0.1:8000/` in your browser.

### Admin Access

To access the Django admin panel at `/admin/`:

```bash
python manage.py createsuperuser
```

## API Routes

| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| GET    | `/`               | Home — list donors & add form |
| POST   | `/`               | Create a new donor       |
| GET    | `/<id>`           | Edit form for a donor    |
| POST   | `/<id>`           | Update donor record      |
| POST   | `/delete/<id>`    | Delete a donor record    |
| GET    | `/admin/`         | Django admin panel       |

## Contributing

Contributions are welcome. Please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is released into the public domain under the [Unlicense](LICENSE).
