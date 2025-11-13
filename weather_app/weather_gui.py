import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "5970c159bfe1b6c06d3d73a0f8f15678"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result_text.set(
                f"🌤️ Weather in {city_name}, {country}\n"
                f"Temperature: {temperature}°C\n"
                f"Feels like: {feels_like}°C\n"
                f"Condition: {description}\n"
                f"Humidity: {humidity}%\n"
                f"Wind speed: {wind_speed} m/s"
            )
        else:
            messagebox.showerror("Error", f"City '{city}' not found.")
            result_text.set("")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("🌦️ Weather App")
root.geometry("400x350")
root.resizable(False, False)
root.config(bg="#DFF6FF")

title_label = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#DFF6FF")
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather, bg="#62CDFF", fg="white", width=15)
search_button.pack(pady=5)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="#DFF6FF", justify="left")
result_label.pack(pady=10)

root.mainloop()
