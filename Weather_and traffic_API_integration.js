const axios = require('axios');

async function getWeatherData(location) {
  const apiKey = 'YOUR_OPENWEATHERMAP_API_KEY';
  const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=${location[0]}&lon=${location[1]}&appid=${apiKey}`);
  return response.data.weather[0].description;
}

async function getTrafficData(location) {
  const apiKey = 'YOUR_GOOGLE_MAPS_API_KEY';
  const response = await axios.get(`https://maps.googleapis.com/maps/api/traffic?location=${location}&key=${apiKey}`);
  return response.data.status;
}

module.exports = { getWeatherData, getTrafficData };
