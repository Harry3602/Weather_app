# Weather_app
# Weather App

This is a simple weather application built using Python and PyQt5. It fetches weather data from the OpenWeatherMap API and displays it in a user-friendly interface.

## Features

- Search for weather information by city name
- Display current temperature, feels like temperature, and weather description
- Show appropriate weather icons based on the weather description

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Harry3602/Weather_app.git
    cd Weather_app
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Make sure you have an OpenWeatherMap API key. Replace the placeholder API key in [weather_app.py](http://_vscodecontentref_/1) with your own API key.

## Usage

1. Run the application:
    ```sh
    python app_ui.py
    ```

2. Enter a city name in the search bar and press Enter or click the search button to fetch and display the weather information.

## Project Structure

- [weather_app.py](http://_vscodecontentref_/2): Contains the function to fetch weather data from the OpenWeatherMap API.
- [app_ui.py](http://_vscodecontentref_/3): Contains the PyQt5 user interface code.
- [images](http://_vscodecontentref_/4): Contains the weather icons used in the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
