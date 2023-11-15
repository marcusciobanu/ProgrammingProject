// Defining constants to make writing easier and more concise

const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.loginLink');
const registerLink = document.querySelector('.registerLink');
const loginBtn = document.querySelector('.loginBtn');
const closeButton = document.querySelector('.closeButton');

// Detects when user clicks register button and adds class to .wrapper 

registerLink.addEventListener('click', ()=> {
  wrapper.classList.add('active');
});

// Detects when user clicks login button and removes class from .wrapper

loginLink.addEventListener('click', ()=> {
  wrapper.classList.remove('active');
});

// Detects when user clicks on menubar login button and adds popup class to .wrapper

loginBtn.addEventListener('click', ()=> {
  wrapper.classList.add('popup');
  wrapper.classList.remove('active')
});

// Detects when user clicks on cross icon and removes popup class from .wrapper

closeButton.addEventListener('click',()=> {
  wrapper.classList.remove('popup');
});
