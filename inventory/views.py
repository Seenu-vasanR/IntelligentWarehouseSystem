
from django.http import HttpResponse
from .models import Product, Category, Supplier


def home(request):

    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()

    total_stock = sum(
        Product.objects.values_list('quantity', flat=True)
    )

    low_stock = sum(
        1 for product in Product.objects.all()
        if 0 < product.quantity <= product.minimum_stock
    )

    out_of_stock = Product.objects.filter(quantity=0).count()

    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Warehouse Management System</title>

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>

            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                padding: 30px;
                font-family: Arial, sans-serif;
                background: #60458A;
                color: white;
                text-align: center;
                min-height: 100vh;
            }}

            /* HEADER */

            .header {{
                background: #30204F;
                padding: 22px;
                border-radius: 12px;
                margin-bottom: 30px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            }}

            h1 {{
                font-size: 34px;
                color: white;
                margin: 10px 0;
            }}

            .subtitle {{
                color: #E5D8FF;
                font-size: 16px;
            }}

            /* ADMIN BUTTON */

            .admin-btn {{
                display: inline-block;
                background: #8B70B5;
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border: 1px solid #C4AFE5;
                border-radius: 8px;
                font-weight: bold;
                margin-top: 12px;
                transition: 0.3s;
            }}

            .admin-btn:hover {{
                background: #49316F;
                color: white;
            }}

            h2 {{
                font-size: 28px;
                color: white;
                margin: 35px 0;
            }}

            /* DASHBOARD CARDS */

            .dashboard {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 25px;
                max-width: 1100px;
                margin: auto;
            }}

            .card {{
                background: #49316F;
                padding: 35px 15px;
                border: 1px solid #A58BCB;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.20);
                transition: 0.3s;
            }}

            .card:hover {{
                transform: translateY(-5px);
                background: #30204F;
            }}

            .card h3 {{
                font-size: 19px;
                color: #E5D8FF;
                margin-bottom: 18px;
            }}

            .number {{
                font-size: 38px;
                font-weight: bold;
                color: white;
            }}

            .danger {{
                color: #FFB3C1;
            }}

            /* FOOTER */

            .footer {{
                margin-top: 40px;
                padding: 18px;
                background: #30204F;
                border-radius: 10px;
                color: #E5D8FF;
                font-size: 14px;
            }}

            /* RESPONSIVE */

            @media (max-width: 700px) {{

                body {{
                    padding: 15px;
                }}

                h1 {{
                    font-size: 25px;
                }}

                .dashboard {{
                    grid-template-columns: repeat(2, 1fr);
                    gap: 12px;
                }}

                .card {{
                    padding: 25px 10px;
                }}

                .card h3 {{
                    font-size: 15px;
                }}

                .number {{
                    font-size: 28px;
                }}
            }}

        </style>
    </head>

    <body>

        <div class="header">

            <h1>Intelligent Warehouse & Inventory Management System</h1>

            <div class="subtitle">
                Smart Stock Monitoring and Warehouse Management
            </div>

            <a href="/admin/" class="admin-btn">
                Admin Panel
            </a>

        </div>

        <h2>Warehouse Dashboard</h2>

        <div class="dashboard">

            <div class="card">
                <h3>Total Products</h3>
                <div class="number">{total_products}</div>
            </div>

            <div class="card">
                <h3>Total Categories</h3>
                <div class="number">{total_categories}</div>
            </div>

            <div class="card">
                <h3>Total Suppliers</h3>
                <div class="number">{total_suppliers}</div>
            </div>

            <div class="card">
                <h3>Total Stock Quantity</h3>
                <div class="number">{total_stock}</div>
            </div>

            <div class="card">
                <h3>Low Stock Products</h3>
                <div class="number danger">{low_stock}</div>
            </div>

            <div class="card">
                <h3>Out of Stock Products</h3>
                <div class="number danger">{out_of_stock}</div>
            </div>

        </div>

        <div class="footer">
            Intelligent Warehouse Management System
        </div>

    </body>
    </html>
    """)
