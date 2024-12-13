import requests
apikey = open("apikey.txt",'r').read()
def fetch_weather(location):
    try:
        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}&units=metric")
        data = result.json()
        if result.json()["cod"] != 200:
            return {"error": data.get("message", "Unknown error")}

        return {
            "name": data["name"],
            "description": data["weather"][0]["description"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"]
        }
    except Exception as e:
        return {"error": str(e)}