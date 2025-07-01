
//El for of sirve para recorrer la lista con objetos
const frutas = ["manzana", "pera", "uva"];

for (const fruta of frutas) {
    console.log(fruta);
}

// for in 

const persona2={
    nombre:"Luis", 
    edad:22
};
for(const clave in persona2){
    console.log(clave);
    console.log(persona2[clave]);
};

// const persona = {
//     nombre: "Ana",
//     edad: 25,
//     ciudad: "Bogotá",
//     apellido: "Suarez",
//     skills:["html","CSS","PY","JS"],
//     ladrar: function() {
//         let a = 2;
//         let b = 3;
//         console.log(a+b);
//         console.log("Guau!");;
//     }
// };

// for (const clave in persona){
//     console.log(clave);
//     console.log(persona[clave]);
// }

const personas =[
    {nombre:"Luis", edad:40},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},

]
//Crea una tabla en la consola
console.table(personas);

const colores = ["rojo", 
    "verde", 
    "azul",
    true,
    {
        id:1
    },
];
console.log(colores[4]?.name2);
//Aca imprime el nuevo tamaño del array
console.log(colores.push("gris"));

console.log((colores[3]));
