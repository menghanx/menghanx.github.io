// input validation
const Joi = require('joi');
const express = require('express');
const app = express();

// enable json middleware
app.use(express.json());

weathers = [
    { id: 1, name: 'weather 1' },
    { id: 2, name: 'weather 2' },
    { id: 3, name: 'weather 3' }
];


//  GET and call back function
app.get('/', (req, res) => {
    res.send('hello world!');
});

// weather api, take req -> get params -> build new req to tomorrow.io
// -> put resp from tomorrow to res -> [optional] process json -> res.send
app.get('/api/weather', (req, res) => {
    res.send(weathers);
});

// Handle POST
app.post('/api/weathers', (req, res) => {

    const schema = {
        name: Joi.string().min(3).required()
    }

    const result = Joi.validate(req.body, schema);
    console.log(result);

    if (result.error) {
        res.status(400).send(result.error);
        return;
    };

    const w = {
        id: weathers.length + 1,
        name: req.body.name
    }
    weathers.push(w);
    res.send(weathers);
});

// query params
app.get('/api/weather/:id', (req, res) => {
    w = weathers.find(c => c.id === parseInt(req.params.id));
    if (!w) res.status(404).send('The weather data is not available');
    res.send(w);
});

app.get('/api/posts', (req, res) => {
    res.send(req.query);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));