import sqlite3


conn = sqlite3.connect('weather.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS weather (
                city TEXT PRIMARY KEY,
                temperature TEXT,
                humidity TEXT,
                condition TEXT)''')

c.execute("INSERT OR REPLACE INTO weather (city, temperature, humidity, condition) VALUES ('Chennai', '30°C', '60%', 'Sunny')")
c.execute("INSERT OR REPLACE INTO weather (city, temperature, humidity, condition) VALUES ('Bangalore', '25°C', '70%', 'Cloudy')")
c.execute("INSERT OR REPLACE INTO weather (city, temperature, humidity, condition) VALUES ('Delhi', '20°C', '80%', 'Rainy')")
c.execute("INSERT OR REPLACE INTO weather (city, temperature, humidity, condition) VALUES ('Mumbai', '35°C', '50%', 'Sunny')")
c.execute("INSERT OR REPLACE INTO weather (city, temperature, humidity, condition) VALUES ('Kolkata', '40°C', '30%', 'Sunny')")


conn.commit()


conn.close()
