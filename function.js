let carrousel = document.getElementById("carrousel");
let check1 = document.getElementById("check-1");
let check2 = document.getElementById("check-2");
let check3 = document.getElementById("check-3");

check1.addEventListener('click', function(){
    carrousel.style.backgroundImage = "url(https://okdiario.com/img/vida-sana/2015/10/zapatillas.jpg)";
    carrousel.style.width = "100%";
    carrousel.style.height = "800px";
    carrousel.style.transition = "0.5s";
});

check2.addEventListener('click', function(){
    carrousel.style.backgroundImage = "url(https://www.streetprorunning.com/blog/wp-content/uploads/2017/12/mejores-zapatillas-calidad-precio-1263x560.jpg)";
    carrousel.style.width = "100%";
    carrousel.style.height = "800px";
    carrousel.style.transition = "0.5s";
});

check3.addEventListener('click', function(){
    carrousel.style.backgroundImage = "url(https://i.ytimg.com/vi/ZOaGr1nGieg/maxresdefault.jpg)";
    carrousel.style.width = "100%";
    carrousel.style.height = "800px";
    carrousel.style.transition = "0.5s";
});
