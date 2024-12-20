# booking/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from booking.models import Schedule
import datetime

class AppointmentTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.appointment = Schedule.objects.create(
            user=self.user,
            date=datetime.date(2024, 11, 20),
            time='10:00:00',
        )

    def test_patients_page_view(self):
        response = self.client.get(reverse('patients_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/patients.html')
        self.assertContains(response, 'My Appointments')
        self.assertIn('appointments', response.context)

    def test_book_appointment_view(self):
        response = self.client.get(reverse('booking_appointment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_appointment.html')
        self.assertContains(response, 'Book Appointment')

    def test_edit_appointment_view(self):
        response = self.client.get(reverse('edit_appointment', args=[self.appointment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_appointment.html')
        self.assertContains(response, 'Edit Appointment')

    def test_delete_appointment(self):
        response = self.client.post(reverse('delete_appointment', args=[self.appointment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Schedule.objects.filter(id=self.appointment.id).exists())

    def test_logout_view(self):
        login_response = self.client.login(username='testuser', password='password')
        self.assertTrue(login_response)    
        logout_url = reverse('account_logout')  
        response = self.client.get(logout_url)    
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('account_login'))