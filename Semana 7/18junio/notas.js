// Calculadora de Promedio de Notas
 
 
// Enunciado:
// Crea un formulario con 5 campos numéricos (una nota por cada uno) y un botón “Calcular Promedio”. Al hacer clic:
 
// Una función debe tomar los valores, sumarlos en un for.
// Calcular el promedio y mostrarlo en el DOM.
// Usar una condicional para mostrar si el estudiante aprobó (promedio ≥ 3.0) o reprobó.
// usar validación de solo numeros en los campos de las notas.

function calcularPromedio(event) {
    event.preventDefault();
    let notas=[]

    notas.push(document.getElementById("n1").value)
    notas.push(document.getElementById("n2").value)
    notas.push(document.getElementById("n3").value)
    notas.push(document.getElementById("n4").value)
    notas.push(document.getElementById("n5").value)
    console.log(notas);

    let suma=0;
    let promedio
    
    for (i=0; i<notas.length; i++){
        notas[i] = Number(notas[i]);
        console.log(notas[i])
        if(notas[i]<0){
            document.getElementById("pabo").textContent = `Debes ingresar un valor positivo`
            return;
        }
        if (!notas[i] && notas[i]!==0) {
            document.getElementById("pabo").textContent = `Debes ingresar un valor numérico válido`
            return;
        }
        suma=suma+notas[i]
    }
    promedio=suma/notas.length;
    if (promedio>= 3){
        console.log(promedio);
        document.getElementById("pabo").textContent = `Su promedio es ${promedio}, aprobaste!`
    } else {
        document.getElementById("pabo").textContent = `Su promedio es ${promedio}, reprobaste`
    }
}
