from django.contrib import admin # type: ignore
from .models import Client, Order, Package, Warehouse, Employee, PackageScan

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Package)
admin.site.register(Warehouse)
admin.site.register(Employee)
admin.site.register(PackageScan)
