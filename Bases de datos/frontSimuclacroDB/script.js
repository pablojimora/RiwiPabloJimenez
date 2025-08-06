import {get, post, update, deletes} from './services.js'

const urlUsers= "http://localhost:3000/users"

function obtener_datos() {
    try {
        let containerUsers = document.getElementById("users-container");
        containerUsers.innerHTML = ""; // limpiar antes de mostrar

        let userData = get(urlUsers)
        
        userData.then((data) => {
            console.log(data)
            data.forEach(user => {
                let userElement = document.createElement("div");
                userElement.className = "user";
                userElement.innerHTML = `
                <div class="event-info">
                <p style= display:none >ID: ${user.id}</p>
                <p>Nombre: ${user.nombre}</p>
                <p>Apellido: ${user.apellido}</p>
                <p>Departamento: ${user.departamento}</p>
                <p>Salario:${user.salario}</p>
                <p>Fecha de ingreso:${user.fecha_ingreso.split("T")[0]}</p>
                <button class="edit-user-btn" >Editar</button>
                <button class="delete-user-btn">Borrar</button>
                </div>
                `;
                containerUsers.appendChild(userElement);
            });
        }).catch(error => {
        console.error("Error fetching users:", error);
    });
       
    } catch (error) {
        console.error("Error:", error);
    }
}

document.addEventListener("DOMContentLoaded", obtener_datos);


//Este bloque sirve para que se pueda capturar el id del usuario que se va a editar
//Esto se hace por medio de delegacion de eventos: permite manejar elementos dinamicos, que no estan por defecto en el DOM 
let userId;

document.getElementById("users-container").addEventListener("click", async function (event) {
    if (event.target.matches('button[class="edit-user-btn"]')) {
        // Obtener el ID del usuario
        userId = event.target.parentElement.querySelector("p").textContent.split(": ")[1];
        console.log("ID del usuario a editar:", userId);

        // Traer solo ese usuario
        const data = await get(urlUsers);

        // Buscar usuario específico
        const userToEdit = data.find(user => user.id == userId);

        if (userToEdit) {
            document.getElementById("name").value = userToEdit.nombre;
            document.getElementById("lastName").value = userToEdit.apellido;
            document.getElementById("department").value = userToEdit.departamento;
            document.getElementById("age").value = userToEdit.edad;
            document.getElementById("salary").value = userToEdit.salario;
            document.getElementById("dateAdmission").value = userToEdit.fecha_ingreso.split("T")[0];

            document.getElementById("submit-btn").textContent = "Guardar cambios";
        }
    }
});


function addUser() {
    const form = document.getElementById("new-user-form");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const nombre = document.getElementById("name").value.trim();
        const apellido = document.getElementById("lastName").value.trim();
        const departamento = document.getElementById("department").value.trim();
        const edad = parseInt(document.getElementById("age").value);
        const salario = parseFloat(document.getElementById("salary").value);
        const fecha_ingreso = document.getElementById("dateAdmission").value.trim();

        const newUser = {
            nombre,
            apellido,
            departamento,
            edad,
            salario,
            fecha_ingreso
        };

        console.log("Enviando usuario:", newUser);

        try {
            // con este condicional hago que si hay un userId haga la actualziacion y si no hay haga el agregar
            if (userId) {
                await update(urlUsers, userId, newUser);
                alert(" El usuario fue actualizado correctamente");
                form.reset();
                obtener_datos();

            } else {

            
            await post(urlUsers, newUser);
            alert(" El usuario fue agregado correctamente");
            form.reset();
            obtener_datos();
            }
        } catch (error) {
            console.log("Error agregando usuario:", error);
        }
    });
}

addUser()

//Este bloque sirve para que se pueda capturar el id del usuario que se va a eliminar

// Este bloque sirve para capturar el id del usuario que se va a eliminar
let userIddel;

document.getElementById("users-container").addEventListener("click", function (event) {
    if (event.target.matches('button[class="delete-user-btn"]')) {
        userIddel = event.target.parentElement.querySelector("p").textContent.split(": ")[1];
        console.log(userIddel);
        deleteUser(userIddel);
    }
});

// Función para eliminar usuarios
async function deleteUser(userIddel) {
    console.log(`El usuario eliminado es: ${userIddel}`);
    try {
        await deletes(urlUsers, userIddel);
        alert("El usuario fue eliminado correctamente");
    } catch (error) {
        alert("No se pudo eliminar el usuario. Verifica el ID.");
        console.error("Error eliminando usuario:", error);
    }
}

// function updateUser() {
//     const form = document.getElementById("new-user-form");
//     form.addEventListener("submit", async (e) => {
//         e.preventDefault();

//         const nombre = document.getElementById("name").value.trim();
//         const apellido = document.getElementById("lastName").value.trim();
//         const departamento = document.getElementById("department").value.trim();
//         const edad = parseInt(document.getElementById("age").value);
//         const salario = parseFloat(document.getElementById("salary").value);
//         const fecha_ingreso = document.getElementById("dateAdmission").value.trim();

//         const updatedUser = {
//             nombre,
//             apellido,
//             departamento,
//             edad,
//             salario,
//             fecha_ingreso
//         };
//         console.log("Actualizando usuario:", updatedUser);

//         try {
//             await update(urlUsers, userId, updatedUser);
//             alert(" El usuario fue actualizado correctamente");
//             form.reset();
//             obtener_datos();
//         } catch (error) {
//             console.log("Error actualizando usuario:", error);
//         }
//     });
// }
// updateUser()