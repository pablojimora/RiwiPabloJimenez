const handleClick = async () => {

try {
    const variable = 110

    if (variable == 12){
        console.log("es igual");
    } else {
        throw new Error ("El numero es diferente")
    }
} catch (error){
    console.log(error.message);
}





    // //EL try catch sirve para el manejo de errores, y permite que el programa siga funcionando si se presenta un error 
    // try {

    //     await fetch("http://localhost:3000/usuarios", {
    //         method: 'POST',
    //         headers: {
    //             bearerToken: 'iosahdj3klmnk23n4',
    //             'Content-type': 'application'
    //         },
    //         body: {
    //             id: "3",
    //             nombre: "Juan",
    //             edad: 28,
    //         }
    //     })
    // }
    // catch{

    // }
}

handleClick()