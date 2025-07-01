//Escribe un programa en JavaScript que imprima los números del 1 al 100 en el DOM, pero siguiendo estas reglas:
// •Por cada número divisible por 3, imprime “Fizz” en lugar del número.
// •Por cada número divisible por 5, imprime “Buzz” en lugar del número.
// •Para los números divisibles por ambos 3 y 5, imprime “FizzBuzz”.
// •Si el número no es divisible ni por 3 ni por 5, imprime el número normalmente.

function FizzBuzz() {

    for (var i = 0; i < 101; i++) {

        if ((i % 3 == 0) && (i % 5 == 0)) {
            document.getElementById("pabo").textContent += "FizzBuzz \n";
        } else if (i % 5 == 0) {
            document.getElementById("pabo").textContent += "Buzz \n";
        } else if (i % 3 == 0) {
            document.getElementById("pabo").textContent += "Fizz \n";
        } else {
            document.getElementById("pabo").textContent += " " + i + " ";
        }
    }
}
FizzBuzz()