//Es una funcion que recuerda el contecto en el que fue creada, puede acceder a variables definidas
// fuera de ella incluso después de que el contexto haya terminado

function crearContador(){
    let count = 0;
    return function (){
        count ++;
        console.log(count);
    }
}
const contar = crearContador();
contar();
contar();
contar();

//ejemplo 2 

function crearSaludo(saludo){
    return function (nombre) {
        console.log(`${saludo},${nombre}`);
    }
}
const saludar = crearSaludo();
saludar("Pablo");