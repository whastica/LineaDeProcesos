// Import the necessary classes
import { Actividad } from './actividad.js';
import { Usuario } from './usuario.js';
import { Requisitos } from './requisitos.js';
import { Proceso } from './proceso.js';
import { Aplicacion } from './aplicacion.js';

// Define the application startup function
async function iniciarAplicacion() {
    // Create an instance of the `Usuario` class
    const usuario = new Usuario('Nombre del usuario', 'correo@ejemplo.com', 'Nombre de la aplicación');

    // Create an instance of the `Requisitos` class
    const requisitos = new Requisitos();

    // Create an instance of the `Proceso` class
    const proceso = new Proceso('Proceso de creación de aplicación de mensajería instantánea', 1);

    // Start the application process
    await proceso.iniciar();
}

// Call the application startup function
iniciarAplicacion();