import tkinter as tk
import requests
import folium

def get_weather():
    # Get the user's input from the entry field
    location = entry.get()

    # Use an external weather API to fetch weather data (replace API_KEY with your API key)
    api_key = '3576a335115fd71f7e01ec64d2f8b029'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)

    try:
        response.raise_for_status()  # Raise an error if the HTTP request was unsuccessful

        data = response.json()

        # Extract weather information from the API response
        temperature = data['main']['temp'] - 273.15  # Convert temperature to Celsius
        humidity = data['main']['humidity']
        conditions = data['weather'][0]['description']

        # Extract wind information
        wind_speed = data['wind']['speed']
        wind_direction = data['wind']['deg']

        # Display weather and wind information on the Tkinter interface with a bold font
        weather_label.config(text=f'Temperature: {temperature:.2f}°C\nHumidity: {humidity}%\nConditions: {conditions}\nWind Speed: {wind_speed} m/s\nWind Direction: {wind_direction}°', font=('Arial', 12, 'bold'))

        # Display the location on a map using Folium
        location_map = folium.Map(location=[data['coord']['lat'], data['coord']['lon']], zoom_start=10)
        folium.Marker([data['coord']['lat'], data['coord']['lon']], tooltip=location).add_to(location_map)
        location_map.save('location_map.html')

    except requests.exceptions.HTTPError as err:
        weather_label.config(text=f'Error: {err}', font=('Arial', 12, 'bold'))

    except Exception as e:
        weather_label.config(text=f'An unexpected error occurred: {e}', font=('Arial', 12, 'bold'))


# Create the main Tkinter window
root = tk.Tk()
root.title('Weather App with Maps')

# Create a label and entry field for location input
label = tk.Label(root, text='Enter Location:', font=('Arial', 14))
label.pack()
entry = tk.Entry(root, font=('Arial', 14))
entry.pack()

# Create a "Search" button to get weather information
search_button = tk.Button(root, text='Search', command=get_weather, font=('Arial', 14))
search_button.pack()

# Create a label to display weather information
weather_label = tk.Label(root, text='', font=('Arial', 12))
weather_label.pack()

# Create a footer label
footer_label = tk.Label(root, text='Powered by Adi', font=('Arial', 10))
footer_label.pack()

# Run the Tkinter main loop
root.mainloop()
