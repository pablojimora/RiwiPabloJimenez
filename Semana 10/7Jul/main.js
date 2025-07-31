const cambiar = () => {
    titulo=document.getElementById("titulo");
    titulo.textContent = "Hola Mundo";
}


//Function to append elements to the list
let contador= 0;
const append = () => {
    const lista = document.getElementById("lista");
    const li = document.createElement("li");
    li.textContent = `Elemento ${contador}`;
    contador++;
    lista.appendChild(li);
}