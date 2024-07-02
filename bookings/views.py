
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from .models import Train, Booking
from .forms import UserRegisterForm , UserLoginForm
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as django_logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

@login_required
def get_seat_availability(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        
        trains = Train.objects.filter(source=source, destination=destination)
        return render(request, 'seat_availability.html', {'trains': trains})
    
    return render(request, 'seat_availability.html')

@require_POST
@login_required
def book_seat(request):
    train_id = request.POST.get('train_id')
    train = get_object_or_404(Train, pk=train_id)
    
    if train.total_seats > train.booking_set.count():
        Booking.objects.create(user=request.user, train=train)
        return JsonResponse({'message': 'Booking successful!'})
    else:
        return JsonResponse({'message': 'No seats available!'}, status=400)

@permission_required('bookings.add_train')
def add_train(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        total_seats = int(request.POST.get('total_seats'))
        
        train = Train.objects.create(source=source, destination=destination, total_seats=total_seats)
        return JsonResponse({'message': 'Train added successfully!', 'train_id': train.id})
    else:
        return JsonResponse({'message': 'Only admin can add a train!'}, status=403)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form =UserLoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
    else:
        form=UserLoginForm()        
    return render(request, 'login.html')

@login_required
def user_logout(request):
    django_logout(request)
    return redirect('login')