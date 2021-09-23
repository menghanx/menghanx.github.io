import json
import re
import urllib
from datetime import datetime
from urllib import parse
from urllib.request import urlopen

import jyserver.Flask as jsf
from flask import Flask, jsonify, current_app, request

app = Flask(__name__)


@app.route("/")
def home():
    # button tutorial
    # return App.render(render_template('index.html'))
    return current_app.send_static_file('index.html')


@app.route("/weather-api/json", methods=['GET'])
def get_weather():
    # if param contains loc:"lat,lng"
    if 'loc' in request.args:
        geo_location = request.args.get('loc')
    # else use geo api to look up
    else:
        if 'street' not in request.args:
            return "Error: No street param"
        if 'city' not in request.args:
            return "Error: No city param"
        if 'state' not in request.args:
            return "Error: No state param"

        # build url to get geo data
        street = request.args.get('street')
        city = request.args.get('city')
        state = request.args.get('state')
        address = street.strip() + ", " + city.strip() + ", " + state.strip()
        GEO_API_KEY = "AIzaSyCLJBmNPC4h2bQlqiUl17X0m0hzYMgKzAs"
        params = {
            "key": GEO_API_KEY,
            "address": address
        }
        querystring = parse.urlencode(params)

        # GET geo_url
        geo_url = "https://maps.googleapis.com/maps/api/geocode/json?"+querystring
        try:
            geo_response = urlopen(geo_url)
        except urllib.error.URLError as e:
            print("HTTP Response: " + str(e.code))
            print("Bad Request!!")

        try:
            geo_data = json.loads(geo_response.read())
        except:
            geo_data = None

        lat = geo_data['results'][0]['geometry']['location']['lat']
        lng = geo_data['results'][0]['geometry']['location']['lng']
        geo_location = str(lat) + "," + str(lng)

    # Build query string
    #location = "-73.98529171943665,40.75872069597532"
    timesteps = "1d"
    WEATHER_API_KEY = "oMxv2FQh3mL4u4wyRZ0lV4qKC8rTZxCh"
    weather_params = {"location": geo_location,
                      "fields": "temperature,temperatureApparent,temperatureMin,temperatureMax,windSpeed,windDirection,humidity,pressureSeaLevel,uvIndex,weatherCode,precipitationProbability,precipitationType,sunriseTime,sunsetTime,visibility,moonPhase,cloudCover",
                      "timesteps": timesteps,
                      "units": "imperial",
                      "apikey": WEATHER_API_KEY,
                      "timezone": "America/Los_Angeles"
                      }
    querystring = parse.urlencode(weather_params)

    # build tomorrow.io request url
    url = 'https://api.tomorrow.io/v4/timelines?' + querystring

    # Get response
    try:
        weather_resp = urlopen(url)
    except urllib.error.URLError as e:
        print("Bad Request!!")
        return jsonify({"Response", str(e.code)})

    # decode response to json
    data_json = json.loads(weather_resp.read())

    return jsonify(data_json)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
