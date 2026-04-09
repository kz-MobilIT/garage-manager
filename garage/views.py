from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Vehicle, Reservation


def home(request):
    return render(request, 'garage/home.html')


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'garage/customer_list.html', context)

from django.shortcuts import render, redirect
from .models import Customer

def customer_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        note = request.POST.get('note')

        Customer.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address,
            note=note,
        )

        return redirect('customer_list')
    
    return render(request, 'garage/customer_form.html')

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer': customer,
    }
    return render(request, 'garage/customer_detail.html', context)

def customer_update(request,pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('phone')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.note = request.POST.get('note') or ''
        customer.save()

        return redirect('customer_detail', pk=customer.pk)
    
    context = {
        'customer': customer,
    }
    return render(request, 'garage/customer_form.html', context)

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    
    context = {
        'customer': customer,
    }
    return render(request, 'garage/customer_confirm_delete.html', context)

def vehicle_list(request):
    vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles,
    }

    return render(request, 'garage/vehicle_list.html', context)

def vehicle_create(request):

    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        name = request.POST.get('name')
        plate_number = request.POST.get('plate_number')

        customer = get_object_or_404(Customer, pk=customer_id)

        Vehicle.objects.create(
            customer=customer,
            name=name,
            plate_number=plate_number,
        )

        return redirect('vehicle_list')
    
    customers = Customer.objects.all()
    context = {
        'customers': customers,   
    }
    return render(request, 'garage/vehicle_form.html', context)

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    context ={
        'vehicle' : vehicle,
    }
    return render(request, 'garage/vehicle_detail.html', context)

def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    customers = Customer.objects.all()

    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        name = request.POST.get('name')
        plate_number = request.POST.get('plate_number')

        if not customer_id or not name or not plate_number:
            context = {
                'vehicle': customers,
                'customers': customers,
                'error_message': '全て入力してください',
            }
            return render(request, 'garage/vehicle_form.html', context)
        
        customer = get_object_or_404(Customer, pk=customer_id)

        vehicle.customer = customer
        vehicle.name = name
        vehicle.plate_number = plate_number
        vehicle.save()

        return redirect('vehicle_detail', pk=vehicle.pk)
    
    context = {
        'vehicle': vehicle,
        'customers': customers,
    }
    return render(request, 'garage/vehicle_form.html', context)

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'garage/vehicle_confirm_delete.html', context)

def reservation_list(request):
    reservations = Reservation.objects.all()

    context = {
        'reservations': reservations,
    }
    return render(request, 'garage/reservation_list.html', context)


def reservation_create(request):
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()

    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        vehicle_id = request.POST.get('vehicle')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')

        if not customer_id or not vehicle_id or not date or not time:
            context = {
                'customers': customers,
                'vehicles': vehicles,
                'error_message': '顧客・車両・日付・時間は必須です。',
            }
            return render(request, 'garage/reservation_form.html', context)

        customer = get_object_or_404(Customer, pk=customer_id)
        vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

        Reservation.objects.create(
            customer=customer,
            vehicle=vehicle,
            date=date,
            time=time,
            description=description,
        )

        return redirect('reservation_list')

    context = {
        'customers': customers,
        'vehicles': vehicles,
    }
    return render(request, 'garage/reservation_form.html', context)

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    context = {
        'reservation': reservation,
    }
    return render(request, 'garage/reservation_detail.html', context)

def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()

    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        vehicle_id = request.POST.get('vehicle')
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description')

        if not customer_id or not vehicle_id or not date or not time:
            context = {
                'reservation': reservation,
                'customers': customers,
                'vehicles': vehicles,
                'error_message': '顧客・車両・日付・時間は必須です。',
            }
            return render(request, 'garage/reservation_form.html', context)

        customer = get_object_or_404(Customer, pk=customer_id)
        vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

        reservation.customer = customer
        reservation.vehicle = vehicle
        reservation.date = date
        reservation.time = time
        reservation.description = description
        reservation.save()

        return redirect('reservation_detail', pk=reservation.pk)

    context = {
        'reservation': reservation,
        'customers': customers,
        'vehicles': vehicles,
    }
    return render(request, 'garage/reservation_form.html', context)

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    
    context = {
        'reservation': reservation,
    }
    return render(request, 'garage/reservation_confirm_delete.html', context)