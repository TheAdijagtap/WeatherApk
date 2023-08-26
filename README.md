# WeatherApk
This Python project is a Weather App with live location tracking. It leverages the Tkinter library for the graphical user interface and integrates with the OpenWeatherMap API to provide real-time weather data for a user-specified location.

<b>Here's a brief description of its key features:</b>

<b>1.User-Friendly Interface:</b> The app offers a simple and intuitive graphical interface built with Tkinter, including an input field for the location, a "Search" button to trigger the weather lookup, and a display area for weather information.

<b>Weather Data Retrieval:</b> Upon clicking the "Search" button, the app sends a request to the OpenWeatherMap API, fetching data such as temperature, humidity, weather conditions, wind speed, and wind direction for the specified location.

<b>Error Handling:</b> It incorporates robust error handling to manage situations where the API request might fail. Any errors, whether due to network issues or other unexpected problems, are presented to the user.

<b>Weather Display:</b> The app presents the retrieved weather information, including temperature in Celsius, humidity percentage, weather conditions, wind speed in meters per second, and wind direction in degrees, in a clear and readable format.

<b>Interactive Map:</b> It utilizes the Folium library to create an interactive map pinpointing the location of the queried place. A marker on the map helps users visualize the geographical context of the weather report.

<b>Data Storage:</b> The map with the location marker is saved as an HTML file ('location_map.html') for users to access and view outside the app.

<b>Footer Information:</b> A footer label credits the application creator or the source of weather data (in this case, "Powered by Adi").

Overall, this Weather App combines user-friendly design with real-time weather data retrieval and visualization on an interactive map, making it a handy tool for users to quickly access weather information and explore the location on a map.
