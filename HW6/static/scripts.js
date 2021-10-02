var result_address = "-";
var GEO_API_KEY = "AIzaSyCLJBmNPC4h2bQlqiUl17X0m0hzYMgKzAs"
var icon_mapping =
{
    "1000": ["/static/Images/clear_day.svg", "Clear"],
    "1001": ["/static/Images/cloudy.svg", "Cloudy"],
    "1100": ["/static/Images/mostly_clear_day.svg", "Mostly Clear"],
    "1101": ["/static/Images/partly_cloudy_day.svg", "Partly Cloudy"],
    "1102": ["/static/Images/mostly_cloudy.svg", "Mostly Cloudy"],
    "2000": ["/static/Images/fog.svg", "Fog"],
    "2100": ["/static/Images/fog_light.svg", "Light Fog"],
    "3000": ["https://www.clipartmax.com/png/middle/31-318730_cold-wind-blowing-vectorwind-blow-icon.png", "Light Wind"],
    "3001": ["https://www.clipartmax.com/png/middle/31-319198_winds-weather-symbol-vectorweather-symbol-for-wind.png", "Wind"],
    "3002": ["https://www.clipartmax.com/png/middle/2-27821_wind-clipart-forecast-icon-line-icon-weather-wind-windy-wind-clipart.png", "Strong Wind"],
    "4000": ["/static/Images/drizzle.svg", "Drizzle"],
    "4001": ["/static/Images/rain.svg", "Rain"],
    "4200": ["/static/Images/rain_light.svg", "Light Rain"],
    "4201": ["/static/Images/rain_heavy.svg", "Heavy Rain"],
    "5000": ["/static/Images/snow.svg", "Snow"],
    "5001": ["/static/Images/flurries.svg", "Flurries"],
    "5100": ["/static/Images/snow_light.svg", "Light Snow"],
    "5101": ["/static/Images/snow_heavy.svg", "Heavy Snow"],
    "6000": ["/static/Images/freezing_drizzle.svg", "Freezing Drizzle"],
    "6001": ["/static/Images/freezing_rain.svg", "Freezing Rain"],
    "6200": ["/static/Images/freezing_rain_light.svg", "Light Freezing Rain"],
    "6201": ["/static/Images/freezing_rain_heavy.svg", "Heavy Freezing Rain"],
    "7000": ["/static/Images/ice_pellets.svg", "Ice Pellets"],
    "7101": ["/static/Images/ice_pellets_heavy.svg", "Heavy Ice Pellets"],
    "7102": ["/static/Images/ice_pellets_light.svg", "Light Ice Pellets"],
    "8000": ["/static/Images/tstorm.svg", "Thunderstorm"]
}

function hide_all_div() {
    document.getElementById("no-result-section").style.display = "none";
    document.getElementById("weather-card-wrapper").style.display = "none";
    document.getElementById("detail-container").style.display = "none";
    document.getElementById("weather-table-wrapper").style.display = "none";
}

// store location data in json object entry, and build param with it for backend API call
function request_weather_data() {

    hide_all_div();

    var checkBox = document.getElementById("auto-location-check");

    // if user choose to detect location from IP address
    if (checkBox.checked == true) {
        fetch('https://ipinfo.io/json?token=15ee8a4671b9a0').
            then(function (response) {
                if (response.status !== 200) {
                    console.log(`Response status: ${response.status}`);
                    return;
                }
                response.json().
                    then(function (data) {
                        // Get city and state to display in the weather card
                        result_address = data.city + ", " + data.region + ", " + data.country;
                        console.log(result_address);
                        // Pass geo_location to get_weather_data()
                        get_weather_data(data.loc);
                    })
            });

    } else {
        // if user entered detalied address
        var street = document.getElementById("street");
        var city = document.getElementById("city");
        var state = document.getElementById("state")
        // build google geocode api query
        var query_address = street.value.trim() + ", " + city.value.trim() + ", " + state.value.trim();
        var geo_entry = {
            key: GEO_API_KEY,
            address: query_address
        };
        // build url with params
        var geo_url = new URL('https://maps.googleapis.com/maps/api/geocode/json');
        geo_url.search = new URLSearchParams(geo_entry).toString();
        // get location details
        fetch(geo_url).
            then(function (response) {
                if (response.status !== 200) {
                    console.log(`Response status: ${response.status}`);
                    return;
                }

                response.json().
                    then(function (data) {
                        // get formatted address
                        result_address = data.results[0].formatted_address;
                        console.log(result_address);
                        console.log(data);


                        // get geo location, pass to get_weather_data()
                        var geo_lat = data.results[0].geometry.location.lat;
                        var geo_lng = data.results[0].geometry.location.lng;
                        var geo_loc = geo_lat + "," + geo_lng;
                        get_weather_data(geo_loc);
                    })
            });


        var entry = {
            street: street.value,
            city: city.value,
            state: state.value
        };
        // get_weather_data(entry);
    }

}

// This function builds request url and send it to an API hosted by backend
// This call should populate data for current, 1h and 1d
function get_weather_data(geo_location) {

    var entry = {
        loc: geo_location
    };
    var url = new URL(`${window.origin}/weather-api/json`);
    url.search = new URLSearchParams(entry).toString();
    fetch(url).
        then(function (response) {
            if (response.status !== 200) {
                // Display No records
                document.getElementById("no-result-section").style.display = "block";
                console.log(`Response status: ${response.status}`);
                return;
            }

            response.json().
                then(function (data) {
                    populate_result(data);
                })
        });
}

