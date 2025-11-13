import requests

API_KEY = "5970c159bfe1b6c06d3d73a0f8f15678" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\n🌤️  Weather in {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind speed: {data['wind']['speed']} m/s\n")
    else:
        print("\n❌ City not found. Please check the name and try again.\n")

if __name__ == "__main__":
    print("=== 🌦️ Simple Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)
