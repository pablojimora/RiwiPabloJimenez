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

console.log(Object.values(persona));
console.log(Object.keys(persona));
console.log(persona.hasOwnProperty("edad"));
console.log(Object.entries(persona));


