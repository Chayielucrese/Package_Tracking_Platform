# views.py
from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .models import Client, Order, Package, Employee, PackageScan

# Client Views
@login_required
def search_package(request):
    if hasattr(request.user, 'client'):
        if request.method == 'POST':
            tracking_id = request.POST.get('tracking_id')
            order = get_object_or_404(Order, tracking_id=tracking_id)
            packages = Package.objects.filter(order=order)
            return render(request, 'client/package_details.html', {'order': order, 'packages': packages})
        return render(request, 'client/search.html')
    else:
        return redirect('home')  # Or show an error message

@login_required
def package_details(request, package_id):
    if hasattr(request.user, 'client'):
        package = get_object_or_404(Package, id=package_id)
        scans = PackageScan.objects.filter(package=package)
        return render(request, 'client/package_history.html', {'package': package, 'scans': scans})
    else:
        return redirect('home')  # Or show an error message

# Employee Views
@login_required
def employee_dashboard(request):
    if hasattr(request.user, 'employee'):
        packages = Package.objects.all()
        return render(request, 'employee/dashboard.html', {'packages': packages})
    else:
        return redirect('home')  # Or show an error message

@login_required
def scan_package(request, package_id):
    if hasattr(request.user, 'employee'):
        package = get_object_or_404(Package, id=package_id)
        employee = request.user.employee
        warehouse = employee.warehouse
        PackageScan.objects.create(package=package, employee=employee, warehouse=warehouse)
        package.current_location = warehouse.location
        package.save()
        return redirect('employee_dashboard')
    else:
        return redirect('home')  # Or show an error message

def admin_dashboard(request):
    orders = Order.objects.all()
    packages = Package.objects.all()
    return render(request, 'admin/dashboard.html', {'orders': orders, 'packages': packages})

def employee_dashboard(request):
    packages = Package.objects.all()
    return render(request, 'employee/dashboard.html', {'packages': packages})

def scan_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    employee = request.user.employee
    warehouse = employee.warehouse
    PackageScan.objects.create(package=package, employee=employee, warehouse=warehouse)
    package.current_location = warehouse.location
    package.save()
    return redirect('employee_dashboard')

def search_package(request):
    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_id')
        order = get_object_or_404(Order, tracking_id=tracking_id)
        packages = Package.objects.filter(order=order)
        return render(request, 'client/package_details.html', {'order': order, 'packages': packages})
    return render(request, 'client/search.html')

def package_details(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    scans = PackageScan.objects.filter(package=package)
    return render(request, 'client/package_history.html', {'package': package, 'scans': scans})
