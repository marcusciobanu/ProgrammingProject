const login = document.querySelector("[name='login']");
const register = document.querySelector("[name='register']");
const home = document.querySelector("[name='home']")

login.addEventListener('click', () => {
    window.location.href = '/login';
});

register.addEventListener('click', () => {
    window.location.href = '/register';
});

home.addEventListener('click', () => {
    window.location.href = '/';
});