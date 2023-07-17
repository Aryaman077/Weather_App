#!/usr/bin/env python
# coding: utf-8

# In[1]:

# In[3]:


import time
import requests as req
import pyttsx3

def speaktext(command):
    text=pyttsx3.init()
    text.say(command)
    text.runAndWait()

#Current Weather
def getCurrentWeather():
    city = entry1.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city+"&appid=163980b15492f9e137f75d28c27309dd"
    json_data = req.get(api).json()
    print(json_data)
    description = str(json_data["weather"][0]["description"])
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = str(json_data['main']['pressure'])
    humidity = str(json_data['main']['humidity'])
    sunrise = str(time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600)))
    sunset = str(time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600)))
    w_speed = str(json_data["wind"]["speed"])

    final_description = description + "\n" + str(temp) + "°C"
    final_info = "Pressure: " + str(pressure) + " milibars" + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Sunrise: " + sunrise + " a.m." + "\n" + "Sunset: " + sunset + " p.m." + "\n" + "Wind Speed: " + str(w_speed) + " miles per hour"
    #print(final_info)
    #print(final_description)
    current_label2.config(text=final_description)
    current_label3.config(text=final_info)


#Past Weather
def getPastWeather():
    lat = entry2.get()
    long = entry3.get()
    api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + \
        lat+"&lon="+long+"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = req.get(api).json()
    past_description = json_data["daily"][0]["weather"][0]["description"]
    past_temp = int(json_data["daily"][0]['temp']['day'] - 273.15)
    past_pressure = str(json_data["daily"][0]['pressure'])
    past_humidity = str(json_data["daily"][0]['humidity'])
    past_sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data["daily"][0]["sunrise"] - 21600))
    past_sunset = time.strftime('%I:%M:%S', time.gmtime(json_data["daily"][0]["sunset"] - 21600))
    past_w_speed = str(json_data["daily"][0]["wind_speed"])
    final_past_description = past_description + "\n" + str(past_temp) + "°C"
    final_past_info = "Pressure: " + str(past_pressure) + " milibars" + "\n" + "Humidity: " + str(past_humidity) + "%" + "\n" + "Sunrise: " + past_sunrise + " a.m." + "\n" + "Sunset: " + past_sunset + " p.m." + "\n" + "Wind Speed: " + str(past_w_speed) + " miles per hour"
    #print(final_past_info)
    #print(final_past_description)
    current_label6.config(text=final_past_description)
    current_label7.config(text=final_past_info)

   

    
def getFutureWeather():
    city = entry5.get()
    api = "https://api.openweathermap.org/data/2.5/forecast?q=" + \
        city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = req.get(api).json()
    #print(json_data)
    fut_description = str(json_data["list"][0]["weather"][0]["description"])
    fut_temp = int(json_data["list"][0]['main']['temp'] - 273.15)
    fut_pressure = str(json_data["list"][0]['main']['pressure'])
    fut_humidity = str(json_data["list"][0]['main']['humidity'])
    fut_sunrise = str(time.strftime('%I:%M:%S', time.gmtime(json_data['city']['sunrise'] - 21600)))
    fut_sunset = str(time.strftime('%I:%M:%S', time.gmtime(json_data['city']['sunset'] - 21600)))
    fut_w_speed = str(json_data["list"][0]["wind"]["speed"])

    final_fut_description = fut_description + "\n" + str(fut_temp) + "°C"
    final_fut_info = "Pressure: " + str(fut_pressure) + " milibars" + "\n" + "Humidity: " + str(fut_humidity) + "%" + "\n" + "Sunrise: " + fut_sunrise + " a.m." + "\n" + "Sunset: " + fut_sunset + " p.m." + "\n" + "Wind Speed: " + str(fut_w_speed) + " miles per hour"
    #print(final_fut_info)
    #print(final_fut_description)
    current_label9.config(text=final_fut_description)
    current_label10.config(text=final_fut_info)
    


from tkinter import *
top = Tk()
top.title("Weather App")
top['bg']= 'light blue'
top.geometry("500x500")

