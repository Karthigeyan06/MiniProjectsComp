import tkinter as tk
from tkinter import ttk
import sqlite3

def get_weather(city):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute("SELECT * FROM weather WHERE city=?", (city,))
    result = c.fetchone()
    conn.close()
    return result

def show_weather():
    city = city_combobox.get()
    weather = get_weather(city)
    if weather:
        temperature_label.config(text=f"Temperature: {weather[1]}")
        humidity_label.config(text=f"Humidity: {weather[2]}")
        condition_label.config(text=f"Condition: {weather[3]}")
    else:
        temperature_label.config(text="Temperature: N/A")
        humidity_label.config(text="Humidity: N/A")
        condition_label.config(text="Condition: N/A")


root = tk.Tk()
root.title("Weather App")


city_label = tk.Label(root, text="Select City:")
city_label.grid(column=0, row=0, padx=10, pady=10)

city_combobox = ttk.Combobox(root, values=["Chennai", "Bangalore", "Delhi", "Mumbai", "Kolkata"])
city_combobox.grid(column=1, row=0, padx=10, pady=10)


show_button = tk.Button(root, text="Show Weather", command=show_weather)
show_button.grid(column=2, row=0, padx=10, pady=10)


temperature_label = tk.Label(root, text="Temperature: ")
temperature_label.grid(column=0, row=1, columnspan=3, padx=10, pady=10)

humidity_label = tk.Label(root, text="Humidity: ")
humidity_label.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

condition_label = tk.Label(root, text="Condition: ")
condition_label.grid(column=0, row=3, columnspan=3, padx=10, pady=10)

root.mainloop()
