
from django.contrib import admin
from django.urls import path, include

# Admin Panel Customization
admin.site.site_header = "Intelligent Warehouse & Inventory Management System"
admin.site.site_title = "Warehouse Management System"
admin.site.index_title = ""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
]