current_label = Label(top, text="Weather Prediction App",justify='center', width=45, background="green", foreground="white")
current_label.pack()

    
def currentScreen():
    global entry1
    global current_label2
    global current_label3
   
    top = Toplevel()
    top.geometry("300x300")
    top["bg"] = "#A4DE02"
   
    current_label1 = Label(top, text="Please enter City Name to get current weather",
                       justify='center', width=45, background="green", foreground="white")
    current_label1.pack()
   
    entry1 = Entry (top)
    entry1.pack(pady=20)
   
    button1 = Button(top, text = "Show current weather", fg = "Black", command = getCurrentWeather)
    button1.place(x=80,y=250)
   
    current_label2 = Label(top,
                       justify='center', width=45, background="green", foreground="white")
    current_label2.pack()
   
    current_label3 = Label(top,
                       justify='center', width=45, background="green", foreground="white")
    current_label3.pack()
    top.after(1000, speaktext, "Welcome to the Current Weather Prediction feature. Please enter the name of the city or simply speak the city name to view the current weather status.")
    top.mainloop()

   
#Past
def pastScreen():
    global entry2
    global entry3
    global current_label6
    global current_label7
   
    top = Toplevel()
    top.geometry("300x450")
    top["bg"] = "#A4DE02"
   
    current_label5_1 = Label(top, text="Please enter City Lattitude to get past weather",
                       justify='center', width=45, background="green", foreground="white")
    current_label5_1.pack()
   
    entry2 = Entry (top)
    entry2.pack(pady=20)

    current_label5_2 = Label(top, text="Please enter City Longitude to get past weather",
                       justify='center', width=45, background="green", foreground="white")
    current_label5_2.pack()
   
    entry3 = Entry (top)
    entry3.pack(pady=40)
   
    button2 = Button(top, text = "Show past weather", fg = "Black", command = getPastWeather)
    button2.place(x=85,y=400)
   
    current_label6 = Label(top,
                       justify='center', width=45, background="green", foreground="white")
    current_label6.pack()
   
    current_label7 = Label(top,
                       justify='center', width=45, background="green", foreground="white")
    current_label7.pack()
    top.after(1000, speaktext, "Welcome to the Historical Weather Prediction feature. Please enter the latitude or longitude of the city or simply speak the latitude or longitude name to view the historical weather status.")  
    top.mainloop()
 


def getForecastWeather():

    global entry5
    global current_label9
    global current_label10
   
    top = Toplevel()
    top.geometry("300x400")
    top["bg"] = "#A4DE02"
   
    current_label8 = Label(top, text="Please enter City Name to get past weather",
                       justify='center', width=45, background="green", foreground="white")
    current_label8.pack()
   
    entry5 = Entry(top)
    entry5.pack(pady=20)

    button2 = Button(top, text = "Show future weather", fg = "Black", command = getFutureWeather)
    button2.place(x=85,y=350)
   
    current_label9 = Label(top,
                       justify='center', width=45, background="green", foreground="white")
    current_label9.pack()
   
    current_label10 = Label(top,
                       justify='center', width=45, background="green", foreground="white")
    current_label10.pack()

    top.after(1000, speaktext, "Welcome to the Forecast Weather Prediction feature. Please enter the name of the city or simply speak the city name to view the future weather status.")
    top.mainloop()
       

currentbutton = Button(top, text = "Click for current weather", fg = "Black", command = currentScreen)
currentbutton.place(x=200,y=60)

pastbutton = Button(top, text = "Click for past weather", fg = "Black", command = pastScreen)
pastbutton.place(x=200,y=160)

forecastbutton = Button(top, text = "Click for forecasted weather", fg = "Black", command = getForecastWeather)
forecastbutton.place(x=200,y=270)

#speaktext('Welcome to our Weather Prediction App! Unleash the power of weather prediction with our captivating app - past, present, and future weather data at your fingertips!')
top.after(1000, speaktext, "Welcome to our Weather Prediction App! Unleash the power of weather prediction with our captivating app - past, present, and future weather data at your fingertips!")


top.mainloop()


   




# In[ ]:




