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
import lxml.html



while True:
    #youll have to go to https://weather.com/weather and search for your city than copy and paste the URL below where mine is
    page = requests.get("https://weather.com/weather/today/l/57312336018afbd8918d5eefe6ccd5308696bf6d8056348868a1d39d80709a34")
    soup=BeautifulSoup(page.content,"html.parser")
    soup_condition=BeautifulSoup(page.content,"html.parser")
    #fix the html not found error when updating, problem occurs in line below
    lxml = lxml.html.fromstring(page.content)

    #all the web scraping classes to get the information
    current_temperature = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/span/text()""")[0]
    current_state = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/div/text()""")[0]
    current_precip = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[3]/span/text()""")[0]
    current_high = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[2]/div[1]/div[2]/span[1]/text()""")[0]
    current_low = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[2]/div[1]/div[2]/span[2]/text()""")[0]
    current_realfeel = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[1]/div[1]/span[1]/text()""")[0]
    sunset_time = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[1]/div[2]/div/div/div/div[2]/p/text()""")[0]
    sunrise_time = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/div[1]/div[2]/div/div/div/div[1]/p/text()""")[0]
    location = lxml.xpath("""/html/body/div[1]/main/div[2]/main/div[6]/section/header/h2/text()""")[0]
    humidity = lxml.xpath("""//*[@id="todayDetails"]/section/div[2]/div[3]/div[2]/span/text()""")[0]

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
        pass_highlow = tk.Label(text= "High/Low: " + str(current_high) + " / " + str(current_low))
        updateButton = tk.Button(text = "Update", command = root.destroy)
        closeButton = tk.Button(text= "Close", command= quit)
        pass_realfeal = tk.Label(text= "Real Feel: " + str(current_realfeel))
        pass_time = tk.Label(text= "Last Update: " + str(last_update))
        pass_sunset = tk.Label(text= "Sunset at: " + str(sunset_time))
        pass_sunrise = tk.Label(text= "Sunrise at: " + str(sunrise_time))
        pass_location = tk.Label(text= location)
        pass_humidity = tk.Label(text= "Humidity: " + str(humidity))

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
        pass_humidity.place(x=235, y= 100)
        updateButton.place(x=175, y=150)
        closeButton.place(x=177, y=200)
        pass_highlow.place(x=350, y=100)

        #the things needed to update it
        root.quit()
        print("weather updated")
        root.mainloop()
        time.sleep(1)
    
    tkinter()