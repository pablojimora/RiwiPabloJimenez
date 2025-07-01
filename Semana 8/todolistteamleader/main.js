let tareas = []

function agregarTarea() {
    const input = document.getElementById("nuevaTarea");
    const text = input.value.trim();

    //Para que no se agreguen tareas vacias
    if (text == '') return


    const tarea = {
        id: Date.now(),
        task: text,
        isDone: false
    }

    console.log(tareas);
    
    tareas.push(tarea);


    //para que cuando se ponga una tarea se borre del input
    input.value = "";

    mostrarTareas()

}

function cambiarEstado(id) {
    for (let i = 0; i < tareas.length; i++) {

        if (id === tareas[i].id) {
            if(tareas[i].id === id) {
                tareas[i].isDone = !tareas[i].isDone;
            }
             // El signo de admiracion hace que cambie lo que recibe, o sea si recibe false, pasa true, y si esta en tru, pasa a false
        }
    }
    mostrarTareas();
}

function eliminarTarea(id) {
    for (let i = 0; i < tareas.length; i++) {

        if (tareas[i].id === id) {

            tareas.splice(i, 1) 
            break//Eliminar la tarea que esta en posicion i y solo quiero eliminr 1 tarea
        }
    }
    mostrarTareas();
}
function mostrarTareas() {

    const list = document.getElementById("listaTareas")
    list.innerHTML = ''

    for (let i = 0; i < tareas.length; i++) {
        const tarea = tareas[i];
        const li = document.createElement("li");

        li.className = tarea.isDone ? 'hecho' : ''  // esto esta validando que si la tarea esta en verdadera, le agregue a la clase, hecho, sino, no le agregue nada

        //Es para introducir texto, que seria la task, y lo de abajo se crean dos botones cada que se cree una tarea
        li.innerHTML = ` 
        ${tarea.task}
        <button onclick= "cambiarEstado(${tarea.id})" > ${tarea.isDone ? "Desmarcar" : "Hecho"}</button>
        <button onclick= "eliminarTarea(${tarea.id})" >eliminar</button>
        `;

        list.appendChild(li);

    }
}