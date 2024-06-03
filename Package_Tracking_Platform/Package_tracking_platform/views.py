from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Client, Employee, Package, PackageScan
# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if Client.objects.filter(email=email).exists():
                messages.info(request, 'email already exist!')
                return render(request, 'signup.html')
            else:
                client =  Client.objects.create(name=name, lastname=lastname, email=email, password=password)
                client.save()
                messages.info(request, 'Client created succesfully!')
                return render(request, 'login.html')

        else:
            messages.info(request, 'Password do not match!')
            return render(request, 'signup.html')
    else:

      return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        client = Client.objects.get(email=email)
        
        if client.password == password:
            return render(request, 'clientportal.html') 
        else:
            messages.info(request, 'Invalid email or password')
    
    else:
        return render(request, 'login.html')

def employee_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        employee = Employee.objects.get(email=email)

        clients = Client.objects.all()
        packages = Package.objects.all()
       
        if employee.password == password:
            return render(request, 'employeeportal.html', {'employee_id': employee.id,'clients': clients, 'packages': packages}) 
        else:
            messages.info(request, 'Invalid email or password')
    
    else:
        return render(request, 'employeelogin.html')
    

def package_registration(request):
    if request.method == 'POST':
        client_id = request.POST['client_name']
        weight = request.POST.get('weight')
        destination = request.POST.get('destination')
        price = request.POST.get('price')

        package = Package.objects.create(client_id=client_id, weight=weight, destination=destination,price=price)
        package.save()

        return render(request, 'employeeportal.html')
    else:
        clients = Client.objects.all()
        return render(request, 'employeeportal.html', {'clients': clients})
    
def confirm_package(request):
    clients = Client.objects.all()
    packages = Package.objects.all()
    
    if request.method == 'POST':
        employee_id = request.POST['employee']
        package_id = request.POST['package']
        existing_scan = PackageScan.objects.filter(employee_id=employee_id, package_id=package_id).exists()
        if existing_scan:
            messages.error(request, 'This package has already been scanned by You.')
            return render(request, 'employeeportal.html', {'employee_id': employee_id,'clients': clients, 'packages': packages})
        else:
            packagescan = PackageScan.objects.create(employee_id =employee_id, package_id=package_id)
            packagescan.save()
            return render(request, 'employeeportal.html')

    else:
        return render(request, 'employeeportal.html')
    
def dashboard(request):
    return render(request, 'dashboard.html')