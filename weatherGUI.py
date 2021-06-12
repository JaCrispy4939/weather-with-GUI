#Made by Ja'Crispy4939, please dont steal the code and name it yours
#Enjoy :)

import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from datetime import time
import os
import time
import tkinter as tk

while True:
    #youll have to go to https://weather.com/weather and search for your city than copy and paste the URL below where mine is
    page = requests.get("https://weather.com/weather/today/l/57312336018afbd8918d5eefe6ccd5308696bf6d8056348868a1d39d80709a34")
    soup=BeautifulSoup(page.content,"html.parser")
    soup_condition=BeautifulSoup(page.content,"html.parser")
    #all the web scraping classes to get the information
    current_temperature = soup.find(class_="CurrentConditions--tempValue--MHmYY").text
    current_state = soup_condition.find(class_="CurrentConditions--phraseValue--mZC_p").text
    current_precip = soup.find(class_="CurrentConditions--precipValue--2aJSf").text
    current_highlow = soup.find(class_="WeatherDetailsListItem--wxData--kK35q").text
    current_realfeel = soup.find(class_="TodayDetailsCard--feelsLikeTempValue--2icPt").text
    sunset_time = soup.find(class_="SunriseSunset--sunsetDateItem--1nyxW SunriseSunset--sunriseDateItem--H9yAh").text
    sunrise_time = soup.find(class_="SunriseSunset--sunriseDateItem--H9yAh").text
    location = soup.find(class_="CurrentConditions--location--1YWj_").text
    

    

    #date and time vars
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%m/%d/%Y")
    last_update = time.strftime("%H:%M:%S")
    
    #tkinter window setup
    def tkinter():
        global root
        root = tk.Tk()
        root.title("Weather By JaCrispy")
        root.geometry("500x300")
        
        #tkinter var setup
        global pass_var
        pass_var=tk.StringVar()
        pass_temp = tk.Label(text= "Current Temp: " + str(current_temperature))
        pass_precip = tk.Label(text= "Rain: " + str(current_precip))
        pass_day = tk.Label(text= "Date: " + str(today))
        pass_clouds = tk.Label(text= "State: "+ str(current_state))
        pass_highlow = tk.Label(text= "High/Low: " + str(current_highlow))
        updateButton = tk.Button(text = "Update", command = root.destroy)
        closeButton = tk.Button(text= "Close", command= quit)
        pass_realfeal = tk.Label(text= "Real Feel: " + str(current_realfeel))
        pass_time = tk.Label(text= "Last Update: " + str(last_update))
        pass_sunset = tk.Label(text= str(sunset_time))
        pass_sunrise = tk.Label(text= str(sunrise_time))
        pass_location = tk.Label(text= location)
        
        #tkinter var placement 
        pass_location.place(x=150, y=30)
        pass_sunrise.place(x= 50, y= 150)
        pass_sunset.place(x= 250, y=150)
        pass_time.place(x=250, y= 10)
        pass_realfeal.place(x= 50, y= 100)
        pass_day.place(x=150, y= 10)
        pass_precip.place(x=250, y=50)
        pass_temp.place(x=50, y= 50)
        pass_clouds.place(x=135, y=100)
        updateButton.place(x=175, y=150)
        closeButton.place(x=177, y=200)
        pass_highlow.place(x=350, y=100)

        #the things needed to update it
        root.quit()
        print("weather updated")
        root.mainloop()
        time.sleep(1)
    
    tkinter()