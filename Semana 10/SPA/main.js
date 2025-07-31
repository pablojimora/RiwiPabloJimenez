import { get, post, update, deletes } from './services.js';


const urlUsers = 'http://localhost:3000/users';

const routes = {
    '/login': './views/login.html',
    '/': './views/users.html',
    '/users': './views/users.html',
    '/newuser': './views/newUsers.html',
    '/about': './views/about.html',
    '/updateuser': './views/updateUser.html'
};

let counter = 0;

// Esta función verifica si el usuario está autenticado
function isAuth() {
    let result = localStorage.getItem('Auth') || null
    const resultBool = result === 'true'
    return resultBool;
}

function isAdmin() {
    let result = localStorage.getItem('role') || null
    const resultBool = result === 'true'
    return resultBool;
}

async function navigate(pathname) {
    // Verifica si el usuario está autenticado para permitir la entrada a las vistas
    if (!isAuth()) {
        pathname = '/login';
    }
    if (!isAdmin()) {
        if (pathname === '/newuser' || pathname === '/updateuser') {
            alert("No tienes permisos para acceder a esta página");
            pathname = '/users';
        }
    }

    const route = routes[pathname];
    const html = await fetch(route).then(res => res.text());
    document.getElementById('content').innerHTML = html;
    history.pushState({}, '', pathname);
    // Verifica si la ruta es '/about' para ejecutar la función de contador
    //Y asi debo llamar a cada funcion de las diferentes vistas
    if (pathname === '/about') {
        functionCount();
    }
    if (pathname === "/login") {
        setupLoginForm()
    };
    if (pathname === '/users') {
        showUsers();
    }
    if (pathname === '/newuser') {
        addUser();
    }
    if (pathname === '/updateuser') {
        updateUser();
    }

};

//Debo comenzar a escuchar eventos para capturar las funciones por medio de los botones

document.body.addEventListener('click', (e) => {
    if (e.target.matches("[data-link]")) {
        //Estas lineas son para evitar que el navegador recargue la pagina
        e.preventDefault();
        //Esta linea es para navegar a la ruta que se le pasa como parametro
        const path = e.target.getAttribute('href');
        navigate(path);
    }
});

function functionCount() {
    const counterValue = document.getElementById('counter-value');
    const incrementBtn = document.getElementById('increment-btn');
    const decrementBtn = document.getElementById('decrement-btn');

    incrementBtn.addEventListener("click", () => {
        counter++;
        counterValue.textContent = counter;
    });
    decrementBtn.addEventListener("click", () => {
        counter--;
        counterValue.textContent = counter;
    });
};

// Esta funcion sirve para devolverme a la pagina anterior
window.addEventListener("popstate", () => {
    console.log("se hizo clic");
    console.log(location);
    navigate(location.pathname);
});


//funcion del  login 
function setupLoginForm() {

    const form = document.getElementById("login-spa");

    // Sirve para que busque en los co rreos y contraseña
    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const user = document.getElementById("user").value;
        const pass = document.getElementById("password").value;
        fetch(urlUsers)
            .then(response => response.json())
            .then(data => {
                //Con esto se obtienen todos los datos del usuario que tenga el email ingresado, sino se encuentra, este va a retornar un undefined:false
                const usuario = data.find(userEmail => userEmail.email === user);
                if (!usuario || pass !== usuario.password) {
                    alert("Usuario o contraseña incorrectas");
                    return;
                }
                if (usuario.role === "admin") {
                    localStorage.setItem("role", "true");
                } else {
                    localStorage.setItem("role", "false");
                }
                localStorage.setItem("Auth", "true");
                navigate("/users");
            });
    })
};

//Funcion para cerrar sesion 
const buttonCloseSession = document.getElementById("close-sesion");
buttonCloseSession.addEventListener("click", () => {
    localStorage.setItem("Auth", "false");
    navigate("/login");
});


window.addEventListener("DOMContentLoaded", () => {
    navigate(location.pathname);
});

//Funcion para mostrar usuarios

