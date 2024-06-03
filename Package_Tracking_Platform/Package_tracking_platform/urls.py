from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.signup, name="signup"),
    # path('employeeportal/', views.employeeportal, name='employeeportal'),
    #path('clientportal/', views.clientportal, name='clientportal'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('confirmpackage/', views.confirm_package, name='confirmpackage'),
    path('employeelogin/', views.employee_login, name='employeelogin'),
    path('package_registration/', views.package_registration, name='package_registration'),
    
] 