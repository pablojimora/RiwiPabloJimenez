const input = document.querySelector('input');
const addBtn = document.querySelector('.btn-add');
const ul = document.querySelector('ul');
const empty = document.querySelector('.empty');

addBtn.addEventListener('click', (e) => {
    e.preventDefault(); //Esta linea es para que no se recargue la pagina 


    const text = input.value;
    if (text !== "") {
        const li = document.createElement('li');
        const p = document.createElement('p');
        p.textContent = text;


        li.appendChild(p);
        li.appendChild(addDeleteBtn())
        ul.appendChild(li);

        input.value = ""; // Esto hace que cada vez que coloquemos le boton de añadir, el valor del input se va a convertir en blanco para que no se quede la tarea que agg
        empty.style.display = "none";
    }
});

function addDeleteBtn() {
    const deleteBtn = document.createElement('button');

    deleteBtn.textContent = "X"
    deleteBtn.className = "btn-delete";

    deleteBtn.addEventListener('click', (e) => {
        const item = e.target.parentElement;
        ul.removeChild(item);

        const items = document.querySelectorAll('li');

        if (items.length === 0){
            empty.style.display = "block";
        }
    });
    return deleteBtn;
}