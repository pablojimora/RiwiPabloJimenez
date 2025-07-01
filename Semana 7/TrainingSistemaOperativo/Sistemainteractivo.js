function mensaje(event) {
    event.preventDefault();
    let nombre = document.getElementById("nombre").value;
    let edad = document.getElementById("edad").value;

    if (isNaN(edad)) {
        document.getElementById("pabo").textContent = `Error: Por favor, ingresa una edad válida en números.`;
    } else if (edad < 18) {
        document.getElementById("pabo").textContent = `Hola ${nombre}, eres menor de edad, ¡Sigue aprendiendo y disfrutando del código! `;
    } else {
        document.getElementById("pabo").textContent = `Hola ${nombre}, eres mayor de edad, ¡Prepárate para grandes oportunidades en el mundo de la programación!`;
}

}


mensaje()