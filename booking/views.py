from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
# from django.http import HttpResponse

# Class view to have reviews displayed on the home page.
class HomePage(generic.ListView):
    queryset = Review.objects.filter(approved=True).order_by('-created_on')[:3]    
    template_name = "booking/index.html"


# Function view to have reviews displayed on the dashboard page.
@login_required
def patients_page(request):    
    reviews = Review.objects.filter(author=request.user).order_by("-created_on")
    review_count = reviews.count()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review has being successfuly submitted and is awaiting approval!'
            )
            return redirect('patients_page')
    else:
        form = ReviewForm() 
    
    return render(
        request,
        "booking/patients.html",
        {
            "reviews": reviews,
            "review_count": review_count,
            "form": form,
        },
    )    


def edit_review(request, review_id):

    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        
        review_form = ReviewForm(data=request.POST, instance=review)          

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

        return HttpResponseRedirect(reverse('patients_page')) 

    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'your_template_path/edit_review.html', {'form': review_form})

    
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        if review.author == request.user:
            review.delete()
            messages.add_message(request, messages.SUCCESS, 'Review Deleted!')
        else:
            messages.add_message(request, messages.ERROR, 'Error deleting review. You can only delete your own comments!')

        return HttpResponseRedirect(reverse('patients_page')) 

    return redirect('patients_page')




