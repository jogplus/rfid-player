import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import spotipy_helper
import time
import config


def run():
    cfg = config.Config()
    reader = SimpleMFRC522()
    sp = spotipy_helper.SpotipyHelper(cfg)
    try:
        while True:
            card_id, text = reader.read()
            msg = text.strip()
            print(card_id, msg)
            if msg == "switch":
                requests.post(f"{cfg.roku_target}/launch/tvinput.hdmi2")
            else:
                requests.post(f"{cfg.roku_target}/launch/22297")
                time.sleep(1)
                sp.play_track(msg)
            time.sleep(3)
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    run()
