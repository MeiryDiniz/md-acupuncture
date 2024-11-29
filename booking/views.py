from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Schedule
from .forms import ScheduleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.http import HttpResponse

# Class view to have reviews displayed on the home page.
class HomePage(TemplateView):
    template_name = "booking/index.html"


@login_required
def patients_page(request):
    appointments = Schedule.objects.filter(user=request.user)
    return render(request, 'booking/patients.html', {'appointments': appointments})

    
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Appointment booked successfully.')
            return redirect('patients_page')
    else:
        form = ScheduleForm()
    
    return render(request, 'booking/booking_appointment.html', {'form': form})

@login_required
def edit_appointment(request, id):
    appointment = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('patients_page')
    else:
        form = ScheduleForm(instance=appointment)
    
    return render(request, 'booking/edit_appointment.html', {'form': form})

@login_required
def delete_appointment(request, id):
    appointment = Schedule.objects.get(id=id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
        return redirect('patients_page')
    return render(request, 'confirm_delete.html', {'appointment': appointment})

