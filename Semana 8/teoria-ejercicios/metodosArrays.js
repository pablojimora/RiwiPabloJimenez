const personas =[
    {nombre:"Luis", edad:40},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},
    {nombre:"Ana", edad:30},

]

const numeros = [1,2,3];

// numeros.push(4) //AGrega al final
// numeros.pop() //ELimina el ultimo elemento
// numeros.shift() //Elimina el primer elemento
// numeros.unshift('a') //Agrega un elemento al inicio
// const miFiltro = numeros.filter(num => num == 2) //Filtra los elementos que cumplen cierta condicion
//const find = numeros.find(num => num==2) // Encuentra el primer elemento que cumpla la condición.
const existe = numeros.includes(2) // Verifica si un elemento existe en el Array

console.log(existe);
