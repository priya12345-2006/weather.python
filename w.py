# Importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # Getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # Base URL
    try:
        # Construct the full URL with your API key and city name
        complete_url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName
        response = requests.get(complete_url)  # Requesting content from the URL
        x = response.json()  # Converting response to JSON

        # Check if city was found
        if x["cod"] != 200:
            mb.showerror("Error", f"City '{cityName}' not found.")
            return

        y = x["main"]
        temp = y["temp"] - 273.15  # Convert from Kelvin to Celsius
        pres = y["pressure"]
        hum = y["humidity"]
        weather_desc = x["weather"][0]["description"]

        # Format info string
        info = f"""Here is the weather description of {cityName}:
Temperature = {temp:.2f}°C
Atmospheric pressure = {pres} hPa
Humidity = {hum}%
Weather description = {weather_desc}"""

        # Show notification
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            timeout=5  # Duration of notification
        )
        time.sleep(1)  # Short delay

    except Exception as e:
        mb.showerror('Error', str(e))  # Show error pop-up

# Creating the window
wn = Tk()
wn.title("PythonGeeks Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

# Getting the city name 
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get notification
btn = Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification)
btn.place(relx=0.4, rely=0.75)

# Run the window till closed by user
wn.mainloop()
