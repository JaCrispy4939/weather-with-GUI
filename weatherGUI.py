#Made by Ja'Crispy4939, please dont steal the code and name it yours
#Enjoy :)

import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
import os
import time
import tkinter as tk

while True:
    #youll have to go to https://weather.com/weather and search for your city than copy and paste the URL below where mine is
    page = requests.get("https://weather.com/weather/today/l/57312336018afbd8918d5eefe6ccd5308696bf6d8056348868a1d39d80709a34")
    soup=BeautifulSoup(page.content,"html.parser")
    soup_condition=BeautifulSoup(page.content,"html.parser")
    current_temperature = soup.find(class_="CurrentConditions--tempValue--3KcTQ").text
    current_state = soup_condition.find(class_="CurrentConditions--phraseValue--2xXSr").text
    current_precip = soup.find(class_="CurrentConditions--precipValue--RBVJT").text
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%m/%d/%Y")

    
    
    def tkinter():
        global root
        root = tk.Tk()
        root.title("Weather By JaCrispy")
        root.geometry("500x150")
        

        global pass_var
        pass_var=tk.StringVar()
        pass_temp = tk.Label(text= "Current Temp: " + current_temperature)
        pass_precip = tk.Label(text= "Rain: " + str(current_precip))
        pass_day = tk.Label(text= "Date: " + str(today))
        pass_clouds = tk.Label(text= "Clouds: "+ current_state)
        updateButton = tk.Button(text = "Update", command = root.destroy)
        closeButton = tk.Button(text= "Close", command= quit)

        pass_day.place(x=150, y= 10)
        pass_precip.place(x=250, y=50)
        pass_temp.place(x=50, y= 50)
        pass_clouds.place(x=135, y=100)
        updateButton.place(x=175, y=50)
        closeButton.place(x=177, y=125)

        root.quit()
        print("weather updated")
        root.mainloop()
        time.sleep(1)
    tkinter()
