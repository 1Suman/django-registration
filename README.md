# Django Authentication Project

This is a simple Django project for user authentication.
Users can:
- Sign Up
- Login
- Logout
- Go to Home Page

This project is made for learning purposes.


## 🛠 Technology Used

- Python
- Django 
- SQLite Database


## 📂 Project Structure

```
django-registration/
│
├── authentication/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── templates/
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
└── manage.py
```


## 🗄 Database

This project uses **SQLite** (default Django database).

All user data is stored inside:

```
db.sqlite3
```



## 🔗 URLs

| URL | What It Does |
|------|--------------|
| `/` | Signup Page |
| `/login/` | Login Page |
| `/home/` | Home Page |
| `/logout/` | Logout |
| `/admin/` | Admin Panel |





## 🚀 How To Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/1Suman/django-registration.git
cd django-registration
```

### 2. Create virtual environment
```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Run server
```bash
python manage.py runserver
```

Open browser:
```
http://127.0.0.1:8000/
---

## 👨‍💻 Author

Suman  
GitHub: https://github.com/1Suman

