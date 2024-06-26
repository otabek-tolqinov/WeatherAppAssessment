
let API_KEY = "ade9f4cabec74e36b585f951ace85a05"

document.getElementById("weatherForm").addEventListener("submit", function(event) {
    event.preventDefault();
});





function fetchWeatherData() {
  city_name = document.getElementById("cityInput").value

  if (localStorage.when != null
  && parseInt(localStorage.when) + 10000 > Date.now()) {

  let sec = Math.round((Date.now() - localStorage.when)/1000);

  document.getElementById("weather_state").innerHTML = localStorage.weather_state;
      document.getElementById("temp").innerHTML=localStorage.temp;
      document.getElementById("city_name").innerHTML = localStorage.city_name;
      document.getElementById("pressure").innerHTML = localStorage.pressure;
  } else {
    city_name = document.getElementById("cityInput").value

  fetch(`https://weatherappassessment.onrender.com/get-weather-by-city/${city_name}/`)
    .then(response => response.json())
    .then(response => {
      console.log(response);
      localStorage.setItem("city_name", JSON.stringify(city_name))
      localStorage.setItem("temperature", JSON.stringify(response.temperature))
      localStorage.setItem("pressure", JSON.stringify(city_name))
      localStorage.setItem("weather_state", JSON.stringify(response.description))

      document.getElementById("city_name").innerHTML = city_name;
      document.getElementById("weather_state").innerHTML = response.description;
      document.getElementById("temp").innerHTML=response.temperature;
      document.getElementById("icon").src = `https://openweathermap.org/img/wn/${response.icon}@2x.png`;
      document.getElementById("pressure").innerHTML = response.pressure;
    })
    .catch(err => {
      console.log(err);
    });

  }









}