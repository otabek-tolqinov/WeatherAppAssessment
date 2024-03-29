let getdate = new Date();
let get_hours = getdate.getHours();
let get_minutes = getdate.getMinutes();
let get_month = getdate.getMonth() + 1;
let get_day = getdate.getDate();
let get_year = getdate.getFullYear();
let formatted_time = `${get_hours}:${get_minutes}`;
let dateHTML = `<p>${get_month}/${get_day}/${get_year}</p>`;


document.getElementById("weatherForm").addEventListener("submit", function(event) {
    event.preventDefault();
});

function fetchWeatherData() {
    fetch(`https://weatherappassessment.onrender.com/get-weather-by-city/Birmingham/`)
    .then(response => response.json())
    .then(response => {
        console.log(response)
        document.getElementById("weather_state").innerHTML = response['description'];
        document.getElementById("temp").innerHTML=response['temperature'];
        document.getElementById("pressure").innerHTML=response['pressure'];
        document.getElementById("icon").src = `https://openweathermap.org/img/wn/${response['icon']}@2x.png`;
    })
    .catch(err => {
        console.log(err);
    });
}