//El metodo es llamar una funcion dentro de un objeto

const persona = {
    nombre: "Ana",
    edad: 25,
    ciudad: "Bogotá",
    apellido: "Suarez",
    skills:["html","CSS","PY","JS"],
    ladrar: function() {
        let a = 2;
        let b = 3;
        console.log(a+b);
        console.log("Guau!");;
    }
};

persona.ladrar()