from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Schedule
from .forms import ScheduleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, time

# Class view to have reviews displayed on the home page.
class HomePage(TemplateView):
    template_name = "booking/index.html"


@login_required
def patients_page(request):
    now = timezone.now()  
    appointments = Schedule.objects.filter(user=request.user, date__gte=now.date()).order_by('date', 'time')
    return render(request, 'booking/patients.html', {'appointments': appointments})

    
# @login_required
# def book_appointment(request):
#     if request.method == 'POST':
#         form = ScheduleForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.user = request.user
#             try:
#                 appointment.save()
#                 messages.success(request, 'Appointment booked successfully!')
#                 return redirect('patients_page')
#             except ValidationError as e:                           
#                 messages.error(request, f"Error: {e.message}") 
#                 return redirect('booking_appointment')  
#         else:
#             for error in form.non_field_errors():  
#                 messages.error(request, error)
#     else:
#         form = ScheduleForm()
    
#     return render(request, 'booking/booking_appointment.html', {'form': form})
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            # Validate if the appointment is in the past
            date = form.cleaned_data.get('date')
            time_str = form.cleaned_data.get('time')
            if date and time_str:
                time_obj = datetime.strptime(time_str, "%H:%M").time()
                appointment_datetime = datetime.combine(date, time_obj)
                if appointment_datetime < datetime.now():
                    messages.error(request, "You cannot book an appointment in the past!")
                    return redirect('booking_appointment')
            try:
                appointment.save()
                messages.success(request, 'Appointment booked successfully!')
                return redirect('patients_page')
            except ValidationError as e:
                    messages.error(request, f"Error: {e.message}")
        else:
                for error in form.non_field_errors():
                    messages.error(request, error)
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
            messages.success(request, 'Appointment updated successfully!')
            return redirect('patients_page')
    else:
        form = ScheduleForm(instance=appointment)
    
    return render(request, 'booking/edit_appointment.html', {'form': form})

@login_required
def delete_appointment(request, id):
    appointment = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('patients_page')
    return render(request, 'booking/confirm_delete.html', {'appointment': appointment})

