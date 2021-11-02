import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
// DEBUG TO REMOVE
import * as data from "./data.json";

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {
  // weather data
  weatherData!: any;
  headers = ["#", "Date", "Status", "Temp. High(°F)", "Temp. Low(°F)", "Wind Speed (mph)"];
  mapping: any = {
    "1000": [
      "../../assets/images/clear_day.svg",
      "Clear"
    ],
    "1001": [
      "../../assets/images/cloudy.svg",
      "Cloudy"
    ],
    "1100": [
      "../../assets/images/mostly_clear_day.svg",
      "Mostly Clear"
    ],
    "1101": [
      "../../assets/images/partly_cloudy_day.svg",
      "Partly Cloudy"
    ],
    "1102": [
      "../../assets/images/mostly_cloudy.svg",
      "Mostly Cloudy"
    ],
    "2000": [
      "../../assets/images/fog.svg",
      "Fog"
    ],
    "2100": [
      "../../assets/images/fog_light.svg",
      "Light Fog"
    ],
    "3000": [
      "../../assets/images/light_wind.svg",
      "Light Wind"
    ],
    "3001": [
      "../../assets/images/wind.svg",
      "Wind"
    ],
    "3002": [
      "../../assets/images/strong_wind.svg",
      "Strong Wind"
    ],
    "4000": [
      "../../assets/images/drizzle.svg",
      "Drizzle"
    ],
    "4001": [
      "../../assets/images/rain.svg",
      "Rain"
    ],
    "4200": [
      "../../assets/images/rain_light.svg",
      "Light Rain"
    ],
    "4201": [
      "../../assets/images/rain_heavy.svg",
      "Heavy Rain"
    ],
    "5000": [
      "../../assets/images/snow.svg",
      "Snow"
    ],
    "5001": [
      "../../assets/images/flurries.svg",
      "Flurries"
    ],
    "5100": [
      "../../assets/images/snow_light.svg",
      "Light Snow"
    ],
    "5101": [
      "../../assets/images/snow_heavy.svg",
      "Heavy Snow"
    ],
    "6000": [
      "../../assets/images/freezing_drizzle.svg",
      "Freezing Drizzle"
    ],
    "6001": [
      "../../assets/images/freezing_rain.svg",
      "Freezing Rain"
    ],
    "6200": [
      "../../assets/images/freezing_rain_light.svg",
      "Light Freezing Rain"
    ],
    "6201": [
      "../../assets/images/freezing_rain_heavy.svg",
      "Heavy Freezing Rain"
    ],
    "7000": [
      "../../assets/images/ice_pellets.svg",
      "Ice Pellets"
    ],
    "7101": [
      "../../assets/images/ice_pellets_heavy.svg",
      "Heavy Ice Pellets"
    ],
    "7102": [
      "../../assets/images/ice_pellets_light.svg",
      "Light Ice Pellets"
    ],
    "8000": [
      "../../assets/images/tstorm.svg",
      "Thunderstorm"
    ]
  };


  constructor(
    private dataServ: DataService
  ) { }

  status(input: string) {
    return this.mapping[input][1];
  }

  imagePath(input: string) {
    return this.mapping[input][0];
  }
  getDate(input: string) {
    //2021-10-31T03:00:00-07:00
    return new Date(input);
  }

  ngOnInit(): void {
    // subscribe to the weather json data
    this.dataServ.currentData.subscribe(data => this.weatherData = data);
    // DEBUG TO REMOVE
    this.weatherData = data;

  }

}
