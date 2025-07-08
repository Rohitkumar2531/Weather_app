import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io, requests

from utils.api import fetch_weather
from utils.location import detect_location

def show_weather():
    city = city_entry.get() or detect_location()
    if not city:
        messagebox.showwarning("Location Error", "Could not detect your city.")
        return

    data = fetch_weather(city)

    if data.get("cod") != 200:
        messagebox.showerror("API Error", data.get("message", "Unknown error"))
        return

    weather = data["weather"][0]["description"].capitalize()
    icon_code = data["weather"][0]["icon"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    weather_text = (
        f"City: {city}\n"
        f"Weather: {weather}\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind} m/s"
    )

    result_label.config(text=weather_text)
    show_icon(icon_code)

def show_icon(icon_code):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    img_data = response.content
    img = Image.open(io.BytesIO(img_data))
    img = img.resize((100, 100))
    img_tk = ImageTk.PhotoImage(img)
    icon_label.config(image=img_tk)
    icon_label.image = img_tk  # Prevent garbage collection

# GUI Setup
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("300x400")

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=5)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

icon_label = tk.Label(root)
icon_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 11), justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()