// add admin modal
var modal = document.getElementById('login');
var modal1 = document.getElementById('signup');
var modal2 = document.getElementById('sm');

window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
    if (event.target === modal1) {
        modal1.style.display = "none";
    }
    if (event.target === modal2) {
        modal2.style.display = "none";
    }
}