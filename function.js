import { productos } from "./BaseDatos.js";

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

const contenedorProductos = document.querySelector("#productos");

function mostrarProductos() {
  productos.forEach((producto) => {
    const tarjeta = document.createElement("div");
    tarjeta.classList.add("producto");

    const imagen = document.createElement("img");
    imagen.src = producto.imagen;
    imagen.alt = producto.nombre;
    tarjeta.appendChild(imagen);

    const nombre = document.createElement("h3");
    nombre.innerText = producto.nombre;
    tarjeta.appendChild(nombre);

    const descripcion = document.createElement("p");
    descripcion.innerText = producto.descripcion;
    tarjeta.appendChild(descripcion);

    const precio = document.createElement("p");
    precio.innerText = `$${producto.precio}`;
    tarjeta.appendChild(precio);

    contenedorProductos.appendChild(tarjeta);
  });
}
mostrarProductos();