function processTableJson(data) {
    var days = [];
    for (var i = 0; i < data.length; i++) {
        var row = JSON.parse(JSON.stringify(data[i].values));
        // data[i].values = data[i].startTime;
        row["startTime"] = data[i].startTime;
        days.push(row);
    }
    return days;
}

function jsonToTable(data) {
    // json data [ {day 1}, {day 2}, ... {day n}]
    var jsonData = processTableJson(data);

    // Create a table element
    var table = document.createElement("table");

    // Table header and the key to look up the value of each column
    var headers = ["Date", "Status", "Temp High", "Temp Low", "Wind Speed"];
    var keys = ["startTime", "weatherCode", "temperatureMax", "temperatureMin", "windSpeed"];

    // Generate header row, use -1 to append tr to the last row
    var tr = table.insertRow(-1);
    for (var i = 0; i < headers.length; i++) {
        var th = document.createElement("th");
        th.innerHTML = headers[i];
        tr.appendChild(th);
    }

    // add json data to table rows
    for (var i = 0; i < jsonData.length; i++) {

        tr = table.insertRow(-1);

        for (var j = 0; j < keys.length; j++) {
            var cell = tr.insertCell(-1);
            // for weather code, j==1, turn code into icon and weather description
            if (j == 0) {
                var date = new Date(jsonData[i][keys[j]]);
                var weekday = date.toLocaleDateString("en-US", { weekday: 'long' });
                var day = ("0" + date.getDate()).slice(-2);
                var month = date.toLocaleDateString("en-US", { month: 'short' });
                var year = date.toLocaleDateString("en-US", { year: 'numeric' });
                var formatted_date = weekday + ", " + day + " " + month + " " + year;
                cell.innerHTML = formatted_date;
            }
            else if (j == 1) {
                // Get icon corresponding to the weather code
                weather_code = jsonData[i][keys[j]];
                var icon_src = "";
                var icon_txt = "";
                if (weather_code in icon_mapping) {
                    icon_src = icon_mapping[weather_code][0];
                    icon_txt = icon_mapping[weather_code][1];
                } else {
                    icon_src = "/static/Images/tstorm.svg";
                    icon_txt = "Invalid Weather Code";
                }
                icon = document.createElement("img");
                icon.className = "table_row_icon";
                icon.src = icon_src;
                cell.appendChild(icon);

                // get description corresponding to the weather code
                text_span = document.createElement("span");
                text_span.innerHTML = icon_txt;
                cell.appendChild(text_span);

                // cell style
                cell.style.display = "flex";
                cell.style.alignItems = "center";
                cell.style.justifyContent = "center";
            }
            else {
                cell.innerHTML = jsonData[i][keys[j]];
            }
        }
    }

    // div where table is shown
    var table_div = document.getElementById("weather-table-div");
    table_div.appendChild(table);

}

function populate_result(data) {
    // Weather Card
    document.getElementById("weather-card-wrapper").style.display = "block";

    curr_weather_data = data.data.timelines[0].intervals[0].values
    document.getElementById("weather-city-state-title").innerHTML = result_address;
    // Change icon and icon text according to weahter code
    weather_code = String(curr_weather_data.weatherCode);
    if (weather_code in icon_mapping) {
        img_src = icon_mapping[weather_code][0];
        img_txt = icon_mapping[weather_code][1];
    } else {
        img_src = "/static/Images/tstorm.svg";
        img_txt = "Invalid Weather Code";
    }
    document.getElementById("weather-img").style.backgroundImage = "url('" + img_src + "')";
    document.getElementById("weather-img-text").innerHTML = img_txt;
    // Populate other weahter stats
    document.getElementById("weather-card-temp").innerHTML = Math.round(curr_weather_data.temperature * 10) / 10;
    document.getElementById("weather-humidity").innerHTML = curr_weather_data.humidity;
    document.getElementById("weather-pressure").innerHTML = curr_weather_data.pressureSeaLevel;
    document.getElementById("weather-wind").innerHTML = curr_weather_data.windSpeed;
    document.getElementById("weather-visibility").innerHTML = curr_weather_data.visibility;
    document.getElementById("weather-cloud").innerHTML = curr_weather_data.cloudCover;
    document.getElementById("weather-UV").innerHTML = curr_weather_data.uvIndex;

    // Others to do
    jsonToTable(data.data.timelines[2].intervals);
    document.getElementById("weather-table-wrapper").style.display = "block";
    console.log(data);
}

// This button to clear input form and result
function clear_page() {

    // clean input form and checked box
    document.getElementById("input-form").reset();

    var inputbox = document.getElementById("street")
    if (inputbox.disabled == true) {
        document.getElementById("street").disabled = false;
        document.getElementById("city").disabled = false;
        document.getElementById("state").disabled = false;
    }

    // clean result here and hide it
    hide_all_div()
}

function checkbox_switch() {
    var checkBox = document.getElementById("auto-location-check");
    // var resultSection = document.getElementById("result-section");

    if (checkBox.checked == true) {
        document.getElementById("input-form").reset();
        document.getElementById("auto-location-check").checked = true;
        document.getElementById("street").disabled = true;
        document.getElementById("city").disabled = true;
        document.getElementById("state").disabled = true;
    } else {
        // uncheck the checkbox should reset everything on the page
        clear_page()
    }
}
