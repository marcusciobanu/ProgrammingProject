// Defining constants to make writing easier and more concise

const loginBtn = document.querySelector(".loginBtn");

// When loginBtn is clicked, it takes the user to the login page
loginBtn.addEventListener('click', () => {
  window.location.href = '/login';
});
