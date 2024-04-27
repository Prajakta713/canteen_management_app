from django.shortcuts import render
from mycanteen.models import Section
from mycanteen.models import MenuItem
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.shortcuts import redirect
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .models import Notification
from ..mycanteen import models

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            # Passwords don't match, handle this case as needed (e.g., show an error message)
            pass
        else:
            # Create user and save to database
            data = User.objects.create_user(username=username, password=password1)
            # Optionally, you can log in the user automatically after signup
            # login(request, user)
            data.save()
            return redirect('login')
           
    return render(request, 'signup.html')


def Login(request):
    return render(request,'login.html')

def track_order(request):
    # Your view logic for tracking orders
    return render(request, 'track_order.html')  


def menu_view(request):
    # Retrieve menu items from the database or any other source
    menu_items = MenuItem.objects.all()  # Example query to retrieve all menu items

    # Render the menu template with the menu items
    return render(request, 'mycanteen/menu.html', {'menu_items': menu_items})

def user(request):
    # Retrieve all sections and their associated items
    sections = Section.objects.prefetch_related('item_set').all()

    # Debug: Print sections and associated items to console to verify data
    for section in sections:
        print(section.name)
        for item in section.item_set.all():
            print(item.name)

    # Pass sections and items to the template
    return render(request, 'mycanteen/user.html', {'sections': sections})


def get_notifications(request):
    # Retrieve notifications data from the database
    notifications = Notification.objects.all().values_list('message', flat=True)
    # Convert QuerySet to list and return as JSON response
    return JsonResponse(list(notifications), safe=False)