<p align="center">
  <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Django.svg" alt="Django Logo" width="90" height="90" />
</p>

<h1 align="center">🛒 Grocery Shopping Web Application</h1>

<p align="center">
  A full-featured online grocery shopping platform built with the Django framework, featuring role-based access, OTP verification, order tracking, and an integrated admin workflow.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" />
  <img src="https://img.shields.io/badge/Platform-Web-brightgreen?style=for-the-badge" alt="Platform" />
</p>

---

## 📌 Project Overview

This application bridges grocery retailers and everyday customers by digitizing the purchase workflow. Customers can register securely, verify accounts via OTP, browse categorized products, complete checkout with simulated payments, and leave ratings. Administrators retain complete control over inventory, user listings, order fulfillments, and review moderation.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
* **Database:** SQLite
* **Authentication & Mail:** Django Auth, SMTP (OTP verification)
* **IDE / Environment:** PyCharm / Visual Studio Code

---

## 📂 Project Structure

```text
GroceryShopping_2025/
│
├── grocery/
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── grocery/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   └── myapp/
│       ├── models.py
│       ├── views.py
│       ├── admin.py
│       ├── apps.py
│       └── tests.py
│
├── media/
├── .venv/
└── .idea/

## 🧩 Key Features

### 👤 Customer Experience
* **Authentication & Security:** Secure signup and signin backed by SMTP OTP generation.
* **Catalog Exploration:** Filter items across dynamic grocery categories.
* **Cart & Order Placement:** Seamless checkout pipeline tracking order volume and pricing.
* **Payment Records:** Automated storage of transaction receipts.
* **Community Feedback:** Product ratings and review submissions.

### 🔐 Administrative Tools
* **Inventory Control:** Create, update, or remove grocery categories and inventory items.
* **Order Oversight:** Monitor real-time orders, delivery states, and payment records.
* **User & Feedback Moderation:** Supervise customer profiles and review postings.

---

## 🗄️ Database Architecture

| Model | Purpose |
| :--- | :--- |
| `UserLogin` | Core user identity and authentication credentials |
| `UserRegistration` | Extended personal metadata and profile information |
| `AddCategory` | Category labels and sorting structure |
| `AddGrocery` | Catalog items and grocery inventory |
| `GroceryItems` | Granular product attributes (weight, SKU, variants) |
| `GroceryOrder` | Order manifests, statuses, and customer mappings |
| `AddPayment` | Transaction ledgers and settlement logs |
| `AddReviews` | Customer ratings, reviews, and timestamps |
| `OtpCode` | Temporal tokens for account validation |

lidation
