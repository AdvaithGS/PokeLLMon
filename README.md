# URL Shortener

A simple and efficient **URL Shortener** built using **Django**. This project allows users to shorten long URLs, track visit counts, and create custom aliases for their links.

## Features
- **Shorten URLs** automatically using a **hash-based system**.
- **Custom Aliases**: Users can define their own short URLs.
- **Error Handling** for invalid URLs and duplicate aliases.
- **Visit Tracking**: Each shortened URL maintains a count of visits, that can be looked at through a dedicated webpage
- **Redirect System**: Users are automatically redirected to the original long URL when accessing a short link.
- **User-Friendly Interface** with form-based input and real-time alerts.

---

## Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (default, can be switched to PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript
- **Hashing**: `hashlib` (SHA-256) for generating unique slugs

---

## Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/AdvaithGS/URL_Shortener.git
cd URL_Shortener
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Make Checks,and run the Server
```sh
python manage.py check
python manage.py runserver
```
Access the app at: **http://127.0.0.1:8000/**

---

## 🎯 URL Shortening Process

### 1️⃣ Shortening a URL
- Enter a valid URL in the input field.
- (Optional) Enable "Use custom alias?" and provide a custom short name.
- Click the **Shorten URL** button.
- If the alias is available, the system generates a shortened URL.
- If no alias is provided, a unique slug is generated using `hashlib`.

### 2️⃣ Redirecting to the Original URL
- Visit the shortened URL (`http://127.0.0.1:8000/u/<slug>/`).
- The system redirects to the original long URL and updates the visit count.

### 3️⃣ Viewing URL Statistics
- Visit **http://127.0.0.1:8000/stats/** to see:
  - The original long URL
  - The generated short URL
  - The total number of visits

---

## Error Handling
### **Invalid URLs**
- The system validates input to ensure only properly formatted URLs are accepted.
- Users are alerted if an invalid URL is entered.

### **Alias Conflicts**
- If a user selects a custom alias that is already taken, an **alert message** is displayed.
- The user can then select a different alias.

### **Non-Existent Short URLs**
- If a user attempts to access a non-existent short URL, they are shown a **404 error page**.

---

## Project Structure
```
URL_Shortener
│──url/
    │── urls.py          # URL routing
    │── views.py         # Core logic (shortening, redirecting, statistics)
    │── models.py        # Database models
    │── forms.py         # Django forms (URL input & alias toggle)
    │── templates/       # HTML templates
│──URL_Shortener/
    │── urls.py          # Universal URL routing
    │── settings.py      # Some very important settings, including django module config
│── manage.py        # script that manages the entire implementation 
│── db.sqlite3       # SQLite database
└── README.md        # Project documentation
```

---
