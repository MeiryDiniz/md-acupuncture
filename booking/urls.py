from django.urls import path
from . import views

# app_name = 'booking'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('patients/', views.patients_page, name='patients_page'),
    path('patients/edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('patients/delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]