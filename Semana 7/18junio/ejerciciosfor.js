// For (inicializacion; condicion; incremento) {
// //codigo que se ejecuta en cada repeticion 
//}

for (let i=0; i<10; i++) {
    let multiplicacion
    multiplicacion=i*5
    console.log(`5*${i}=${multiplicacion}`)
}

for (let i=100; i>=10; i--) {
    let multiplicacion
    multiplicacion=i*5
    console.log(`el numero es ${i}`)
}

let dia="miercoles"
//switch case

switch (dia) {
    case "lunes":
        console.log("primer dia")
        break;
    case "martes":
        console.log("segundo dia")
        break;
    case "miercoles":
        console.log("tercer dia")
        break;
    case "jueves":
        console.log("cuarto dia")
        break;
    case "viernes":
        console.log("quinto dia")
        break;
    default:
        console.log("es otro dia")
}

//Ejemplo de switch
let user="admin"
let permision=0

switch(user) {
    case "admin":
        console.log("Tiene permisos para administrar");
        permision=1;
        break;
    
    case "superAdmin":
        console.log("Tiene todos los permisos para administrar y puede eliminar");
        permision=2;
        if (permision===2) {
            console.log("entro al sistema y puede eliminar usuarios")
        }
        let sumaPermisos =permision+4

        break;

}

// los 7 valores falsy en JS:
// 1. false
// 2. 0
// 3. -0
// 4. "" cadena vacia
// 5. null
// 6. undefined
// 7. NaN

//Condicional if, siempre se ejecuta si tiene una variable que es verdadera
let dato = "4748";
let datoInNumber;

datoInNumber = Number(dato)

console.log(dato)
console.log(datoInNumber)

if(datoInNumber){
    console.log("Es un numero")
} else {
    console.log("No es un numero")
} 
