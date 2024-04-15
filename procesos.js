const nombre = document.getElementById("nombre").value;
const correo = document.getElementById("correo").value;
const mensaje = document.getElementById("mensaje").value;

localStorage.setItem("nombre", nombre);
localStorage.setItem("correo", correo);
localStorage.setItem("mensaje", mensaje);

