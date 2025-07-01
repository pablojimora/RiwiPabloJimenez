//Es posible llamar la funcion antes de la definicion de la funcion
// sumar()

function sumar(value, value2) {
    let result;

    result = value + value2;
    console.log(result);
}

const sumar2 = (value, value2) => {
    console.log(``)
}

sumar(11, "22") //Cuando se coloca eso pasa a concadenar 
sumar(11 ,22) //Asi si se suma


let contador = 0

function incrementar() {
    contador=contador+1
    console.log(contador)
    document.getElementById("contador").textContent=contador
}

const decrementar = () => {
    contador = contador - 1
    console.log(contador)
    document.getElementById("contador").textContent=contador
}
const reset = () => {
    contador= 0
    console.log(contador)
    document.getElementById("contador").textContent=contador
}
