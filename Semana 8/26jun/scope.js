//Scope: lo que pasa es que se pueden decalrar variables de igual nombre
//si una esta dentro de una funcion, y la otra es global, pero
//sino se decalra la variable dentro de la funcion con let o var
//Hace que esa que no esta con estas claves sea reasignacion
//y va a priorizar las de funciones  
var animal = "perro";


// function mostrarAnimal() {
//     let animal = "Gato";         //Esta y la de abajo hacen lo mismo
//     console.log(animal);
// }

const mostrarAnimal = () => {
    let animal = "Gato";
    console.log(animal);
}
mostrarAnimal();

// // El set time out, sirve para configurar el tiempo en el que se 
// //realice una funcion 

// for (let i = 0; i <3 ; i++) {
//     setTimeout (() => {
//         console.log(i);
//     }, 1);
// }


// //this sirve en funciones declaradas por metodo clasico

// const persona = {
//     nombre: "David",
//     saludar: function() {
//         console.log("Hola, soy "+ this.nombre);
//     }
// }
// persona.saludar()