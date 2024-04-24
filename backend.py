import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import schedule
import time

# Set up Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('alarmify_clientID'),
                                               client_secret=os.getenv('alarmify_clientsecret'),
                                               redirect_uri="http://localhost:8080",
                                               scope="user-modify-playback-state user-read-playback-state"))

# Function to play music from a playlist
def play_playlist(playlist_uri):
    try:
        devices = sp.devices()
        if 'devices' in devices and devices['devices']:
            device_id = devices['devices'][0]['id']  # Use the first available device
            sp.start_playback(context_uri=playlist_uri, device_id=device_id)
        else:
            print("No active device found.")
    except spotipy.SpotifyException as e:
        print("Error occurred while retrieving devices:", e)

# Schedule the alarm to play a playlist at a specific time
def schedule_alarm(playlist_uri, alarm_time):
    schedule.every().day.at(alarm_time).do(play_playlist, playlist_uri)

# Example usage
if __name__ == "__main__":
    # Playlist URI for the alarm
    playlist_uri = 'spotify:playlist:7nc7OQdPTekErtFSRxOBKh'
    
    # Set the time for the alarm (24-hour format)
    alarm_time = '13:44'  # Example: 8:00 AM
    
    # Schedule the alarm
    schedule_alarm(playlist_uri, alarm_time)
    
    # Loop to check the schedule every minute
    while True:
        schedule.run_pending()
        time.sleep(5)

