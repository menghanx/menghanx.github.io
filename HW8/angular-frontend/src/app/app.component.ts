import { Component } from '@angular/core';
import { TomorrowService } from './tomorrow.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = "Weather"


  // TomorrowService talks to NodeJS api to get weather data
  constructor(private tom: TomorrowService) { }

  // loc holds geoLocation
  loc = "0.758,-23.9855";

  // store weather data 
  weather_data: any;
  getWeather() {
    this.tom.getData(this.loc).subscribe(data => {
      this.weather_data = data;
      console.log(data);
    });
  }

}
