function confirmDelete(appointmentId) {
    if (confirm('Are you sure you want to delete this appointment?')) {
        document.getElementById('deleteForm' + appointmentId).submit();
    }
}


