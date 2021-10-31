// express app
const express = require('express');
const app = express();
// enable json middleware
app.use(express.json());
// HTTP GET by axios
const axios = require('axios');
require('axios-debug-log');

// CORS
app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', '*');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});

// Weather.io Parameters
let location = "";
const getTimelineURL = "https://api.tomorrow.io/v4/timelines";
const apikey = "oMxv2FQh3mL4u4wyRZ0lV4qKC8rTZxCh";
const fields = "temperature,temperatureApparent,temperatureMin,temperatureMax,windSpeed,windDirection,humidity,pressureSeaLevel,uvIndex,weatherCode,precipitationProbability,precipitationType,sunriseTime,sunsetTime,visibility,moonPhase,cloudCover";
const units = "imperial";
const timesteps = "current,1h,1d";
const timezone = "America/Los_Angeles";

// Autocomplete Parameters
const autoURL = "https://maps.googleapis.com/maps/api/place/autocomplete/json";
const autoKEY = "AIzaSyCLJBmNPC4h2bQlqiUl17X0m0hzYMgKzAs";
const autoTypes = "(cities)";


//  What to do for homepage
app.get('/', (req, res) => {
    res.send('hello world!');
});

// Autocomplete data
app.get('/api/auto', (req, res) => {

    if (req.query.input) {
        location = req.query.input
        auto_params = {
            "input": location,
            "key": autoKEY,
            "types": autoTypes
        }

        axios.get(`${autoURL}`, {
            params: auto_params
        }).then(resp => {
            if (resp.data.predictions.length === 0) {
                res.status(200).json(resp.data.predictions);
            } else {
                output = []
                for (item of resp.data.predictions) {
                    city = item.terms[0].value;
                    state = item.terms[1].value;
                    output.push(
                        {
                            "city": city,
                            "state": state
                        }
                    );
                }
                res.status(200).json(output);
            }

            // res.status(200).json(resp.data.predictions);
        }).catch(
            error => {
                res.status(500).send(error);
            }
        )
    } else {
        res.status(404).json({ "Response": "Invailid request, parameter missing. Expected params: input={string}" });
    }
});

// tomorrow.io get weather data
app.get('/api/weather', (req, res) => {
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
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));