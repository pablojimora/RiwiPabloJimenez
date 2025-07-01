// Una promesa representa un valor que puede estar disponible ahora,
// en el futuro o nunca. Tiene tres estados:
// PENDING (PENDIENTE), FULFILLED(CUMPLIDA), REJECTED(RECHAZADA)

const promesa = new Promise((resolve, reject) => {
    let exito = true

    setTimeout(() => {
        if (exito) {
            resolve(" la BD respondió")
        } else {
            reject("Error desconocido")
        }
    },4000)

});


//cuando se llama la promesa aparece then, catch y finally 
//El then es para 

promesa.then((result) => {
    console.log(result);
}
).catch((error) => {
    console.log(error);
})