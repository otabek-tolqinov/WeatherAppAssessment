
let API_KEY = "78a96a8c1b99d70f3cf7f1659c3961ca"

document.getElementById("weatherForm").addEventListener("submit", function(event) {
    event.preventDefault();
});



let city_name = document.getElementById("cityInput").value

function fetchWeatherData() {
  fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${API_KEY}`)
    .then(response => response.json())
    .then(response => {
      console.log(response);
      localStorage.setItem("city_name", JSON.stringify(city_name))
      localStorage.setItem("temp", JSON.stringify((response.main.temp-273).toFixed(1)))
      localStorage.setItem("pressure", JSON.stringify(city_name))
      localStorage.setItem("weather_state", JSON.stringify(response.weather[0].description))
      document.getElementById("weather_state").innerHTML = response.weather[0].description;
      document.getElementById("temp").innerHTML=(response.main.temp-273).toFixed(1);
      document.getElementById("icon").src = `https://openweathermap.org/img/wn/${response.weather[0].icon}@2x.png`;
      document.getElementById("pressure").innerHTML = response.main.pressure;
    })
    .catch(err => {
      console.log(err);
    });




}