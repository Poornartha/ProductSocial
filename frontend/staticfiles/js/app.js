
/* Sticky Navbar */
var nav = document.getElementById("navbar");
var landing = document.getElementById("navbar-landing");
var sticky;
if(nav != null) sticky = nav.offsetTop;
else sticky = landing.offsetTop;


window.onscroll = () => {
    if (window.pageYOffset > sticky) {
        if(nav != null) nav.classList.add("sticky");
        else {
            landing.classList.add("sticky");
            landing.classList.add("custom-light");
            landing.classList.remove("custom-dark");
        }
    }
    else {
        if(nav != null) nav.classList.remove("sticky");
        else {
            landing.classList.remove("sticky");
            landing.classList.add("custom-dark");
            landing.classList.remove("custom-light");
        }
    }
};

/* Login Signup */
function gotoSignUp() {
    document.getElementById("sign-up").style.display = "inline";
    document.getElementById("login").style.display = "none";
}

function gotoLogin() {
    document.getElementById("sign-up").style.display = "none";
    document.getElementById("login").style.display = "inline";
}
