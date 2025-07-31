//Se crea una const para guardar la ciudad 
const ciudad = "Medellin"
const API_KEY = "1572a88f681166d30636774bee65467d";

const request = async () => {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${ciudad}&appid=${API_KEY}&units=metric&lang=es`);
    const data = await response.json();
    console.log(response);
    console.log(data);
}

request()



