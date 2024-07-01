import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk

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
        update_background(weather[3])
    else:
        temperature_label.config(text="Temperature: N/A")
        humidity_label.config(text="Humidity: N/A")
        condition_label.config(text="Condition: N/A")

def update_background(condition):
    if condition.lower() == "sunny":
        background_image = Image.open(r"C:\Users\karth\Downloads\sunny.jpg")
    elif condition.lower() == "cloudy":
        background_image = Image.open(r"C:\Users\karth\Downloads\cloudy.jpg")
    elif condition.lower() == "rainy":
        background_image = Image.open(r"C:\Users\karth\Downloads\rainy.jpg")
    elif condition.lower() == "hot":
        background_image = Image.open("hot.jpg")
    elif condition.lower() == "humid":
        background_image = Image.open("humid.jpg")
    else:
        background_image = Image.open("default.jpg")
    
    background_photo = ImageTk.PhotoImage(background_image)
    background_label.config(image=background_photo)
    background_label.image = background_photo


root = tk.Tk()
root.title("Weather Dis")
root.geometry("600x400")


background_image = Image.open(r"C:\Users\karth\OneDrive\Pictures\wsbg.png")
background_photo = ImageTk.PhotoImage(background_image)


background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='lightblue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

city_label = tk.Label(frame, text="Select City:", bg='lightblue', font=('Arial', 12, 'bold'))
city_label.pack(side='left', padx=10, pady=10)

city_combobox = ttk.Combobox(frame, values=["Chennai", "Bangalore", "Delhi", "Mumbai", "Kolkata"], font=('Arial', 12))
city_combobox.pack(side='left', padx=10, pady=10)

show_button = tk.Button(frame, text="Show Weather", command=show_weather, font=('Arial', 12, 'bold'))
show_button.pack(side='left', padx=10, pady=10)

details_frame = tk.Frame(root, bg='lightblue', bd=5)
details_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

temperature_label = tk.Label(details_frame, text="Temperature: ", bg='lightblue', font=('Arial', 14, 'bold'))
temperature_label.pack(pady=10)

humidity_label = tk.Label(details_frame, text="Humidity: ", bg='lightblue', font=('Arial', 14, 'bold'))
humidity_label.pack(pady=10)

condition_label = tk.Label(details_frame, text="Condition: ", bg='lightblue', font=('Arial', 14, 'bold'))
condition_label.pack(pady=10)

root.mainloop()
