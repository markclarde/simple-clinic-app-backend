# Simple Clinic App Backend

This is a practice Django project using PostgreSQL and pgAdmin.

## Features
- Django REST framework
- PostgreSQL
- pgAdmin
- Docker

### 1. Clone the repository
```
git clone https://github.com/markclarde/simple-clinic-app-backend.git
cd simple-clinic-app-backend
```

### 2. Set Up Environment Variables
- Create a `.env` file based on the example:
```
cp .env.example .env
```

### 3. Build and start Docker containers
```
docker compose up --build
```

### 4. Activate Python environment
```
python -m venv venv
venv\Scripts\activate
```

### 5. Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

### 7. Run Django migrations
```
python manage.py makemigrations
python manage.py migrate
```
- This will create all tables in your Postgres database.
- You can verify in pgAdmin at `http://localhost:5050/`.

### 8. Create superuser
```
python manage.py createsuperuser
```
- You can refer to the credentials in your `.env` file if you want to use predefined values.

### 8. Start Django server
```
python manage.py runserver
```
- Accessible at `http://127.0.0.1:8000/`.
