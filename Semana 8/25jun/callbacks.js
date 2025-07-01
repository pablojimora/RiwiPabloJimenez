//ES una funcion que se pasa cmo parametro a otra para ser llamada luego
//ES fundamental para la programacion asincronica de JS

// function sumar(a,b){
//     let suma = a+b
//     return suma 
// }
// const result =sumar(2,4)
// const result2 =sumar(1000,4)


// console.log(result);
// console.log(result2);

function procesarEntrada(input,callback) {
    const nombre = input.toUpperCase();
    callback(nombre);
}

procesarEntrada("david", function(nombreProcesado){
    console.log("hola "+nombreProcesado);
});
procesarEntrada("Esteban", function(nombreProcesado){
    console.log("Chao "+nombreProcesado);
    console.log("Chao "+nombreProcesado);
    console.log("Chao "+nombreProcesado);
});
procesarEntrada("david", function(nombreProcesado){
    console.log("hola "+nombreProcesado);
});