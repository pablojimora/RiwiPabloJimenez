const frutas = ["Manzana","Banano","Fresa"];
const lista = document.createElement("ul");

frutas.forEach(function(fruta) {
    const item = document.createElement("li");

})

document.body.appendChild(lista);

const frutasUppercase = frutas.map(fruta => fruta.toUpperCase)
console.log(frutasUppercase);