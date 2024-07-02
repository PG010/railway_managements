"""
URL configuration for railway_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.urls import path
from .import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-seat-availability/', views.get_seat_availability, name='get_seat_availability'),
    path('book-seat/', views.book_seat, name='book_seat'),
    path('add-train/', views.add_train, name='add_train'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
]

    

