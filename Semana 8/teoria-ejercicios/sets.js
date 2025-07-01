
//Los sets sriven para meter valores que no pueden estar duplicados, en este caso solo
// se va a imprimir a b y c porque a se repite 
const letras = new Set(["a","b","c","a"])

letras.add("z");
letras.add("b"); //No se agrega porque ya está
console.log(letras)

