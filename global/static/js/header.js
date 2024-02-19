const login = document.querySelector("[name='login']");
const staff = document.querySelector("[name='staff']");

login.addEventListener('click', () => {
    window.location.href = '/login';
});

staff.addEventListener('click', () => {
    window.location.href = '/admin';
});