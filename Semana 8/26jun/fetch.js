//Los fetchs nos permiten hacer llamados de APIS

//La API es una interfaz para acceder a datos de un servidor

// debo poner un fecth de ejemplo 










// Async
// El await no se puede utilizar sino es con async
// lo que hace es llegar a la web y darle pausa hasta que se responda
// el llamado a las peticiones
let users= ''

async function getUsers() {
    try{
        const res = await fetch("")
        const data = await res.json();
        console.log(data.title);
    } catch (err) {
        console.error("Error:", err);
    }
    finally {
        console.log("Se imprime al final");
    }
}


getUsers()

// console.log(users);

setTimeout(()=>{
    console.log(users);
},1000)

