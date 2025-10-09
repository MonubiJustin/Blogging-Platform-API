# 📰 Blogging Platform API

A RESTful API built with **Django** and **Django REST Framework (DRF)** that powers a blogging platform.
It allows users to create, read, update, and delete blog posts, manage categories and tags, and perform filtering, search, and authentication.

---

## 🚀 Project Overview

This project is part of the **ALX Backend Engineering Capstone Project**.
The goal is to design and implement a fully functional **Blogging Platform API** that demonstrates backend development skills in Django.

---

## 🧩 Features

* **User Management (CRUD)**
  * User registration, login, profile update, and deletion
  * Authentication and permissions (only authors can modify their posts)
* **Blog Post Management (CRUD)**
  * Create, update, delete, and view posts
  * Associate posts with categories and optional tags
  * Pagination, search, and filtering
* **Filtering and Search**
  * Filter posts by author, category, tags, or date
  * Search posts by title or content
* **Optional Enhancements**
  * Comments, likes, and draft publishing
  * Markdown support for post content

---

## 🧱 Models Overview

| Model                    | Description                                |
| ------------------------ | ------------------------------------------ |
| **User**                 | Represents authors and readers             |
| **Post**                 | Stores blog post details and relationships |
| **Category**             | Defines categories (e.g., Tech, Lifestyle) |
| **Tag**                  | Defines tags (e.g., AI, Health, Startups)  |
| **Comment** *(optional)* | Stores user comments on posts              |

---

## 🛠️ Tech Stack

* **Language:** Python
* **Frameworks:** Django, Django REST Framework
* **Database:** MySQL
* **Authentication:** Django Auth / JWT
* **Testing:** Postman & Django Test Framework
* **Deployment:** PythonAnywhere / Render

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/blogging-platform-api.git
cd blogging-platform-api
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # on Mac/Linux
venv\Scripts\activate       # on Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Update your `settings.py` with MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_api_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

Visit the API at:
👉 `http://127.0.0.1:8000/api/`

---

## 📖 API Endpoints (Examples)

| Method   | Endpoint               | Description          |
| -------- | ---------------------- | -------------------- |
| `GET`    | `/api/posts/`          | List all posts       |
| `POST`   | `/api/posts/`          | Create new post      |
| `GET`    | `/api/posts/{id}/`     | Retrieve single post |
| `PUT`    | `/api/posts/{id}/`     | Update post          |
| `DELETE` | `/api/posts/{id}/`     | Delete post          |
| `GET`    | `/api/categories/`     | List categories      |
| `GET`    | `/api/tags/`           | List tags            |
| `POST`   | `/api/users/register/` | Register new user    |
| `POST`   | `/api/users/login/`    | Log in user          |

---

## 🧭 Folder Structure

```
blogging-platform-api/
│
├── blog/                  # Main app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── blog_api/              # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── requirements.txt
├── manage.py
└── README.md
```

---

## 🧠 Future Enhancements

* Add comments and likes system
* Implement JWT authentication
* Add markdown support for content
* Deploy frontend integration (React or Flutter)

---

## 👨‍💻 Author

**[Justin Monubi Ogenche]**
Backend Engineering Student @ ALX
📧 [monubijustin@gmail.com]
🔗 [[linkedIn](https://www.linkedin.com/in/monubi-justin-928014301/)]

---