from django.shortcuts import render
from django.views import generic
from .models import Review
# from django.http import HttpResponse

# Create your views here.

class HomePage(generic.ListView):
    queryset = Review.objects.filter(approved=True).order_by('-created_on')[:3]    
    template_name = "booking/index.html"
    


# def home(request):
#     # Retrieve the three most recent approved reviews
#     recent_reviews = Review.objects.filter(approved=True).order_by('-created_on')[:3]

#     context = {
#         'recent_reviews': recent_reviews
#     }

#     return render(request, 'base.html', context)

# def index(request):
#     return HttpResponse("Hello Patients!")