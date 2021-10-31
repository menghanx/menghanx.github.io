import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
// import http
import { HttpClientModule } from '@angular/common/http';
// import forms
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
// import material

import { MatInputModule } from '@angular/material/input'
import { MatAutocompleteModule } from '@angular/material/autocomplete'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WeatherFormComponent } from './weather-form/weather-form.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    WeatherFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    MatInputModule,
    MatAutocompleteModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
