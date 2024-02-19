const login = document.querySelector("[name='login']");
const register = document.querySelector("[name='register']");

login.addEventListener('click', () => {
    window.location.href = '/login';
});

register.addEventListener('click', () => {
    window.location.href = '/register';
});