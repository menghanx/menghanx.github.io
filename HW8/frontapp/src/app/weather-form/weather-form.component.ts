import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AutocompleteService } from '../autocomplete.service'
import { Observable } from 'rxjs';

import { Query } from '../query';

@Component({
  selector: 'app-weather-form',
  templateUrl: './weather-form.component.html',
  styleUrls: ['./weather-form.component.css']
})
export class WeatherFormComponent implements OnInit {

  constructor(
    private auto: AutocompleteService
  ) { }

  states: any[] = [
    { id: "AL", full: "Alabama" },
    { id: "AK", full: "Alaska" },
    { id: "AZ", full: "Arizona" },
    { id: "AR", full: "Arkansas" },
    { id: "CA", full: "California" },
    { id: "CO", full: "Colorado" },
    { id: "CT", full: "Connecticut" },
    { id: "DE", full: "Delaware" },
    { id: "DC", full: "District Of Columbia" },
    { id: "FL", full: "Florida" },
    { id: "GA", full: "Georgia" },
    { id: "HI", full: "Hawaii" },
    { id: "ID", full: "Idaho" },
    { id: "IL", full: "Illinois" },
    { id: "IN", full: "Indiana" },
    { id: "IA", full: "Iowa" },
    { id: "KS", full: "Kansas" },
    { id: "KY", full: "Kentucky" },
    { id: "LA", full: "Louisiana" },
    { id: "ME", full: "Maine" },
    { id: "MD", full: "Maryland" },
    { id: "MA", full: "Massachusetts" },
    { id: "MI", full: "Michigan" },
    { id: "MN", full: "Minnesota" },
    { id: "MS", full: "Mississippi" },
    { id: "MO", full: "Missouri" },
    { id: "MT", full: "Montana" },
    { id: "NE", full: "Nebraska" },
    { id: "NV", full: "Nevada" },
    { id: "NH", full: "New Hampshire" },
    { id: "NJ", full: "New Jersey" },
    { id: "NM", full: "New Mexico" },
    { id: "NY", full: "New York" },
    { id: "NC", full: "North Carolina" },
    { id: "ND", full: "North Dakota" },
    { id: "OH", full: "Ohio" },
    { id: "OK", full: "Oklahoma" },
    { id: "OR", full: "Oregon" },
    { id: "PA", full: "Pennsylvania" },
    { id: "RI", full: "Rhode Island" },
    { id: "SC", full: "South Carolina" },
    { id: "SD", full: "South Dakota" },
    { id: "TN", full: "Tennessee" },
    { id: "TX", full: "Texas" },
    { id: "UT", full: "Utah" },
    { id: "VT", full: "Vermont" },
    { id: "VA", full: "Virginia" },
    { id: "WA", full: "Washington" },
    { id: "WV", full: "West Virginia" },
    { id: "WI", full: "Wisconsin" },
    { id: "WY", full: "Wyoming" }
  ]
  // dummy data
  options: string[] = ['New York - NY', 'New York - MN', 'New York - TX'];
  filteredOptions: string[] = [];
  minLength = 2;

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
      state: new FormControl('default'),
      autoDetect: new FormControl(false)
    });
    // autocomplete
    this.weatherForm.get('city')?.valueChanges.subscribe(response => {
      // update options here
      console.log('change is ', response);
      // filter the items
      if (response && response.length >= this.minLength) {
        this.filterData(response);
      } else {
        this.filteredOptions = [];
      }
    })
  }

  filterData(enteredData: string) {
    // use service to update options
    this.getAutos(enteredData);
    // filter options and store in filteredOptions
    this.filteredOptions = this.options.filter(item => {
      return item.toLowerCase().indexOf(enteredData.toLowerCase()) > -1
    })
  }

  getAutos(input: string) {
    this.auto.getData(input).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log("error");
      }
    )
  }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.weatherForm.value);
  }

  defualtValues() {
    this.weatherForm.setValue({ street: '', city: '', state: 'default', autoDetect: false })
  }

  disableInput($event: any) {

    if ($event.target.checked) {
      this.weatherForm.controls.street.disable();
      this.weatherForm.controls.city.disable();
      this.weatherForm.controls.state.disable();
      this.weatherForm.controls.street.reset();
      this.weatherForm.controls.city.reset();
      this.weatherForm.controls['state'].setValue('default');

    } else {
      this.weatherForm.controls.street.enable();
      this.weatherForm.controls.city.enable();
      this.weatherForm.controls.state.enable();
    }
  }

  clearForm() {
    this.weatherForm.enable();
    this.weatherForm.reset();
    this.weatherForm.controls['state'].setValue('default');
  }
}
