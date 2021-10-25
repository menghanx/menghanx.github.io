const axios = require('axios');

const getTimelineURL = "https://api.tomorrow.io/v4/timelines";
const apikey = "oMxv2FQh3mL4u4wyRZ0lV4qKC8rTZxCh";
let location = "40.758,-73.9855";
const fields = "temperature,temperatureApparent,temperatureMin,temperatureMax,windSpeed,windDirection,humidity,pressureSeaLevel,uvIndex,weatherCode,precipitationProbability,precipitationType,sunriseTime,sunsetTime,visibility,moonPhase,cloudCover";
const units = "imperial";
const timesteps = "current,1h,1d";
const timezone = "America/Los_Angeles";

const weather_params = {
    "location": location,
    "fields": fields,
    "timesteps": timesteps,
    "units": units,
    "apikey": apikey,
    "timezone": timezone
}

parameters = {
    postId: 1
}

const placeholder = 'https://jsonplaceholder.typicode.com/comments';
const weatherAPI = 'https://jsonplaceholder.typicode.com/comments';

axios.get(`${getTimelineURL}`, {
    params: weather_params
}).then(resp => {
    // res.status(200).json(posts.data);
    console.log(resp.data)
}).catch(
    error => {
        console.log(error);
    }
)
