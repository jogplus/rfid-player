import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json


class MySpotify:
    def __init__(self):
        scope = "user-read-playback-state user-modify-playback-state"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))

    def play_track(self, uri: str):
        devices = self.sp.devices()
        print(json.dumps(devices, indent=4, sort_keys=True))
        for device in devices["devices"]:
            if "Roku" in device["name"]:
                device_id = device["id"]
                print(f"Selected: {device}")
                break

        self.sp.start_playback(device_id=device_id, uris=[uri])

