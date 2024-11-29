from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('patients/', views.patients_page, name='patients_page'),
    path('booking/', views.book_appointment, name='booking_appointment'),
    path('edit/<int:id>/', views.edit_appointment, name='edit_appointment'),
    path('delete/<int:id>/', views.delete_appointment, name='delete_appointment'),    
]