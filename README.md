🛒 Grocery Shopping Web Application (Django)

A Grocery Shopping Web Application built using Django Framework that allows users to browse grocery items, place orders, make payments, and submit reviews. The project includes admin and user roles, authentication, OTP verification, and database management using SQLite.

📌 Project Overview

This project is designed to simplify grocery shopping by providing an online platform where users can:

Register and log in securely

Browse grocery categories and items

Add items to cart and place orders

Make payments

Give reviews and ratings

Receive OTP verification

Admins can manage users, groceries, categories, orders, and reviews.

🛠️ Technologies Used

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite

Tools: PyCharm / VS Code

Email Service: SMTP (for OTP)

📂 Project Structure
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
│   ├── myapp/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── tests.py
│
├── media/
├── .venv/
└── .idea/

🧩 Features
👤 User Features

User Registration & Login

OTP verification

Browse grocery items

Place grocery orders

Online payment option

Add reviews and ratings

🔐 Admin Features

Admin login

Manage grocery categories

Add / update grocery items

View orders and payments

Manage user reviews

🗄️ Database Models

Some key models used:

UserLogin – Stores login credentials

UserRegistration – Stores user profile details

AddCategory – Grocery categories

AddGrocery – Grocery products

GroceryItems – Item details

GroceryOrder – Order management

AddPayment – Payment records

AddReviews – User feedback

OtpCode – OTP verification

🚀 How to Run the Project
1️⃣ Extract the Project
unzip GroceryShopping_2025.zip

2️⃣ Navigate to Project Folder
cd GroceryShopping_2025/grocery

3️⃣ Activate Virtual Environment (optional)
.venv\Scripts\activate

4️⃣ Install Dependencies
pip install django

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Start the Server
python manage.py runserver

7️⃣ Open Browser
 http://127.0.0.1:8000/


🔑 Default Roles

Admin: Manages groceries and users

User: Shops and places orders

(Admin credentials can be added directly via database or Django admin panel)

📸 Screenshots

(Add screenshots here for better presentation)

🎯 Purpose of the Project

Academic mini / final project

Learning Django MVC architecture

Understanding authentication & database models

Implementing real-world e-commerce features
