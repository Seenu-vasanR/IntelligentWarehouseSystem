# Intelligent Warehouse & Inventory Management System

A web-based warehouse and inventory management application developed using Python, Django, and MySQL.

## 📌 Project Overview

The Intelligent Warehouse & Inventory Management System helps manage warehouse products, categories, suppliers, and stock movements. It provides a dashboard to monitor inventory levels and identify low-stock and out-of-stock products.

## 🚀 Features

- **Dashboard:** Displays total products, categories, suppliers, and stock quantity.
- **Product Management:** Add, update, search, and manage products.
- **Category Management:** Organize products by category.
- **Supplier Management:** Maintain supplier information.
- **Stock In:** Automatically increases product quantity.
- **Stock Out:** Automatically decreases product quantity.
- **Stock Validation:** Prevents stock-out quantities from exceeding available stock.
- **Stock Monitoring:** Identifies in-stock, low-stock, and out-of-stock products.
- **Search & Filters:** Search products and filter stock movement records.
- **Admin Panel:** Manage warehouse information through Django Admin.

## 🛠️ Technologies Used

- Python
- Django
- MySQL
- HTML
- CSS
- JavaScript (if used in the project)

## 📂 Project Modules

1. Dashboard
2. Product Management
3. Category Management
4. Supplier Management
5. Stock Movement Management
6. Inventory Monitoring
7. Admin Management

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Seenu-vasanR/IntelligentWarehouseSystem.git
```

### 2. Navigate to the project folder

```bash
cd IntelligentWarehouseSystem
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install Django PyMySQL python-dotenv
```

### 6. Configure environment variables

Create a `.env` file in the project root folder and configure your own Django secret key and MySQL database credentials.

### 7. Run database migrations

```bash
python manage.py migrate
```

### 8. Start the development server

```bash
python manage.py runserver
```

### 9. Open the application

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

## 🎯 Project Objective

To simplify warehouse operations, improve inventory tracking, monitor stock availability, and manage stock movements efficiently.

## 👨‍💻 Developer

**Seenuvasan R.**

GitHub: https://github.com/Seenu-vasanR

LinkedIn: https://linkedin.com/in/seenuvasanr

---

⭐ Thank you for visiting my project!
