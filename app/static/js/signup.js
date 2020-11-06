// Show/hide password onClick of button using Javascript only

// https://stackoverflow.com/questions/31224651/show-hide-password-onclick-of-button-using-javascript-only

function show() {
    var p = document.getElementById('pwd1');
    p.setAttribute('type', 'text');
    var p = document.getElementById('pwd2');
    p.setAttribute('type', 'text');
}

function hide() {
    var p = document.getElementById('pwd1');
    p.setAttribute('type', 'password');
    var p = document.getElementById('pwd2');
    p.setAttribute('type', 'password');
}

var pwShown = 0;

document.getElementById("eye1").addEventListener("click", function () {
    if (pwShown === 0) {
        pwShown = 1;
        show();
    } else {
        pwShown = 0;
        hide();
    }
}, false);
document.getElementById("eye2").addEventListener("click", function () {
    if (pwShown === 0) {
        pwShown = 1;
        show();
    } else {
        pwShown = 0;
        hide();
    }
}, false);

