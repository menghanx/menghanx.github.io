// express app
const express = require('express');
const app = express();
// enable json middleware
app.use(express.json());
// HTTP GET by axios
const axios = require('axios');
// Weather.io Parameters
let location = "";
const getTimelineURL = "https://api.tomorrow.io/v4/timelines";
const apikey = "oMxv2FQh3mL4u4wyRZ0lV4qKC8rTZxCh";
const fields = "temperature,temperatureApparent,temperatureMin,temperatureMax,windSpeed,windDirection,humidity,pressureSeaLevel,uvIndex,weatherCode,precipitationProbability,precipitationType,sunriseTime,sunsetTime,visibility,moonPhase,cloudCover";
const units = "imperial";
const timesteps = "current,1h,1d";
const timezone = "America/Los_Angeles";

// DEBUG
const fs = require('fs');

let rawdata = fs.readFileSync('dummy.json');
let dummyData = JSON.parse(rawdata);

// CORS
const cors = require('cors');
app.use(cors({
    origin: '*'
}));

//  What to do for homepage
app.get('/', (req, res) => {
    res.send('hello world!');
});

// flag debug
var debug = true;

// tomorrow.io get weather data
app.get('/api/weather', (req, res) => {
    if (debug) {
        // return dummy data
        res.status(200).json(dummyData);
    } else {
        // obtain latitude and longtitude from params
        if (req.query.loc) {
            location = req.query.loc
            weather_params = {
                "location": location,
                "fields": fields,
                "timesteps": timesteps,
                "units": units,
                "apikey": apikey,
                "timezone": timezone
            }
            axios.get(`${getTimelineURL}`, {
                params: weather_params
            }).then(resp => {
                res.status(200).json(resp.data);
            }).catch(
                error => {
                    res.status(500).send(error);
                }
            )
        } else {
            res.status(404).json({ "Response": "Invailid request, parameter missing. Expected params: loc={lat},{lng}" });
        }
    }



});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));