#imports#
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import AppOpener
import time


class SpotifyPlayback:

    #initialise spotify client authorisation#
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('alarmify_clientID'),
                                                    client_secret=os.getenv('alarmify_clientsecret'),
                                                    redirect_uri="http://localhost:8080",
                                                    scope="user-modify-playback-state user-read-playback-state"))


    #select device and start playback#
    def play_playlist(self, playlist_uri):
        AppOpener.open("spotify", throw_error=True)
        time.sleep(5)

        try:
            devices = self.sp.devices()

            if 'devices' in devices and devices['devices']:
                device_id = devices['devices'][0]['id']  #use the first available device
                self.sp.start_playback(context_uri=playlist_uri, device_id=device_id)

                print('Starting playback :)')

            else:
                print("No active device found.")

        except spotipy.SpotifyException as e:
            print("Error occurred while retrieving devices:", e)