function showUsers() {
    let containerUsers = document.getElementById("container-users");

    let userData = get(urlUsers)

    userData.then((data) => {
        data.forEach(user => {
            let userElement = document.createElement("div");
            userElement.className = "user";
            userElement.innerHTML = `
                <div class="user-info">
                <img class="profile-photo" src="./images/e926f691a012af425ff39d25b0ca54f0223c82cf.jpg" alt="">
                <h3 class="users-title">${user.name}</h3>
                <p>ID: ${user.id}</p>
                <p>Email: ${user.email}</p>
                <p>Phone: ${user.phone}</p>
                <p>Enrollment Number: ${user.enrollNumber}</p>
                <p>Date of Admission: ${user.dateOfAdmission}</p>
                <p>Role: ${user.role}</p>
                <button class="edit-user-btn"><i class="fa-solid fa-pen"></i></button>
                <button class="delete-user-btn" ><i class="fa-solid fa-trash"></i></button>
                </div>
            `;
            containerUsers.appendChild(userElement);
            //Condicional para ocultar los botones de editar y borrar si el usuario no es admin
            if (!isAdmin()) {
                const editButtons = document.querySelectorAll('.edit-user-btn');
                const deleteButtons = document.querySelectorAll('.delete-user-btn');
                editButtons.forEach(button => button.style.display = 'none');
                deleteButtons.forEach(button => button.style.display = 'none');
            }
        });
    }).catch(error => {
        console.error("Error fetching users:", error);
    });

};

//Funcion para agregar usuarios
function addUser() {
    const form = document.getElementById("new-user-form");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const phone = document.getElementById("phone").value;
        const enrollNumber = document.getElementById("enrollNumber").value;
        const dateOfAdmission = document.getElementById("dateOfAdmission").value;
        const userRole = document.getElementById("userRole").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirmPassword").value;

        if (!name || !email || !phone || !enrollNumber || !dateOfAdmission || !userRole) {
            alert("Por favor, completa todos los campos.");
            return;
        }
        if (password !== confirmPassword) {
            alert("Las contraseñas no coinciden.");
            return;
        }

        const newUser = {
            name: name,
            email: email,
            phone: phone,
            enrollNumber: enrollNumber,
            dateOfAdmission: dateOfAdmission,
            role: userRole,
            password: password
        };


        try {
            await post(urlUsers, newUser);
            alert("Usuario agregado correctamente");
            navigate("/users");
        } catch (error) {
            console.error("Error adding user:", error);
        }
    });
}

//Este bloque sirve para que se pueda capturar el id del usuario que se va a editar
//Esto se hace por medio de delegacion de eventos: permite manejar elementos dinamicos, que no estan por defecto en el DOM 
let userId;

document.getElementById("content").addEventListener("click", function (event) {

    if (event.target.matches('button[class="edit-user-btn"]')) {
        // El query selector busca el primer p del parent del boton seleccionado, el cual es el id
        userId = event.target.parentElement.querySelector("p").textContent.split(": ")[1];
        navigate("/updateuser");
    }
});

//Funcion para actualizar usuarios 

function updateUser() {
    const form = document.getElementById("update-user-form");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const name = document.getElementById("nameUP").value;
        const email = document.getElementById("emailUP").value;
        const phone = document.getElementById("phoneUP").value;
        const enrollNumber = document.getElementById("enrollNumberUP").value;
        const dateOfAdmission = document.getElementById("dateOfAdmissionUP").value;
        

        const updatedUser = {
            name: name,
            email: email,
            phone: phone,
            enrollNumber: enrollNumber,
            dateOfAdmission: dateOfAdmission
        };
        console.log(updatedUser)
        try {
            await update(urlUsers, userId, updatedUser);
            alert("Usuario actualizado correctamente");
            navigate("/users");
        } catch (error) {
            alert("No se pudo actualizar el usuario. Verifica el ID.");
            console.error("Error updating user:", error);
        }
    });
}

//Este bloque sirve para que se pueda capturar el id del usuario que se va a eliminar

let userIddel;

document.getElementById("content").addEventListener("click", function (event) {

    if (event.target.matches('button[class="delete-user-btn"]')) {
        // 
        userIddel = event.target.parentElement.querySelector("p").textContent.split(": ")[1];
        deleteUser(userIddel);
    }
});

//Funcion para eliminar usuarios
async function deleteUser(userIddel) {
    console.log(`EL usuario fue eliminado es: ${userIddel}`);
    try {
        await deletes(urlUsers, userIddel);
        alert("Usuario fue eliminado correctamente correctamente");
        navigate("/users");
    } catch (error) {
        alert("No se pudo eliminar el usuario. Verifica el ID.");
        console.error("Error updating user:", error);
    }
}



