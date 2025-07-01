console.log("Hola mundo");

let nombre = "David";
let edad = 18;
let persona = {nombre:"Ana", edad:23};
let numeros = [1, 2, 3];
let nada = null;
let miVariable;

let users = [
    { nombre2: "Ana", apellido: "Macías", edad: 22, isActive: true},
    { nombre2: "Luis", apellido: "Henao", edad: 22, isActive: true},
    { nombre2: "Catalina", apellido: "Macías", edad: 22, isActive: true},
    { nombre2: "Ana", apellido: "Bustamante", edad: 22, isActive: true},

]

let products = {
    motos: [{yamaha:2},{kawasaki:5}]
}

//Es igual el numero?, para comparar nada ams el valor, se usan 2 iguales, y para comparar
//con el tipo de dato, poner 3 iguales, con el diferente para el tipo de dato seria con dos iguales
// num1 = 22
// num2 = "22"

// if (num1 != num2) {
//     console.log("Es diferente")
// } else {
//     console.log("Es igual")
// }

//elif 
let entrada = 14

let num1 = 10
let num2 = 30

if (entrada < num1) {
    console.log("Es menor que 10")
} else if ((entrada > num1) && (entrada < num2)) { //Asi se pone el and en js &&
    console.log("El valor esta entre 10 y 30")
} else {
    console.log("Es mayor que 30")
}
//Se cumple o no se cumple el if

let activo = true; 
let newUser = false;
if (activo || newUser) {   //Asi se pone el or en js &&
    console.log("Se cumple el if")
} else {
    console.log("No se cumple el if")
}

//Asi se pone un condicional en una sola linea
activo == !newUser ? console.log("Se cumple") : console.log("no se cumple")


//Operaciones aritmeticas

let result

let a = 2
let b = 2

result = a + b
console.log(result)

// es mayor de edad? 
if (edad >= 18) {
    console.log("Es mayor de edad")
} else {
    console.log("Es menor de edad")
}
//Para imprimir solo la key, si le quitas el object.keys, se imprime el obejto en esa posicion
console.log(Object.keys(products.motos[1]))

console.log(users[3].apellido)

console.log(persona.edad)

console.log(typeof nombre);

let Name2 = "Camila";
let lastName = "Acosta";
const iva = 19.2;
let isActive = true;


console.log(miVariable)

console.log(numeros[2])