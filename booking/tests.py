from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from booking.models import Appointment  # Assuming you have an Appointment model

class AppointmentTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # Create a test appointment
        self.appointment = Appointment.objects.create(
            user=self.user,
            date='2024-11-20',
            time='10:00:00',
        )

    def test_patients_page_view(self):
        response = self.client.get(reverse('patients_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/patients.html')
        self.assertContains(response, 'My Appointments')
        self.assertIn('appointments', response.context)

    def test_book_appointment_view(self):
        response = self.client.get(reverse('book_appointment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/book_appointment.html')
        self.assertContains(response, 'Book Appointment')

    def test_edit_appointment_view(self):
        response = self.client.get(reverse('edit_appointment', args=[self.appointment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_appointment.html')
        self.assertContains(response, 'Edit Appointment')

    def test_delete_appointment(self):
        response = self.client.post(reverse('delete_appointment', args=[self.appointment.id]))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after deletion
        self.assertFalse(Appointment.objects.filter(id=self.appointment.id).exists())

    def test_logout_view(self):
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect after logout
