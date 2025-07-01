const nombre = "Juan";


const persona = {
    nombre: "Ana",
    edad: 25,
    ciudad: "Bogotá",
    apellido: "Suarez",
    skills:["html","CSS","PY","JS"],
};

//Para agregar propiedad a persona es asi

// persona.isActive=true
persona["isActive"]=true

// Se puede de las dos formas 
console.log(persona);


//Destructurar objeto
const { nombre:nombreObject, edad, ciudad, apellido="Jimenez", skills } = persona

const [uno, dos, eltercero]=skills

console.log(uno);
console.log(dos);

console.log(eltercero);

// console.log(nombre);
// console.log(edad);
// console.log(ciudad);
// console.log(apellido);


// const{uno, dos} = skills