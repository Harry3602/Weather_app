import requests
apikey = open("apikey.txt",'r').read()
while True:
    location = input("Enter the location: ")
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}")
    if result.json()["cod"] == 200:
        break

with open("result.txt",'w') as f:
    f.write(f"{result.json()['name']}\n")
    f.write(f"{result.json()['weather'][0]["description"]}\n")
    f.write(f"temperature: {result.json()['main']['temp']}\t")
    f.write(f"feels like: {result.json()['main']['feels_like']}\n")
