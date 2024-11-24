document.addEventListener('DOMContentLoaded', function() {
    const viewAppointmentsBtn = document.getElementById('view-appointments-btn');
    if (viewAppointmentsBtn) {
        viewAppointmentsBtn.onclick = function() {
            window.location.href = viewAppointmentsBtn.dataset.url;
        };
    }

    const bookAppointmentBtn = document.getElementById('book-appointment-btn');
    if (bookAppointmentBtn) {
        bookAppointmentBtn.onclick = function() {
            window.location.href = bookAppointmentBtn.dataset.url;
        };
    }

    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.onclick = function() {
            window.location.href = logoutBtn.dataset.url;
        };
    }

    const registerBtn = document.getElementById('register-btn');
    if (registerBtn) {
        registerBtn.onclick = function() {
            window.location.href = registerBtn.dataset.url;
        };
    }

    const loginBtn = document.getElementById('login-btn');
    if (loginBtn) {
        loginBtn.onclick = function() {
            window.location.href = loginBtn.dataset.url;
        };
    }

    const backAppointmentsBtn = document.getElementById('back-appointments-btn');
    if (backAppointmentsBtn) {
        backAppointmentsBtn.onclick = function() {
            window.location.href = backAppointmentsBtn.dataset.url;
        };
    }

    document.querySelectorAll('.edit-appointment-btn').forEach(function(button) {
        button.onclick = function() {
            window.location.href = button.dataset.url;
        };
    });
});
