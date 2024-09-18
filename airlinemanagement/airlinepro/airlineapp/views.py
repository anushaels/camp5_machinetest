from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Flight
from .forms import FlightForm
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's built-in authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user is a superuser
            if user.is_superuser:
                # Log the user in
                auth_login(request, user)
                # Redirect to the admin dashboard
                return redirect('admin_dashboard')
            else:
                # Show error if the user is not a superuser
                return render(request, 'account/login.html', {'error': 'You are not authorized to access this page'})
        else:
            # Show error if credentials are invalid
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')

def admin_dashboard(request):
    # Ensure the user is authenticated and is a superuser
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login')

    return render(request, 'registration/admin_dashboard.html')

@login_required
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FlightForm()
    return render(request, 'registration/add_flight.html', {'form': form})

@login_required
def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, flight_id=flight_id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'registration/edit_flight.html', {'form': form})
@login_required
def select_flight_to_edit(request):
    flights = Flight.objects.all()
    return render(request, 'registration/select_flight_to_edit.html', {'flights': flights})


@login_required
def view_all_flights(request):
    flights = Flight.objects.all()
    return render(request, 'registration/view_all_flights.html', {'flights': flights})

@login_required
def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, flight_id=flight_id)
    flight.delete()
    return redirect('admin_dashboard')

@login_required
def search_by_id(request):
    flight = None
    if 'flight_id' in request.GET:
        flight_id = request.GET['flight_id']
        flight = Flight.objects.filter(flight_id=flight_id).first()
    return render(request, 'registration/search_by_id.html', {'flight': flight})


def logout(request):
    # Clear the session data
    request.session.flush()
    return redirect('login')

