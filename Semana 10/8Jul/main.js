console.log(object);

function handle(){
    const boxs = document.getElementsByClassName('box');
    // console.log(boxs[4])
    // const caja5 = boxs[4]
    // caja5.style.backgroundColor = 'red';
    const caja2= boxs[1];

    //con este solo agrega la clase done y no cambia de color cuando se vuelve a pulsar
    // caja2.classList.add('done');


    //con este quita la clase done y cambia de color cuando se vuelve a pulsar
    caja2.classList.toggle('done');

    caja2.classList.contains('done') ? console.log('tiene la clase done') : console.log('no tiene la clase done');
}