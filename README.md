# 🛒 Django + React eCommerce App

This is a full-stack eCommerce application built with **Django (backend)** and **React (frontend)**. It includes user authentication, product management, a shopping cart system using **frontend-generated UUIDs**, and a REST API.

## 📌 Features

- **User Authentication** (Register, Login, Logout)
- **Product Management** (CRUD operations)
- **Category Management**
- **Shopping Cart** (UUID-based, persistent across sessions)
- **Order Processing**
- **RESTful API** (Django REST Framework)
- **Frontend** (React + Bootstrap)

---

## 🚀 Getting Started

### 1️⃣ **Clone the Repository**
```sh
git clone git@github.com:EmmanuelOnyekachi21/MyShopAPI.git
cd MyShopApi
```

### 2️⃣ **Set Up Virtual Environment**
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```python
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**
```sh
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=*
```

### 5️⃣ **Run Database Migrations**
```python
python manage.py migrate
```

### 6️⃣ **Create Superuser (for Admin Panel)**
```python
python manage.py createsuperuser
```

### 7️⃣ **Run the Backend Server**
```python
python manage.py runserver
```