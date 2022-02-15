import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
from spotify import MySpotify
import time

reader = SimpleMFRC522()
sp = MySpotify()
try:
    while True:
        my_id, text = reader.read()
        print(my_id, text)
        if text.strip() == "switch":
            requests.post("http://192.168.0.25:8060/launch/tvinput.hdmi2")
        else:
            requests.post("http://192.168.0.25:8060/launch/22297")
            time.sleep(1)
            sp.play_track(text.strip())
        time.sleep(3)

finally:
    GPIO.cleanup()
