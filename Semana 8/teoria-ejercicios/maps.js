// Es una colección

const mapVariado = new Map();
const obj ={id:1};
const func = function() {};
const numero= 42;

mapVariado.set(obj, true);
mapVariado.set(func, "función como clave");
mapVariado.set(numero,"Numero como clave");

console.log(mapVariado);
//eN ESTE CASO EL 42, SERIA LA CLAVE OARA OBTENER "NUMERO COMO CLAVE"
console.log(mapVariado.get(42));