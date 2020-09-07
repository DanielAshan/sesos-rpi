from tkinter import *


import urllib.request
import simplejson as json
import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def sendingReg():
    print("wejscier")
   
    reader = SimpleMFRC522()

    try:
            id, text = reader.read()
            strid = str(id)
            print(strid)
            print(text)
    finally:
            GPIO.cleanup()
           
           
    print("wysłano rej")
    responser = requests.post("http://185.243.52.8/api/register/"+(strid))

    print (responser.content)
    print(zajecia["lesson"]["name"])
    print(zajecia["id"])

def sendingLog():
   
    print("wejsciel")
    reader = SimpleMFRC522()

    try:
            id, text = reader.read()
            strid = str(id)
            print(strid)
            print(text)
    finally:
            GPIO.cleanup()
   
    print (id)
     
    print("wysłano log")
    responsel = requests.post("http://185.243.52.8/api/addAttendanceRecord/9", data = { "nfc_id": id})

    print (responsel.content)
    print(zajecia["lesson"]["name"])
    print(zajecia["id"])

root = Tk()

response = requests.get("http://185.243.52.8/api/getCurrentLecture/E3")
tablica = response.json()
zajecia = tablica[0]


w = Label(root,font = ('calibri', 40), text=(zajecia["lesson"]["name"]))
y = Label(root,font = ('calibri', 30, 'bold'), text=(zajecia["lesson"]["description"]))
x = Label(root,font = ('calibri', 25, 'bold'), text=("start:",(zajecia["start_date"])))
z = Label(root,font = ('calibri', 20, 'bold'), text=("koniec:",(zajecia["end_date"])))
w.pack()
y.pack()
x.pack()
z.pack()

RegButton = Button(root, font = ('calibri', 40), text="Rejestracja", command = sendingReg)
RegButton.pack()

LogButton = Button(root, font = ('calibri', 40), text="Logowanie", command = sendingLog)
LogButton.pack()

root.geometry("800x400")
     
root.mainloop()