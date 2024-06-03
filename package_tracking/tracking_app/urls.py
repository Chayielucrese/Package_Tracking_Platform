from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('client/search/', views.search_package, name='search_package'),
    path('client/package/<int:package_id>/', views.package_details, name='package_details'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee/scan/<int:package_id>/', views.scan_package, name='scan_package'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
