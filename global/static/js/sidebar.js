const button = document.querySelector('#button')
const sidebar = document.querySelector('.sidebar')
const contentwrapper = document.querySelector('.content-wrapper')

button.onclick = () => {
    sidebar.classList.toggle('active')
    contentwrapper.classList.toggle('active')
}