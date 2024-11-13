from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/details/<int:id>', views.details, name='details'),
    path('add/', views.add_booking, name='add_booking'),
    path('edit/<int:id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:id>/', views.delete_booking, name='delete_booking'),
]