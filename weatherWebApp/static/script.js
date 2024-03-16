let getdate = new Date();
let get_hours = getdate.getHours();
let get_minutes = getdate.getMinutes();
let get_month = getdate.getMonth() + 1;
let get_day = getdate.getDate();
let get_year = getdate.getFullYear();
let formatted_time = `${get_hours}:${get_minutes}`;
let dateHTML = `<p>${get_month}/${get_day}/${get_year}</p>`;
document.getElementById("dateContainer").innerHTML = dateHTML;



const API_KEY = "78a96a8c1b99d70f3cf7f1659c3961ca";

var city_name = "Birmingham";
let lat;
let lon;

function knowPressure() {

  // Get input element by ID

  // Fetch weather data based on the new city
  fetchWeatherData();
}

function fetchWeatherData() {
  fetch(`http://127.0.0.1:8080/get-weather-by-city/Birmingham/`)
    .then(response => response.json())
    .then(response => {
    document.getElementById("weather_state").innerHTML = response.description;


    document.getElementById("temp").innerHTML=response.temp;

    document.getElementById("pressure").innerHTML=response.pressure;
    document.getElementById("icon").src = `https://openweathermap.org/img/wn/${response.icon}@2x.png`;

      // lon = response[0]["lon"];
      // lat = response[0]["lat"];
      // find_temp(lat, lon);
    })
    .catch(err => {
      console.log(err);
    });


}


// function find_temp(lat, lon){
//   fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}`)
//     .then(response => response.json())
//     .then(response => {
//     console.log(response);
//     document.getElementById("temp").innerHTML=response.temp;

//     document.getElementById("pressure").innerHTML=response.pressure;
//     document.getElementById("icon").src = `https://openweathermap.org/img/wn/${response.icon}@2x.png`;

//     })
//     .catch(err => {
//       console.log(err);
//     });
// }


