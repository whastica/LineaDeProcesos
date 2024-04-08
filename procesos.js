// Función para validar las opciones seleccionadas
function validarFormulario() {
    // Validar que se haya seleccionado al menos un tipo de usuario
    const tipoUsuario = document.getElementById("tipo_usuario").value;
    if (tipoUsuario === "") {
        alert("Debe seleccionar un tipo de usuario");
        return false;
    }

    // Validar que se haya seleccionado al menos una funcionalidad básica
    const funcionalidades = document.querySelectorAll('input[name="funcionalidades[]"]:checked');
    if (funcionalidades.length === 0) {
        alert("Debe seleccionar al menos una funcionalidad básica");
        return false;
    }

    // Validar que se haya seleccionado al menos una plataforma
    const plataformas = document.querySelectorAll('input[name="plataforma[]"]:checked');
    if (plataformas.length === 0) {
        alert("Debe seleccionar al menos una plataforma");
        return false;
    }

    return true;
}

// Agregar evento "submit" al formulario
const formulario = document.querySelector("form");
formulario.addEventListener("submit", (event) => {
    event.preventDefault();

    if (validarFormulario()) {
        // Enviar el formulario
        formulario.submit();
    }
});

const fondo = document.querySelector(".fondo");

window.addEventListener("scroll", () => {
    const scrollY = window.scrollY;

    fondo.style.opacity = scrollY / 200;
});

const formulario = document.querySelector("form");

formulario.addEventListener("submit", (event) => {
    event.preventDefault();

    // Obtener las respuestas del usuario
    const respuestas = {};

    for (const elemento of formulario.elements) {
        if (elemento.type === "radio" || elemento.type === "checkbox") {
            if (elemento.checked) {
                respuestas[elemento.name] = elemento.value;
            }
        } else if (elemento.type === "text") {
            respuestas[elemento.name] = elemento.value;
        }
    }

    // Guardar las respuestas en el almacenamiento local
    localStorage.setItem("respuestas", JSON.stringify(respuestas));

    // Redirigir al usuario a otra página
    window.location.href = "otra-pagina.html";
});

const respuestas = {};

for (const elemento of formulario.elements) {
    if (elemento.type === "radio" || elemento.type === "checkbox") {
        if (elemento.checked) {
            respuestas[elemento.name] = elemento.value;
        }
    } else if (elemento.type === "text") {
        respuestas[elemento.name] = elemento.value;
    }
}

const respuestas = {};

for (let i = 1; i <= 9; i++) {
    const pregunta = document.getElementById(`pregunta${i}`);
    const respuestaSeleccionada = pregunta.querySelector(".opcion.seleccionada");

    if (respuestaSeleccionada) {
        respuestas[pregunta.id] = respuestaSeleccionada.id;
    }
}
function mostrarRespuesta(preguntaId, respuestaId) {
    const respuestaElement = document.getElementById(`respuesta-${preguntaId}`);
    const respuesta = localStorage.getItem(respuestaId);

    if (respuesta) {
        respuestaElement.innerHTML = `Respuesta: ${respuesta}`;
    } else {
        respuestaElement.innerHTML = "";
    }
}