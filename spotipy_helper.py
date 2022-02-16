import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
import json


class SpotipyHelper:
    def __init__(self, config: config.Config):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=config.spotipy_client_id,
                client_secret=config.spotipy_secret,
                redirect_uri=config.spotipy_redirect_uri,
                scope=config.spotipy_scope,
                open_browser=False,
            ),
        )

    def play_track(self, uri: str):
        devices = self.sp.devices()
        print(json.dumps(devices, indent=4, sort_keys=True))
        for device in devices["devices"]:
            if "Roku" in device["name"]:
                device_id = device["id"]
                print(f"Selected: {device}")
                break

        self.sp.start_playback(device_id=device_id, uris=[uri])
