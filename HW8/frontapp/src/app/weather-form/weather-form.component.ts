// Imports
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { Observable } from 'rxjs';
// Custom services
import { AutocompleteService } from '../autocomplete.service'
import { TomorrowService } from '../tomorrow.service';
import { IpinfoService } from '../ipinfo.service';
import { Query } from '../query';

@Component({
  selector: 'app-weather-form',
  templateUrl: './weather-form.component.html',
  styleUrls: ['./weather-form.component.css']
})
export class WeatherFormComponent implements OnInit {

  constructor(
    private auto: AutocompleteService,
    private tom: TomorrowService,
    private ipinfo: IpinfoService,
  ) { }

  states: any[] = [{ id: "AL", full: "Alabama" }, { id: "AK", full: "Alaska" }, { id: "AZ", full: "Arizona" }, { id: "AR", full: "Arkansas" }, { id: "CA", full: "California" }, { id: "CO", full: "Colorado" }, { id: "CT", full: "Connecticut" }, { id: "DE", full: "Delaware" }, { id: "DC", full: "District Of Columbia" }, { id: "FL", full: "Florida" }, { id: "GA", full: "Georgia" }, { id: "HI", full: "Hawaii" }, { id: "ID", full: "Idaho" }, { id: "IL", full: "Illinois" }, { id: "IN", full: "Indiana" }, { id: "IA", full: "Iowa" }, { id: "KS", full: "Kansas" }, { id: "KY", full: "Kentucky" }, { id: "LA", full: "Louisiana" }, { id: "ME", full: "Maine" }, { id: "MD", full: "Maryland" }, { id: "MA", full: "Massachusetts" }, { id: "MI", full: "Michigan" }, { id: "MN", full: "Minnesota" }, { id: "MS", full: "Mississippi" }, { id: "MO", full: "Missouri" }, { id: "MT", full: "Montana" }, { id: "NE", full: "Nebraska" }, { id: "NV", full: "Nevada" }, { id: "NH", full: "New Hampshire" }, { id: "NJ", full: "New Jersey" }, { id: "NM", full: "New Mexico" }, { id: "NY", full: "New York" }, { id: "NC", full: "North Carolina" }, { id: "ND", full: "North Dakota" }, { id: "OH", full: "Ohio" }, { id: "OK", full: "Oklahoma" }, { id: "OR", full: "Oregon" }, { id: "PA", full: "Pennsylvania" }, { id: "RI", full: "Rhode Island" }, { id: "SC", full: "South Carolina" }, { id: "SD", full: "South Dakota" }, { id: "TN", full: "Tennessee" }, { id: "TX", full: "Texas" }, { id: "UT", full: "Utah" }, { id: "VT", full: "Vermont" }, { id: "VA", full: "Virginia" }, { id: "WA", full: "Washington" }, { id: "WV", full: "West Virginia" }, { id: "WI", full: "Wisconsin" }, { id: "WY", full: "Wyoming" }]
  states_id: string[] = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"];
  default_state = "Ca";
  // Autocomplete suggestions stored here
  options: any;
  // minimum length to trigger the suggestion
  minLength = 3;

  // location
  result_address!: string;

  weatherForm!: FormGroup;

  ngOnInit(): void {
    // Initialize form
    this.weatherForm = new FormGroup({
      street: new FormControl('', [
        Validators.required
      ]),
      city: new FormControl('', [
        Validators.required
      ]),
      state: new FormControl(this.default_state),
      autoDetect: new FormControl(false)
    });
    // Enable autocomplete on city input
    this.weatherForm.get('city')?.valueChanges.subscribe(response => {
      // update options here
      // console.log('change is ', response);

      // Only trigger autocomplete when minimun length is met
      if (response && response.length >= this.minLength) {
        this.getAutos(response);
      } else {
        this.options = [];
      }
    })
  }

  // Event handler when autocomplete option is selected
  onSelectionChanged(event: MatAutocompleteSelectedEvent) {
    // console.log(event.option.value);
    this.weatherForm.controls['city'].setValue(event.option.value.city);
    if (this.states_id.indexOf(event.option.value.state) > -1) {
      this.weatherForm.controls['state'].setValue(event.option.value.state);
    }
  }

  // Given a string, get autocomplete suggestions through autocomplete service
  getAutos(input: string) {
    this.auto.getData(input).subscribe(
      data => {
        // console.log(data);
        this.options = data;
      },
      error => {
        console.log("error");
      }
    )
  }

  // Submit the search
  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.weatherForm.value);

    // default dummy geo loc
    let loc = "0.758,-23.9855";

    if (this.weatherForm.value['autoDetect']) {
      console.log("auto detect");
      this.ipinfo.getData().subscribe(
        (data: any) => {
          this.result_address = data["city"] + ", " + data["region"] + ", " + data["country"];
          loc = data["loc"];
          console.log(this.result_address);
          // get weather data using loc
          this.getWeather(loc);
        }
      )
    } else {
      console.log("user input");
    }

  }

  // store weather data 
  getWeather(loc: any) {
    var res: any;
    this.tom.getData(loc).subscribe(
      data => {
        // Use Data Here, call a function or something
        console.log(data);
      });
  }

  // disable input fields when checkbox is checked
  disableInput($event: any) {
    if ($event.target.checked) {
      this.weatherForm.controls.street.disable();
      this.weatherForm.controls.city.disable();
      this.weatherForm.controls.state.disable();
      this.weatherForm.controls.street.reset();
      this.weatherForm.controls.city.reset();
      this.weatherForm.controls['state'].setValue("");
    } else {
      this.weatherForm.controls.street.enable();
      this.weatherForm.controls.city.enable();
      this.weatherForm.controls.state.enable();
      this.weatherForm.controls['state'].setValue(this.default_state);
    }
  }

  // Clear everything
  clearForm() {
    this.weatherForm.enable();
    this.weatherForm.reset();
    this.weatherForm.controls['state'].setValue(this.default_state);
  }
}
