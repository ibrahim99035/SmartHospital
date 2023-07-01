let navBarShowBtn=document.querySelector(".navbar-show-btn");
let navbarCollaoseDiv=document.querySelector(".navbar-cllapse");
navBarShowBtn.addEventListener('click',function(){
    navbarCollaoseDiv.classList.add('navbar-show');
});
let HidenBar=document.querySelector(".navbar-hide-btn");
HidenBar.addEventListener('click',function(){
    navbarCollaoseDiv.classList.remove('navbar-show')
})
window.addEventListener('resize',searchIcon);
function searchIcon(){
    let windowSize=window.matchMedia("(min-width:1200px)");
    if (windowSize.matches){
        document.querySelector('.search-icon img').src="{% static '/Images/search-icon-dark.png' %}";
    }
    else{
        document.querySelector('.search-icon img').src="{% static '/Images/search-icon.png' %}";
    }
}
searchIcon();
let resizeTimer;
window.addEventListener('reset',() =>{
    document.body.classList.add('resize-animation-stopper');
    clearTimeout(resizeTimer);
    resizeTimer=setTimeout(()=>{
        document.body.classList.remove('resize-animation-stopper');
    },400)
})