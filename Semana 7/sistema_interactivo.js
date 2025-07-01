//Inicialización del programa 
console.log("¡Bienvenido al Sistema Interactivo de Mensajes");

//Capturar datos del usuario
let nombre= prompt("Por favor, ingresa tu nombre: ");
let edad = prompt("Por favor, ingresa tu edad: ");

//Convertir la edad en número
edad=parseInt(edad);

//Código para validacion y mensajes:
if (isNaN(edad)) {
    console.error("Error: Por favor, ingresa una edad válida en números.");
} else if (edad < 18){
    alert(`Hola ${nombre}, eres menor de edad, ¡Sigue aprendiendo y disfrutando del código! `);
} else {
    alert(`Hola ${nombre}, eres mayor de edad, ¡Prepárate para grandes oportunidades en el mundo de la programación!`)
}
