import json
import re
import urllib
from datetime import datetime
from urllib import parse
from urllib.request import urlopen

import jyserver.Flask as jsf
from flask import Flask, jsonify, current_app, request

WEATHER_API_KEY = "oMxv2FQh3mL4u4wyRZ0lV4qKC8rTZxCh"

SAMPLE_JSON = {
    "data": {
        "timelines": [
            {
                "endTime": "2021-10-01T11:25:00-07:00",
                "intervals": [
                    {
                        "startTime": "2021-10-01T11:25:00-07:00",
                        "values": {
                            "cloudCover": 6,
                            "humidity": 79,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.35,
                            "temperature": 56.64,
                            "temperatureApparent": 56.64,
                            "temperatureMax": 56.64,
                            "temperatureMin": 56.64,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 3000,
                            "windDirection": 356.88,
                            "windSpeed": 8.52
                        }
                    }
                ],
                "startTime": "2021-10-01T11:25:00-07:00",
                "timestep": "current"
            },
            {
                "endTime": "2021-10-05T23:00:00-07:00",
                "intervals": [
                    {
                        "startTime": "2021-10-01T11:00:00-07:00",
                        "values": {
                            "cloudCover": 6,
                            "humidity": 80,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.35,
                            "sunriseTime": "2021-10-01T07:08:20-07:00",
                            "sunsetTime": "2021-10-01T18:48:20-07:00",
                            "temperature": 56.53,
                            "temperatureApparent": 56.53,
                            "temperatureMax": 56.53,
                            "temperatureMin": 56.53,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1000,
                            "windDirection": 356.88,
                            "windSpeed": 8.52
                        }
                    },
                    {
                        "startTime": "2021-10-01T12:00:00-07:00",
                        "values": {
                            "cloudCover": 2.34,
                            "humidity": 77.35,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.32,
                            "sunriseTime": "2021-10-01T07:08:20-07:00",
                            "sunsetTime": "2021-10-01T18:48:20-07:00",
                            "temperature": 56.25,
                            "temperatureApparent": 56.25,
                            "temperatureMax": 56.25,
                            "temperatureMin": 56.25,
                            "uvIndex": 2,
                            "visibility": 9.94,
                            "weatherCode": 1000,
                            "windDirection": 352.2,
                            "windSpeed": 8.17
                        }
                    },
                    {
                        "startTime": "2021-10-01T13:00:00-07:00",
                        "values": {
                            "cloudCover": 15.63,
                            "humidity": 82.62,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.32,
                            "sunriseTime": "2021-10-01T07:08:20-07:00",
                            "sunsetTime": "2021-10-01T18:48:20-07:00",
                            "temperature": 56.26,
                            "temperatureApparent": 56.26,
                            "temperatureMax": 56.26,
                            "temperatureMin": 56.26,
                            "uvIndex": 2,
                            "visibility": 9.94,
                            "weatherCode": 1100,
                            "windDirection": 338.14,
                            "windSpeed": 9.33
                        }
                    },
                    {
                        "startTime": "2021-10-01T14:00:00-07:00",
                        "values": {
                            "cloudCover": 3.99,
                            "humidity": 81.12,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.32,
                            "sunriseTime": "2021-10-01T07:08:20-07:00",
                            "sunsetTime": "2021-10-01T18:48:20-07:00",
                            "temperature": 55.94,
                            "temperatureApparent": 55.94,
                            "temperatureMax": 55.94,
                            "temperatureMin": 55.94,
                            "uvIndex": 2,
                            "visibility": 9.94,
                            "weatherCode": 1000,
                            "windDirection": 337.08,
                            "windSpeed": 9.35
                        }
                    },
                    {
                        "startTime": "2021-10-01T15:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 82.03,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.31,
                            "sunriseTime": "2021-10-01T07:08:20-07:00",
                            "sunsetTime": "2021-10-01T18:48:20-07:00",
                            "temperature": 55.63,
                            "temperatureApparent": 55.63,
                            "temperatureMax": 55.63,
                            "temperatureMin": 55.63,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 341.66,
                            "windSpeed": 9.1
                        }
                    },
                    {
                        "startTime": "2021-10-01T16:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 80.97,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.28,
                            "sunriseTime": "2021-10-01T07:08:20-07:00",
                            "sunsetTime": "2021-10-01T18:48:20-07:00",
                            "temperature": 55.49,
                            "temperatureApparent": 55.49,
                            "temperatureMax": 55.49,
                            "temperatureMin": 55.49,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 347.42,
                            "windSpeed": 8.19
                        }
                    },
                    {
                        "startTime": "2021-10-01T17:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 80.22,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.27,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 55.36,
                            "temperatureApparent": 55.36,
                            "temperatureMax": 55.36,
                            "temperatureMin": 55.36,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 349.22,
                            "windSpeed": 6.38
                        }
                    },
                    {
                        "startTime": "2021-10-01T18:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 83.47,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.26,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 54.39,
                            "temperatureApparent": 54.39,
                            "temperatureMax": 54.39,
                            "temperatureMin": 54.39,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 340.65,
                            "windSpeed": 4.7
                        }
                    },
                    {
                        "startTime": "2021-10-01T19:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 88.68,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.25,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 52.88,
                            "temperatureApparent": 52.88,
                            "temperatureMax": 52.88,
                            "temperatureMin": 52.88,
                            "uvIndex": 0,
                            "visibility": 9.26,
                            "weatherCode": 1001,
                            "windDirection": 327.39,
                            "windSpeed": 4.56
                        }
                    },
                    {
                        "startTime": "2021-10-01T20:00:00-07:00",
                        "values": {
                            "cloudCover": 95.84,
                            "humidity": 90.48,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.25,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 51.78,
                            "temperatureApparent": 51.78,
                            "temperatureMax": 51.78,
                            "temperatureMin": 51.78,
                            "uvIndex": 0,
                            "visibility": 8.73,
                            "weatherCode": 1001,
                            "windDirection": 342.88,
                            "windSpeed": 3.51
                        }
                    },
                    {
                        "startTime": "2021-10-01T21:00:00-07:00",
                        "values": {
                            "cloudCover": 71.21,
                            "humidity": 88.96,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.25,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 51.21,
                            "temperatureApparent": 51.21,
                            "temperatureMax": 51.21,
                            "temperatureMin": 51.21,
                            "uvIndex": 0,
                            "visibility": 8.92,
                            "weatherCode": 1102,
                            "windDirection": 3.05,
                            "windSpeed": 4.45
                        }
                    },
                    {
                        "startTime": "2021-10-01T22:00:00-07:00",
                        "values": {
                            "cloudCover": 93.84,
                            "humidity": 86.82,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.25,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 50.74,
                            "temperatureApparent": 50.74,
                            "temperatureMax": 50.74,
                            "temperatureMin": 50.74,
                            "uvIndex": 0,
                            "visibility": 9.38,
                            "weatherCode": 1001,
                            "windDirection": 21.58,
                            "windSpeed": 3.51
                        }
                    },
                    {
                        "startTime": "2021-10-01T23:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 86.25,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.25,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 50.25,
                            "temperatureApparent": 50.25,
                            "temperatureMax": 50.25,
                            "temperatureMin": 50.25,
                            "uvIndex": 0,
                            "visibility": 9.35,
                            "weatherCode": 1001,
                            "windDirection": 12.56,
                            "windSpeed": 4.14
                        }
                    },
                    {
                        "startTime": "2021-10-02T00:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 85.85,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.26,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 49.87,
                            "temperatureApparent": 49.87,
                            "temperatureMax": 49.87,
                            "temperatureMin": 49.87,
                            "uvIndex": 0,
                            "visibility": 9.19,
                            "weatherCode": 1001,
                            "windDirection": 50.52,
                            "windSpeed": 3.47
                        }
                    },
                    {
                        "startTime": "2021-10-02T01:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 87.28,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.25,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 49.48,
                            "temperatureApparent": 49.48,
                            "temperatureMax": 49.48,
                            "temperatureMin": 49.48,
                            "uvIndex": 0,
                            "visibility": 8.66,
                            "weatherCode": 1001,
                            "windDirection": 34.87,
                            "windSpeed": 2.98
                        }
                    },
                    {
                        "startTime": "2021-10-02T02:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 88.94,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.24,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 49.05,
                            "temperatureApparent": 49.05,
                            "temperatureMax": 49.05,
                            "temperatureMin": 49.05,
                            "uvIndex": 0,
                            "visibility": 8.3,
                            "weatherCode": 1001,
                            "windDirection": 20.5,
                            "windSpeed": 1.77
                        }
                    },
                    {
                        "startTime": "2021-10-02T03:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 88.78,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.24,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 48.78,
                            "temperatureApparent": 48.78,
                            "temperatureMax": 48.78,
                            "temperatureMin": 48.78,
                            "uvIndex": 0,
                            "visibility": 8.14,
                            "weatherCode": 1001,
                            "windDirection": 324.91,
                            "windSpeed": 1.34
                        }
                    },
                    {
                        "startTime": "2021-10-02T04:00:00-07:00",
                        "values": {
                            "cloudCover": 93.92,
                            "humidity": 90.99,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.22,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 49.19,
                            "temperatureApparent": 49.19,
                            "temperatureMax": 49.19,
                            "temperatureMin": 49.19,
                            "uvIndex": 0,
                            "visibility": 7.75,
                            "weatherCode": 1001,
                            "windDirection": 337.07,
                            "windSpeed": 4.45
                        }
                    },
                    {
                        "startTime": "2021-10-02T05:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 90.19,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.23,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 48.87,
                            "temperatureApparent": 48.87,
                            "temperatureMax": 48.87,
                            "temperatureMin": 48.87,
                            "uvIndex": 0,
                            "visibility": 8,
                            "weatherCode": 1001,
                            "windDirection": 25.86,
                            "windSpeed": 2.77
                        }
                    },
                    {
                        "startTime": "2021-10-02T06:00:00-07:00",
                        "values": {
                            "cloudCover": 96.88,
                            "humidity": 95.29,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.24,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 50,
                            "temperatureApparent": 50,
                            "temperatureMax": 50,
                            "temperatureMin": 50,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 20.98,
                            "windSpeed": 3.38
                        }
                    },
                    {
                        "startTime": "2021-10-02T07:00:00-07:00",
                        "values": {
                            "cloudCover": 97.66,
                            "humidity": 94.83,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.23,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 50.56,
                            "temperatureApparent": 50.56,
                            "temperatureMax": 50.56,
                            "temperatureMin": 50.56,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 65.78,
                            "windSpeed": 3.33
                        }
                    },
                    {
                        "startTime": "2021-10-02T08:00:00-07:00",
                        "values": {
                            "cloudCover": 89.06,
                            "humidity": 93.71,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.23,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 50.65,
                            "temperatureApparent": 50.65,
                            "temperatureMax": 50.65,
                            "temperatureMin": 50.65,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 82.33,
                            "windSpeed": 2.53
                        }
                    },
                    {
                        "startTime": "2021-10-02T09:00:00-07:00",
                        "values": {
                            "cloudCover": 93.75,
                            "humidity": 91.58,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.22,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 50.86,
                            "temperatureApparent": 50.86,
                            "temperatureMax": 50.86,
                            "temperatureMin": 50.86,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 165.82,
                            "windSpeed": 1.57
                        }
                    },
                    {
                        "startTime": "2021-10-02T10:00:00-07:00",
                        "values": {
                            "cloudCover": 91.41,
                            "humidity": 88.77,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.22,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 51.84,
                            "temperatureApparent": 51.84,
                            "temperatureMax": 51.84,
                            "temperatureMin": 51.84,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 183.77,
                            "windSpeed": 1.36
                        }
                    },
                    {
                        "startTime": "2021-10-02T11:00:00-07:00",
                        "values": {
                            "cloudCover": 51.56,
                            "humidity": 85.35,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.22,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 52.99,
                            "temperatureApparent": 52.99,
                            "temperatureMax": 52.99,
                            "temperatureMin": 52.99,
                            "uvIndex": 2,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 204.82,
                            "windSpeed": 1.83
                        }
                    },
                    {
                        "startTime": "2021-10-02T12:00:00-07:00",
                        "values": {
                            "cloudCover": 80.47,
                            "humidity": 80.4,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.21,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 54.55,
                            "temperatureApparent": 54.55,
                            "temperatureMax": 54.55,
                            "temperatureMin": 54.55,
                            "uvIndex": 3,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 191.97,
                            "windSpeed": 1.23
                        }
                    },
                    {
                        "startTime": "2021-10-02T13:00:00-07:00",
                        "values": {
                            "cloudCover": 75,
                            "humidity": 75.61,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.2,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 56.14,
                            "temperatureApparent": 56.14,
                            "temperatureMax": 56.14,
                            "temperatureMin": 56.14,
                            "uvIndex": 3,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 149.77,
                            "windSpeed": 1.68
                        }
                    },
                    {
                        "startTime": "2021-10-02T14:00:00-07:00",
                        "values": {
                            "cloudCover": 40.63,
                            "humidity": 70.81,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.18,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 57.54,
                            "temperatureApparent": 57.54,
                            "temperatureMax": 57.54,
                            "temperatureMin": 57.54,
                            "uvIndex": 3,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 147.6,
                            "windSpeed": 2.51
                        }
                    },
                    {
                        "startTime": "2021-10-02T15:00:00-07:00",
                        "values": {
                            "cloudCover": 53.13,
                            "humidity": 65.68,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.16,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 59.27,
                            "temperatureApparent": 59.27,
                            "temperatureMax": 59.27,
                            "temperatureMin": 59.27,
                            "uvIndex": 2,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 138.94,
                            "windSpeed": 1.86
                        }
                    },
                    {
                        "startTime": "2021-10-02T16:00:00-07:00",
                        "values": {
                            "cloudCover": 90.63,
                            "humidity": 63.46,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.16,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 60.06,
                            "temperatureApparent": 60.06,
                            "temperatureMax": 60.06,
                            "temperatureMin": 60.06,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 2.97,
                            "windSpeed": 1.9
                        }
                    },
                    {
                        "startTime": "2021-10-02T17:00:00-07:00",
                        "values": {
                            "cloudCover": 35.16,
                            "humidity": 73.27,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.15,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 57.83,
                            "temperatureApparent": 57.83,
                            "temperatureMax": 57.83,
                            "temperatureMin": 57.83,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1100,
                            "windDirection": 3.53,
                            "windSpeed": 6.78
                        }
                    },
                    {
                        "startTime": "2021-10-02T18:00:00-07:00",
                        "values": {
                            "cloudCover": 63.28,
                            "humidity": 76.32,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 56.95,
                            "temperatureApparent": 56.95,
                            "temperatureMax": 56.95,
                            "temperatureMin": 56.95,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1102,
                            "windDirection": 5.23,
                            "windSpeed": 6.71
                        }
                    },
                    {
                        "startTime": "2021-10-02T19:00:00-07:00",
                        "values": {
                            "cloudCover": 23.44,
                            "humidity": 81.84,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 55.58,
                            "temperatureApparent": 55.58,
                            "temperatureMax": 55.58,
                            "temperatureMin": 55.58,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1100,
                            "windDirection": 354.97,
                            "windSpeed": 4.41
                        }
                    },
                    {
                        "startTime": "2021-10-02T20:00:00-07:00",
                        "values": {
                            "cloudCover": 46.09,
                            "humidity": 79.84,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 56.01,
                            "temperatureApparent": 56.01,
                            "temperatureMax": 56.01,
                            "temperatureMin": 56.01,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 10.46,
                            "windSpeed": 2.59
                        }
                    },
                    {
                        "startTime": "2021-10-02T21:00:00-07:00",
                        "values": {
                            "cloudCover": 49.22,
                            "humidity": 73.69,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 57.4,
                            "temperatureApparent": 57.4,
                            "temperatureMax": 57.4,
                            "temperatureMin": 57.4,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 161.99,
                            "windSpeed": 0.98
                        }
                    },
                    {
                        "startTime": "2021-10-02T22:00:00-07:00",
                        "values": {
                            "cloudCover": 91.41,
                            "humidity": 82.69,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 55.54,
                            "temperatureApparent": 55.54,
                            "temperatureMax": 55.54,
                            "temperatureMin": 55.54,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 171.69,
                            "windSpeed": 5.37
                        }
                    },
                    {
                        "startTime": "2021-10-02T23:00:00-07:00",
                        "values": {
                            "cloudCover": 46.88,
                            "humidity": 79.63,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 55.22,
                            "temperatureApparent": 55.22,
                            "temperatureMax": 55.22,
                            "temperatureMin": 55.22,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 176.57,
                            "windSpeed": 8.52
                        }
                    },
                    {
                        "startTime": "2021-10-03T00:00:00-07:00",
                        "values": {
                            "cloudCover": 53.13,
                            "humidity": 82.63,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.13,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.14,
                            "temperatureApparent": 54.14,
                            "temperatureMax": 54.14,
                            "temperatureMin": 54.14,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 171.65,
                            "windSpeed": 9.46
                        }
                    },
                    {
                        "startTime": "2021-10-03T01:00:00-07:00",
                        "values": {
                            "cloudCover": 71.88,
                            "humidity": 81.58,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54,
                            "temperatureApparent": 54,
                            "temperatureMax": 54,
                            "temperatureMin": 54,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1102,
                            "windDirection": 165,
                            "windSpeed": 9.51
                        }
                    },
                    {
                        "startTime": "2021-10-03T02:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 79.51,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.21,
                            "temperatureApparent": 54.21,
                            "temperatureMax": 54.21,
                            "temperatureMin": 54.21,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 159.28,
                            "windSpeed": 9.62
                        }
                    },
                    {
                        "startTime": "2021-10-03T03:00:00-07:00",
                        "values": {
                            "cloudCover": 99.22,
                            "humidity": 79.25,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.12,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.48,
                            "temperatureApparent": 54.48,
                            "temperatureMax": 54.48,
                            "temperatureMin": 54.48,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 161.7,
                            "windSpeed": 11.01
                        }
                    },
                    {
                        "startTime": "2021-10-03T04:00:00-07:00",
                        "values": {
                            "cloudCover": 97.66,
                            "humidity": 80.75,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.12,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.23,
                            "temperatureApparent": 54.23,
                            "temperatureMax": 54.23,
                            "temperatureMin": 54.23,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 166.32,
                            "windSpeed": 10.11
                        }
                    },
                    {
                        "startTime": "2021-10-03T05:00:00-07:00",
                        "values": {
                            "cloudCover": 77.34,
                            "humidity": 82.25,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.13,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.32,
                            "temperatureApparent": 54.32,
                            "temperatureMax": 54.32,
                            "temperatureMin": 54.32,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 176.14,
                            "windSpeed": 7.96
                        }
                    },
                    {
                        "startTime": "2021-10-03T06:00:00-07:00",
                        "values": {
                            "cloudCover": 92.97,
                            "humidity": 85.27,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.3,
                            "temperatureApparent": 54.3,
                            "temperatureMax": 54.3,
                            "temperatureMin": 54.3,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 201.8,
                            "windSpeed": 5.79
                        }
                    },
                    {
                        "startTime": "2021-10-03T07:00:00-07:00",
                        "values": {
                            "cloudCover": 93.75,
                            "humidity": 88.89,
                            "moonPhase": 7,
                            "precipitationProbability": 10,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.15,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.23,
                            "temperatureApparent": 54.23,
                            "temperatureMax": 54.23,
                            "temperatureMin": 54.23,
                            "uvIndex": 0,
                            "visibility": 5.1,
                            "weatherCode": 1001,
                            "windDirection": 234.87,
                            "windSpeed": 3.27
                        }
                    },
                    {
                        "startTime": "2021-10-03T08:00:00-07:00",
                        "values": {
                            "cloudCover": 99.22,
                            "humidity": 89.23,
                            "moonPhase": 7,
                            "precipitationProbability": 10,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.16,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.46,
                            "temperatureApparent": 54.46,
                            "temperatureMax": 54.46,
                            "temperatureMin": 54.46,
                            "uvIndex": 0,
                            "visibility": 4.27,
                            "weatherCode": 1001,
                            "windDirection": 340.06,
                            "windSpeed": 1.88
                        }
                    },
                    {
                        "startTime": "2021-10-03T09:00:00-07:00",
                        "values": {
                            "cloudCover": 85.16,
                            "humidity": 83.08,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.16,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.3,
                            "temperatureApparent": 54.3,
                            "temperatureMax": 54.3,
                            "temperatureMin": 54.3,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 29.16,
                            "windSpeed": 8.57
                        }
                    },
                    {
                        "startTime": "2021-10-03T10:00:00-07:00",
                        "values": {
                            "cloudCover": 95.31,
                            "humidity": 74.37,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.18,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 53.64,
                            "temperatureApparent": 53.64,
                            "temperatureMax": 53.64,
                            "temperatureMin": 53.64,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 27.46,
                            "windSpeed": 9.75
                        }
                    },
                    {
                        "startTime": "2021-10-03T11:00:00-07:00",
                        "values": {
                            "cloudCover": 93.75,
                            "humidity": 69.2,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.19,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 54.46,
                            "temperatureApparent": 54.46,
                            "temperatureMax": 54.46,
                            "temperatureMin": 54.46,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 23.45,
                            "windSpeed": 8.61
                        }
                    },
                    {
                        "startTime": "2021-10-03T12:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 65.14,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.19,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 55.2,
                            "temperatureApparent": 55.2,
                            "temperatureMax": 55.2,
                            "temperatureMin": 55.2,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 13.82,
                            "windSpeed": 9.13
                        }
                    },
                    {
                        "startTime": "2021-10-03T13:00:00-07:00",
                        "values": {
                            "cloudCover": 92.97,
                            "humidity": 63.75,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.18,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 55.56,
                            "temperatureApparent": 55.56,
                            "temperatureMax": 55.56,
                            "temperatureMin": 55.56,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 3.39,
                            "windSpeed": 9.02
                        }
                    },
                    {
                        "startTime": "2021-10-03T14:00:00-07:00",
                        "values": {
                            "cloudCover": 85.16,
                            "humidity": 64.39,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.16,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 56.1,
                            "temperatureApparent": 56.1,
                            "temperatureMax": 56.1,
                            "temperatureMin": 56.1,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 358.38,
                            "windSpeed": 8.57
                        }
                    },
                    {
                        "startTime": "2021-10-03T15:00:00-07:00",
                        "values": {
                            "cloudCover": 82.81,
                            "humidity": 67.32,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.15,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 56.21,
                            "temperatureApparent": 56.21,
                            "temperatureMax": 56.21,
                            "temperatureMin": 56.21,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 0.64,
                            "windSpeed": 7.52
                        }
                    },
                    {
                        "startTime": "2021-10-03T16:00:00-07:00",
                        "values": {
                            "cloudCover": 60.94,
                            "humidity": 69.74,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.14,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 56.32,
                            "temperatureApparent": 56.32,
                            "temperatureMax": 56.32,
                            "temperatureMin": 56.32,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 356.2,
                            "windSpeed": 6.89
                        }
                    },
                    {
                        "startTime": "2021-10-03T17:00:00-07:00",
                        "values": {
                            "cloudCover": 57.03,
                            "humidity": 71.42,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.12,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 56.12,
                            "temperatureApparent": 56.12,
                            "temperatureMax": 56.12,
                            "temperatureMin": 56.12,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 347.32,
                            "windSpeed": 7.4
                        }
                    },
                    {
                        "startTime": "2021-10-03T18:00:00-07:00",
                        "values": {
                            "cloudCover": 53.13,
                            "humidity": 74.64,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.11,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 55.17,
                            "temperatureApparent": 55.17,
                            "temperatureMax": 55.17,
                            "temperatureMin": 55.17,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 347.43,
                            "windSpeed": 7.4
                        }
                    },
                    {
                        "startTime": "2021-10-03T19:00:00-07:00",
                        "values": {
                            "cloudCover": 50.78,
                            "humidity": 77.34,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.11,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 53.92,
                            "temperatureApparent": 53.92,
                            "temperatureMax": 53.92,
                            "temperatureMin": 53.92,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1101,
                            "windDirection": 354.54,
                            "windSpeed": 7.78
                        }
                    },
                    {
                        "startTime": "2021-10-03T20:00:00-07:00",
                        "values": {
                            "cloudCover": 75.78,
                            "humidity": 77.19,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.11,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 53.56,
                            "temperatureApparent": 53.56,
                            "temperatureMax": 53.56,
                            "temperatureMin": 53.56,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 359.82,
                            "windSpeed": 7.27
                        }
                    },
                    {
                        "startTime": "2021-10-03T21:00:00-07:00",
                        "values": {
                            "cloudCover": 67.97,
                            "humidity": 76.52,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.1,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 53.31,
                            "temperatureApparent": 53.31,
                            "temperatureMax": 53.31,
                            "temperatureMin": 53.31,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1102,
                            "windDirection": 1.09,
                            "windSpeed": 6.53
                        }
                    },
                    {
                        "startTime": "2021-10-03T22:00:00-07:00",
                        "values": {
                            "cloudCover": 80.47,
                            "humidity": 77.53,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.1,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 53.04,
                            "temperatureApparent": 53.04,
                            "temperatureMax": 53.04,
                            "temperatureMin": 53.04,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 6.06,
                            "windSpeed": 6.44
                        }
                    },
                    {
                        "startTime": "2021-10-03T23:00:00-07:00",
                        "values": {
                            "cloudCover": 89.06,
                            "humidity": 77.86,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.1,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 52.68,
                            "temperatureApparent": 52.68,
                            "temperatureMax": 52.68,
                            "temperatureMin": 52.68,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 4.49,
                            "windSpeed": 6.2
                        }
                    },
                    {
                        "startTime": "2021-10-04T00:00:00-07:00",
                        "values": {
                            "cloudCover": 90.63,
                            "humidity": 75.51,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.09,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 52.45,
                            "temperatureApparent": 52.45,
                            "temperatureMax": 52.45,
                            "temperatureMin": 52.45,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 3.92,
                            "windSpeed": 6.58
                        }
                    },
                    {
                        "startTime": "2021-10-04T01:00:00-07:00",
                        "values": {
                            "cloudCover": 89.84,
                            "humidity": 77.42,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.08,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 51.76,
                            "temperatureApparent": 51.76,
                            "temperatureMax": 51.76,
                            "temperatureMin": 51.76,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 5.94,
                            "windSpeed": 6.85
                        }
                    },
                    {
                        "startTime": "2021-10-04T02:00:00-07:00",
                        "values": {
                            "cloudCover": 95.31,
                            "humidity": 80.36,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.07,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 51.42,
                            "temperatureApparent": 51.42,
                            "temperatureMax": 51.42,
                            "temperatureMin": 51.42,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 7.49,
                            "windSpeed": 6.33
                        }
                    },
                    {
                        "startTime": "2021-10-04T03:00:00-07:00",
                        "values": {
                            "cloudCover": 93.75,
                            "humidity": 79.99,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.06,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 51.42,
                            "temperatureApparent": 51.42,
                            "temperatureMax": 51.42,
                            "temperatureMin": 51.42,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 8.45,
                            "windSpeed": 6.17
                        }
                    },
                    {
                        "startTime": "2021-10-04T04:00:00-07:00",
                        "values": {
                            "cloudCover": 89.06,
                            "humidity": 80.79,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.05,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 51.01,
                            "temperatureApparent": 51.01,
                            "temperatureMax": 51.01,
                            "temperatureMin": 51.01,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 13.86,
                            "windSpeed": 5.59
                        }
                    },
                    {
                        "startTime": "2021-10-04T05:00:00-07:00",
                        "values": {
                            "cloudCover": 92.97,
                            "humidity": 81.01,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.05,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 50.85,
                            "temperatureApparent": 50.85,
                            "temperatureMax": 50.85,
                            "temperatureMin": 50.85,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 15.63,
                            "windSpeed": 5.37
                        }
                    },
                    {
                        "startTime": "2021-10-04T06:00:00-07:00",
                        "values": {
                            "cloudCover": 88.28,
                            "humidity": 82.98,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.05,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 50.22,
                            "temperatureApparent": 50.22,
                            "temperatureMax": 50.22,
                            "temperatureMin": 50.22,
                            "uvIndex": 0,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 16.86,
                            "windSpeed": 5.12
                        }
                    },
                    {
                        "startTime": "2021-10-04T07:00:00-07:00",
                        "values": {
                            "cloudCover": 87.11,
                            "humidity": 81.74,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.04,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 50.27,
                            "temperatureApparent": 50.27,
                            "temperatureMax": 50.27,
                            "temperatureMin": 50.27,
                            "uvIndex": 0,
                            "visibility": 10.37,
                            "weatherCode": 1001,
                            "windDirection": 21.8,
                            "windSpeed": 5.15
                        }
                    },
                    {
                        "startTime": "2021-10-04T08:00:00-07:00",
                        "values": {
                            "cloudCover": 88.93,
                            "humidity": 80.88,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.04,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 50.34,
                            "temperatureApparent": 50.34,
                            "temperatureMax": 50.34,
                            "temperatureMin": 50.34,
                            "uvIndex": 0,
                            "visibility": 10.79,
                            "weatherCode": 1001,
                            "windDirection": 20.59,
                            "windSpeed": 4.97
                        }
                    },
                    {
                        "startTime": "2021-10-04T09:00:00-07:00",
                        "values": {
                            "cloudCover": 92.97,
                            "humidity": 78.81,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.03,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 51.03,
                            "temperatureApparent": 51.03,
                            "temperatureMax": 51.03,
                            "temperatureMin": 51.03,
                            "uvIndex": 0,
                            "visibility": 11.21,
                            "weatherCode": 1001,
                            "windDirection": 19.28,
                            "windSpeed": 4.72
                        }
                    },
                    {
                        "startTime": "2021-10-04T10:00:00-07:00",
                        "values": {
                            "cloudCover": 94.79,
                            "humidity": 73.74,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.02,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 52.7,
                            "temperatureApparent": 52.7,
                            "temperatureMax": 52.7,
                            "temperatureMin": 52.7,
                            "uvIndex": 0,
                            "visibility": 11.63,
                            "weatherCode": 1001,
                            "windDirection": 8.07,
                            "windSpeed": 4.41
                        }
                    },
                    {
                        "startTime": "2021-10-04T11:00:00-07:00",
                        "values": {
                            "cloudCover": 94.08,
                            "humidity": 68.67,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.01,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 54.77,
                            "temperatureApparent": 54.77,
                            "temperatureMax": 54.77,
                            "temperatureMin": 54.77,
                            "uvIndex": 1,
                            "visibility": 12.05,
                            "weatherCode": 1001,
                            "windDirection": 212.4,
                            "windSpeed": 4.25
                        }
                    },
                    {
                        "startTime": "2021-10-04T12:00:00-07:00",
                        "values": {
                            "cloudCover": 92.97,
                            "humidity": 64.73,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.99,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 56.95,
                            "temperatureApparent": 56.95,
                            "temperatureMax": 56.95,
                            "temperatureMin": 56.95,
                            "uvIndex": 1,
                            "visibility": 12.47,
                            "weatherCode": 1001,
                            "windDirection": 183.57,
                            "windSpeed": 4.34
                        }
                    },
                    {
                        "startTime": "2021-10-04T13:00:00-07:00",
                        "values": {
                            "cloudCover": 91.21,
                            "humidity": 61.58,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.98,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 58.89,
                            "temperatureApparent": 58.89,
                            "temperatureMax": 58.89,
                            "temperatureMin": 58.89,
                            "uvIndex": 1,
                            "visibility": 12.9,
                            "weatherCode": 1001,
                            "windDirection": 158.71,
                            "windSpeed": 3.47
                        }
                    },
                    {
                        "startTime": "2021-10-04T14:00:00-07:00",
                        "values": {
                            "cloudCover": 89.58,
                            "humidity": 58.94,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.96,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 60.39,
                            "temperatureApparent": 60.39,
                            "temperatureMax": 60.39,
                            "temperatureMin": 60.39,
                            "uvIndex": 1,
                            "visibility": 13.31,
                            "weatherCode": 1001,
                            "windDirection": 227.31,
                            "windSpeed": 3.18
                        }
                    },
                    {
                        "startTime": "2021-10-04T15:00:00-07:00",
                        "values": {
                            "cloudCover": 97.85,
                            "humidity": 56.72,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.94,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 61.45,
                            "temperatureApparent": 61.45,
                            "temperatureMax": 61.45,
                            "temperatureMin": 61.45,
                            "uvIndex": 1,
                            "visibility": 13.74,
                            "weatherCode": 1001,
                            "windDirection": 229.72,
                            "windSpeed": 2.93
                        }
                    },
                    {
                        "startTime": "2021-10-04T16:00:00-07:00",
                        "values": {
                            "cloudCover": 99.61,
                            "humidity": 55.83,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.92,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 61.47,
                            "temperatureApparent": 61.47,
                            "temperatureMax": 61.47,
                            "temperatureMin": 61.47,
                            "uvIndex": 0,
                            "visibility": 14.16,
                            "weatherCode": 1001,
                            "windDirection": 96.57,
                            "windSpeed": 3
                        }
                    },
                    {
                        "startTime": "2021-10-04T17:00:00-07:00",
                        "values": {
                            "cloudCover": 99.87,
                            "humidity": 57.5,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.9,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 60.67,
                            "temperatureApparent": 60.67,
                            "temperatureMax": 60.67,
                            "temperatureMin": 60.67,
                            "uvIndex": 0,
                            "visibility": 14.58,
                            "weatherCode": 1001,
                            "windDirection": 29.73,
                            "windSpeed": 3.44
                        }
                    },
                    {
                        "startTime": "2021-10-04T18:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 66.21,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.89,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 57.06,
                            "temperatureApparent": 57.06,
                            "temperatureMax": 57.06,
                            "temperatureMin": 57.06,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 159.07,
                            "windSpeed": 3.78
                        }
                    },
                    {
                        "startTime": "2021-10-04T19:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 74.08,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.88,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 52.74,
                            "temperatureApparent": 52.74,
                            "temperatureMax": 52.74,
                            "temperatureMin": 52.74,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 293.25,
                            "windSpeed": 4.05
                        }
                    },
                    {
                        "startTime": "2021-10-04T20:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 76.03,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.87,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 51.39,
                            "temperatureApparent": 51.39,
                            "temperatureMax": 51.39,
                            "temperatureMin": 51.39,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 170.18,
                            "windSpeed": 3.8
                        }
                    },
                    {
                        "startTime": "2021-10-04T21:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 78.17,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.86,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 50.23,
                            "temperatureApparent": 50.23,
                            "temperatureMax": 50.23,
                            "temperatureMin": 50.23,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 349.65,
                            "windSpeed": 3.8
                        }
                    },
                    {
                        "startTime": "2021-10-04T22:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 78.93,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.86,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 49.5,
                            "temperatureApparent": 49.5,
                            "temperatureMax": 49.5,
                            "temperatureMin": 49.5,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 347.59,
                            "windSpeed": 3.76
                        }
                    },
                    {
                        "startTime": "2021-10-04T23:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 78.8,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.85,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 49.01,
                            "temperatureApparent": 49.01,
                            "temperatureMax": 49.01,
                            "temperatureMin": 49.01,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 349.84,
                            "windSpeed": 3.56
                        }
                    },
                    {
                        "startTime": "2021-10-05T00:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 70.17,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.79,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 51.75,
                            "temperatureApparent": 51.75,
                            "temperatureMax": 51.75,
                            "temperatureMin": 51.75,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 74.32,
                            "windSpeed": 0.98
                        }
                    },
                    {
                        "startTime": "2021-10-05T01:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 71.6,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.77,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 51.84,
                            "temperatureApparent": 51.84,
                            "temperatureMax": 51.84,
                            "temperatureMin": 51.84,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 158.36,
                            "windSpeed": 1.79
                        }
                    },
                    {
                        "startTime": "2021-10-05T02:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 71.05,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.76,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 53.02,
                            "temperatureApparent": 53.02,
                            "temperatureMax": 53.02,
                            "temperatureMin": 53.02,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 163.66,
                            "windSpeed": 2.59
                        }
                    },
                    {
                        "startTime": "2021-10-05T03:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 72.99,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.75,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 53.46,
                            "temperatureApparent": 53.46,
                            "temperatureMax": 53.46,
                            "temperatureMin": 53.46,
                            "uvIndex": 0,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 176.52,
                            "windSpeed": 3.4
                        }
                    },
                    {
                        "startTime": "2021-10-05T04:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 78,
                            "moonPhase": 7,
                            "precipitationProbability": 30,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.74,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 53.15,
                            "temperatureApparent": 53.15,
                            "temperatureMax": 53.15,
                            "temperatureMin": 53.15,
                            "uvIndex": 0,
                            "visibility": 13.97,
                            "weatherCode": 4000,
                            "windDirection": 177.48,
                            "windSpeed": 3.78
                        }
                    },
                    {
                        "startTime": "2021-10-05T05:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 86.55,
                            "moonPhase": 7,
                            "precipitationProbability": 40,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.73,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 52.5,
                            "temperatureApparent": 52.5,
                            "temperatureMax": 52.5,
                            "temperatureMin": 52.5,
                            "uvIndex": 0,
                            "visibility": 9.36,
                            "weatherCode": 4000,
                            "windDirection": 170.06,
                            "windSpeed": 4.99
                        }
                    },
                    {
                        "startTime": "2021-10-05T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 93.53,
                            "moonPhase": 7,
                            "precipitationProbability": 50,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.72,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 52.74,
                            "temperatureApparent": 52.74,
                            "temperatureMax": 52.74,
                            "temperatureMin": 52.74,
                            "uvIndex": 0,
                            "visibility": 4.42,
                            "weatherCode": 4200,
                            "windDirection": 170.6,
                            "windSpeed": 6.96
                        }
                    },
                    {
                        "startTime": "2021-10-05T07:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 93.91,
                            "moonPhase": 7,
                            "precipitationProbability": 60,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.73,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 53.4,
                            "temperatureApparent": 53.4,
                            "temperatureMax": 53.4,
                            "temperatureMin": 53.4,
                            "uvIndex": 0,
                            "visibility": 3.87,
                            "weatherCode": 4200,
                            "windDirection": 187.73,
                            "windSpeed": 8.46
                        }
                    },
                    {
                        "startTime": "2021-10-05T08:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 91.54,
                            "moonPhase": 7,
                            "precipitationProbability": 65,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.74,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 53.98,
                            "temperatureApparent": 53.98,
                            "temperatureMax": 53.98,
                            "temperatureMin": 53.98,
                            "uvIndex": 0,
                            "visibility": 4.51,
                            "weatherCode": 4200,
                            "windDirection": 184.88,
                            "windSpeed": 13.18
                        }
                    },
                    {
                        "startTime": "2021-10-05T09:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 87.48,
                            "moonPhase": 7,
                            "precipitationProbability": 70,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.78,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 53.28,
                            "temperatureApparent": 53.28,
                            "temperatureMax": 53.28,
                            "temperatureMin": 53.28,
                            "uvIndex": 0,
                            "visibility": 13.34,
                            "weatherCode": 4200,
                            "windDirection": 205.57,
                            "windSpeed": 13.22
                        }
                    },
                    {
                        "startTime": "2021-10-05T10:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 88.63,
                            "moonPhase": 7,
                            "precipitationProbability": 70,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.82,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 52.2,
                            "temperatureApparent": 52.2,
                            "temperatureMax": 52.2,
                            "temperatureMin": 52.2,
                            "uvIndex": 0,
                            "visibility": 14.98,
                            "weatherCode": 4200,
                            "windDirection": 190.25,
                            "windSpeed": 11.9
                        }
                    },
                    {
                        "startTime": "2021-10-05T11:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 89.13,
                            "moonPhase": 7,
                            "precipitationProbability": 70,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.85,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 52.52,
                            "temperatureApparent": 52.52,
                            "temperatureMax": 52.52,
                            "temperatureMin": 52.52,
                            "uvIndex": 1,
                            "visibility": 14.62,
                            "weatherCode": 4200,
                            "windDirection": 199.35,
                            "windSpeed": 11.36
                        }
                    },
                    {
                        "startTime": "2021-10-05T12:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 76.71,
                            "moonPhase": 7,
                            "precipitationProbability": 55,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.88,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 56.23,
                            "temperatureApparent": 56.23,
                            "temperatureMax": 56.23,
                            "temperatureMin": 56.23,
                            "uvIndex": 1,
                            "visibility": 14.84,
                            "weatherCode": 4000,
                            "windDirection": 204.65,
                            "windSpeed": 12.1
                        }
                    },
                    {
                        "startTime": "2021-10-05T13:00:00-07:00",
                        "values": {
                            "cloudCover": 79.59,
                            "humidity": 65.86,
                            "moonPhase": 7,
                            "precipitationProbability": 60,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.9,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 57.87,
                            "temperatureApparent": 57.87,
                            "temperatureMax": 57.87,
                            "temperatureMin": 57.87,
                            "uvIndex": 1,
                            "visibility": 12.32,
                            "weatherCode": 4000,
                            "windDirection": 208.11,
                            "windSpeed": 13.74
                        }
                    },
                    {
                        "startTime": "2021-10-05T14:00:00-07:00",
                        "values": {
                            "cloudCover": 56.07,
                            "humidity": 60.92,
                            "moonPhase": 7,
                            "precipitationProbability": 60,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.9,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 58.42,
                            "temperatureApparent": 58.42,
                            "temperatureMax": 58.42,
                            "temperatureMin": 58.42,
                            "uvIndex": 1,
                            "visibility": 12.72,
                            "weatherCode": 4000,
                            "windDirection": 211.71,
                            "windSpeed": 13.98
                        }
                    },
                    {
                        "startTime": "2021-10-05T15:00:00-07:00",
                        "values": {
                            "cloudCover": 44.08,
                            "humidity": 60.06,
                            "moonPhase": 7,
                            "precipitationProbability": 60,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.92,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 58.48,
                            "temperatureApparent": 58.48,
                            "temperatureMax": 58.48,
                            "temperatureMin": 58.48,
                            "uvIndex": 1,
                            "visibility": 13.19,
                            "weatherCode": 4000,
                            "windDirection": 215.64,
                            "windSpeed": 13.31
                        }
                    },
                    {
                        "startTime": "2021-10-05T16:00:00-07:00",
                        "values": {
                            "cloudCover": 37.93,
                            "humidity": 60.84,
                            "moonPhase": 7,
                            "precipitationProbability": 60,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.93,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 57.88,
                            "temperatureApparent": 57.88,
                            "temperatureMax": 57.88,
                            "temperatureMin": 57.88,
                            "uvIndex": 0,
                            "visibility": 13.95,
                            "weatherCode": 4000,
                            "windDirection": 216.55,
                            "windSpeed": 12.35
                        }
                    },
                    {
                        "startTime": "2021-10-05T17:00:00-07:00",
                        "values": {
                            "cloudCover": 33.02,
                            "humidity": 63.35,
                            "moonPhase": 7,
                            "precipitationProbability": 60,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.94,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 56.53,
                            "temperatureApparent": 56.53,
                            "temperatureMax": 56.53,
                            "temperatureMin": 56.53,
                            "uvIndex": 0,
                            "visibility": 14.36,
                            "weatherCode": 4000,
                            "windDirection": 217.24,
                            "windSpeed": 11.21
                        }
                    },
                    {
                        "startTime": "2021-10-05T18:00:00-07:00",
                        "values": {
                            "cloudCover": 12.52,
                            "humidity": 67.7,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.96,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 54.12,
                            "temperatureApparent": 54.12,
                            "temperatureMax": 54.12,
                            "temperatureMin": 54.12,
                            "visibility": 14.97,
                            "weatherCode": 1100,
                            "windDirection": 213.33,
                            "windSpeed": 10.72
                        }
                    },
                    {
                        "startTime": "2021-10-05T19:00:00-07:00",
                        "values": {
                            "cloudCover": 9.35,
                            "humidity": 73.47,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.98,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 51.85,
                            "temperatureApparent": 51.85,
                            "temperatureMax": 51.85,
                            "temperatureMin": 51.85,
                            "visibility": 15,
                            "weatherCode": 1000,
                            "windDirection": 205.14,
                            "windSpeed": 9.91
                        }
                    },
                    {
                        "startTime": "2021-10-05T20:00:00-07:00",
                        "values": {
                            "cloudCover": 8.31,
                            "humidity": 76.86,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.01,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 50.74,
                            "temperatureApparent": 50.74,
                            "temperatureMax": 50.74,
                            "temperatureMin": 50.74,
                            "visibility": 15,
                            "weatherCode": 1000,
                            "windDirection": 200.1,
                            "windSpeed": 9.24
                        }
                    },
                    {
                        "startTime": "2021-10-05T21:00:00-07:00",
                        "values": {
                            "cloudCover": 7.63,
                            "humidity": 80.04,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.03,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 49.64,
                            "temperatureApparent": 49.64,
                            "temperatureMax": 49.64,
                            "temperatureMin": 49.64,
                            "visibility": 15,
                            "weatherCode": 1000,
                            "windDirection": 183.9,
                            "windSpeed": 6.93
                        }
                    },
                    {
                        "startTime": "2021-10-05T22:00:00-07:00",
                        "values": {
                            "cloudCover": 7.16,
                            "humidity": 79.39,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.04,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 49.17,
                            "temperatureApparent": 49.17,
                            "temperatureMax": 49.17,
                            "temperatureMin": 49.17,
                            "visibility": 15,
                            "weatherCode": 1000,
                            "windDirection": 180.68,
                            "windSpeed": 7.07
                        }
                    },
                    {
                        "startTime": "2021-10-05T23:00:00-07:00",
                        "values": {
                            "cloudCover": 16.94,
                            "humidity": 79.62,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.05,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 49.37,
                            "temperatureApparent": 49.37,
                            "temperatureMax": 49.37,
                            "temperatureMin": 49.37,
                            "visibility": 15,
                            "weatherCode": 1100,
                            "windDirection": 189.3,
                            "windSpeed": 7.16
                        }
                    }
                ],
                "startTime": "2021-10-01T11:00:00-07:00",
                "timestep": "1h"
            },
            {
                "endTime": "2021-10-15T06:00:00-07:00",
                "intervals": [
                    {
                        "startTime": "2021-10-01T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 95,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 30.22,
                            "sunriseTime": "2021-10-01T07:08:20-07:00",
                            "sunsetTime": "2021-10-01T18:48:20-07:00",
                            "temperature": 56.53,
                            "temperatureApparent": 56.53,
                            "temperatureMax": 56.53,
                            "temperatureMin": 48.78,
                            "uvIndex": 2,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 203.22,
                            "windSpeed": 9.35
                        }
                    },
                    {
                        "startTime": "2021-10-02T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 94.83,
                            "moonPhase": 7,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.12,
                            "sunriseTime": "2021-10-02T07:08:20-07:00",
                            "sunsetTime": "2021-10-02T18:46:40-07:00",
                            "temperature": 60.06,
                            "temperatureApparent": 60.06,
                            "temperatureMax": 60.06,
                            "temperatureMin": 50.56,
                            "uvIndex": 3,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 139.93,
                            "windSpeed": 11.01
                        }
                    },
                    {
                        "startTime": "2021-10-03T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 89.23,
                            "moonPhase": 7,
                            "precipitationProbability": 10,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.05,
                            "sunriseTime": "2021-10-03T07:11:40-07:00",
                            "sunsetTime": "2021-10-03T18:45:00-07:00",
                            "temperature": 56.32,
                            "temperatureApparent": 56.32,
                            "temperatureMax": 56.32,
                            "temperatureMin": 50.85,
                            "uvIndex": 1,
                            "visibility": 9.94,
                            "weatherCode": 1001,
                            "windDirection": 124.5,
                            "windSpeed": 9.75
                        }
                    },
                    {
                        "startTime": "2021-10-04T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 86.55,
                            "moonPhase": 7,
                            "precipitationProbability": 40,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.73,
                            "sunriseTime": "2021-10-04T07:13:20-07:00",
                            "sunsetTime": "2021-10-04T18:41:40-07:00",
                            "temperature": 61.47,
                            "temperatureApparent": 61.47,
                            "temperatureMax": 61.47,
                            "temperatureMin": 49.01,
                            "uvIndex": 1,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 165.12,
                            "windSpeed": 5.15
                        }
                    },
                    {
                        "startTime": "2021-10-05T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 93.91,
                            "moonPhase": 7,
                            "precipitationProbability": 70,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.73,
                            "sunriseTime": "2021-10-05T07:13:20-07:00",
                            "sunsetTime": "2021-10-05T18:40:00-07:00",
                            "temperature": 58.48,
                            "temperatureApparent": 58.48,
                            "temperatureMax": 58.48,
                            "temperatureMin": 46.65,
                            "uvIndex": 1,
                            "visibility": 15,
                            "weatherCode": 4200,
                            "windDirection": 206.04,
                            "windSpeed": 13.98
                        }
                    },
                    {
                        "startTime": "2021-10-06T06:00:00-07:00",
                        "values": {
                            "cloudCover": 99.7,
                            "humidity": 89.76,
                            "moonPhase": 0,
                            "precipitationProbability": 5,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.16,
                            "sunriseTime": "2021-10-06T07:15:00-07:00",
                            "sunsetTime": "2021-10-06T18:38:20-07:00",
                            "temperature": 55.72,
                            "temperatureApparent": 55.72,
                            "temperatureMax": 55.72,
                            "temperatureMin": 40.42,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 97.64,
                            "windSpeed": 6.87
                        }
                    },
                    {
                        "startTime": "2021-10-07T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 87.84,
                            "moonPhase": 0,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.92,
                            "sunriseTime": "2021-10-07T07:18:20-07:00",
                            "sunsetTime": "2021-10-07T18:36:40-07:00",
                            "temperature": 57.4,
                            "temperatureApparent": 57.4,
                            "temperatureMax": 57.4,
                            "temperatureMin": 40.3,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 138.51,
                            "windSpeed": 5.01
                        }
                    },
                    {
                        "startTime": "2021-10-08T06:00:00-07:00",
                        "values": {
                            "cloudCover": 96.48,
                            "humidity": 75.15,
                            "moonPhase": 1,
                            "precipitationProbability": 0,
                            "precipitationType": 0,
                            "pressureSeaLevel": 29.9,
                            "sunriseTime": "2021-10-08T07:18:20-07:00",
                            "sunsetTime": "2021-10-08T18:33:20-07:00",
                            "temperature": 60.66,
                            "temperatureApparent": 60.66,
                            "temperatureMax": 60.66,
                            "temperatureMin": 41.79,
                            "visibility": 15,
                            "weatherCode": 1000,
                            "windDirection": 179.59,
                            "windSpeed": 5.06
                        }
                    },
                    {
                        "startTime": "2021-10-09T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 88.66,
                            "moonPhase": 1,
                            "precipitationProbability": 55,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.92,
                            "sunriseTime": "2021-10-09T07:20:00-07:00",
                            "sunsetTime": "2021-10-09T18:31:40-07:00",
                            "temperature": 60.3,
                            "temperatureApparent": 60.3,
                            "temperatureMax": 60.3,
                            "temperatureMin": 42.4,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 188.54,
                            "windSpeed": 12.24
                        }
                    },
                    {
                        "startTime": "2021-10-10T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 92.81,
                            "moonPhase": 1,
                            "precipitationProbability": 60,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.85,
                            "sunriseTime": "2021-10-10T07:21:40-07:00",
                            "sunsetTime": "2021-10-10T18:31:40-07:00",
                            "temperature": 58.69,
                            "temperatureApparent": 58.69,
                            "temperatureMax": 58.69,
                            "temperatureMin": 43.05,
                            "visibility": 15,
                            "weatherCode": 4000,
                            "windDirection": 193.95,
                            "windSpeed": 10.58
                        }
                    },
                    {
                        "startTime": "2021-10-11T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 96.32,
                            "moonPhase": 2,
                            "precipitationProbability": 30,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.87,
                            "sunriseTime": "2021-10-11T07:21:40-07:00",
                            "sunsetTime": "2021-10-11T18:30:00-07:00",
                            "temperature": 55.06,
                            "temperatureApparent": 55.06,
                            "temperatureMax": 55.06,
                            "temperatureMin": 40.28,
                            "visibility": 15,
                            "weatherCode": 4000,
                            "windDirection": 124.16,
                            "windSpeed": 6.24
                        }
                    },
                    {
                        "startTime": "2021-10-12T06:00:00-07:00",
                        "values": {
                            "cloudCover": 97.18,
                            "humidity": 89.13,
                            "moonPhase": 2,
                            "precipitationProbability": 0,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.93,
                            "sunriseTime": "2021-10-12T07:23:20-07:00",
                            "sunsetTime": "2021-10-12T18:26:40-07:00",
                            "temperature": 52.99,
                            "temperatureApparent": 52.99,
                            "temperatureMax": 52.99,
                            "temperatureMin": 39.04,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 142.61,
                            "windSpeed": 7.05
                        }
                    },
                    {
                        "startTime": "2021-10-13T06:00:00-07:00",
                        "values": {
                            "cloudCover": 90.36,
                            "humidity": 90.46,
                            "moonPhase": 2,
                            "precipitationProbability": 5,
                            "precipitationType": 1,
                            "pressureSeaLevel": 30.08,
                            "sunriseTime": "2021-10-13T07:26:40-07:00",
                            "sunsetTime": "2021-10-13T18:25:00-07:00",
                            "temperature": 55.89,
                            "temperatureApparent": 55.89,
                            "temperatureMax": 55.89,
                            "temperatureMin": 38.66,
                            "visibility": 15,
                            "weatherCode": 1001,
                            "windDirection": 179.22,
                            "windSpeed": 6.78
                        }
                    },
                    {
                        "startTime": "2021-10-14T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 95.73,
                            "moonPhase": 3,
                            "precipitationProbability": 80,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.8,
                            "sunriseTime": "2021-10-14T07:26:40-07:00",
                            "sunsetTime": "2021-10-14T18:23:20-07:00",
                            "temperature": 48.18,
                            "temperatureApparent": 48.18,
                            "temperatureMax": 48.18,
                            "temperatureMin": 44.1,
                            "visibility": 15,
                            "weatherCode": 4000,
                            "windDirection": 166.21,
                            "windSpeed": 11.41
                        }
                    },
                    {
                        "startTime": "2021-10-15T06:00:00-07:00",
                        "values": {
                            "cloudCover": 100,
                            "humidity": 94.55,
                            "moonPhase": 3,
                            "precipitationProbability": 75,
                            "precipitationType": 1,
                            "pressureSeaLevel": 29.7,
                            "sunriseTime": "2021-10-15T07:28:20-07:00",
                            "sunsetTime": "2021-10-15T18:21:40-07:00",
                            "temperature": 49.23,
                            "temperatureApparent": 49.23,
                            "temperatureMax": 49.23,
                            "temperatureMin": 47.75,
                            "visibility": 15,
                            "weatherCode": 4200,
                            "windDirection": 166.48,
                            "windSpeed": 6.71
                        }
                    }
                ],
                "startTime": "2021-10-01T06:00:00-07:00",
                "timestep": "1d"
            }
        ]
    },
    "warnings": [
        {
            "code": 246009,
            "message": "The timestep is not supported in full for the time range requested.",
            "meta": {
                "from": "now",
                "timestep": "current",
                "to": "+1m"
            },
            "type": "Missing Time Range"
        },
        {
            "code": 246009,
            "message": "The timestep is not supported in full for the time range requested.",
            "meta": {
                "from": "-6h",
                "timestep": "1h",
                "to": "+336h"
            },
            "type": "Missing Time Range"
        },
        {
            "code": 246001,
            "message": "The following field is not supported for a time range: 'uvIndex'",
            "meta": {
                "field": "uvIndex",
                "from": "2021-10-01T04:30:00-07:00",
                "to": "2021-10-05T23:25:53-07:00"
            },
            "type": "Time Bounded Field"
        },
        {
            "code": 246008,
            "message": "The following field is not supported for the requested timestep: 'sunriseTime'",
            "meta": {
                "field": "sunriseTime",
                "timesteps": [
                    "current",
                    "1h"
                ]
            },
            "type": "Timestep Bounded Field"
        },
        {
            "code": 246008,
            "message": "The following field is not supported for the requested timestep: 'sunsetTime'",
            "meta": {
                "field": "sunsetTime",
                "timesteps": [
                    "current",
                    "1h"
                ]
            },
            "type": "Timestep Bounded Field"
        },
        {
            "code": 246008,
            "message": "The following field is not supported for the requested timestep: 'moonPhase'",
            "meta": {
                "field": "moonPhase",
                "timesteps": [
                    "current",
                    "1h"
                ]
            },
            "type": "Timestep Bounded Field"
        }
    ]
}

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
    # else return an error message
    else:
        return jsonify({"Response": "Invailid request, expected params: lat,lng"})

    # Build query string
    debug_mode = True
    if debug_mode:
        data_json = SAMPLE_JSON
    else:
        # build tomorrow.io request url
        # Bundle 3 timesteps together and get results in one json
        weather_params = {
            "location": geo_location,
            "fields": "temperature,temperatureApparent,temperatureMin,temperatureMax,windSpeed,windDirection,humidity,pressureSeaLevel,uvIndex,weatherCode,precipitationProbability,precipitationType,sunriseTime,sunsetTime,visibility,moonPhase,cloudCover",
            "timesteps": "current,1h,1d",
            "units": "imperial",
            "apikey": WEATHER_API_KEY,
            "timezone": "America/Los_Angeles"
        }
        url = 'https://api.tomorrow.io/v4/timelines?' + \
            parse.urlencode(weather_params)
        # Get responsea
        print(url)
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
