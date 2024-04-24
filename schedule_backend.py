#imports#
from spotify_playback import SpotifyPlayback
import schedule
import time


class Schedule:

    #initialise backend#
    def __init__(self, backend):
        self.backend = backend


    #set schedule and send data to backend (spotify_playback)#
    def schedule_alarm(self, alarm_time, playlist_uri):
        schedule.every().day.at(alarm_time).do(lambda: self.backend.play_playlist(playlist_uri))


    #set alarm and playlist URI#
    def set_alarm(self, alarm_time, playlist_uri):
        self.alarm_time = alarm_time
        self.playlist_uri = playlist_uri

        self.schedule_alarm(self.alarm_time, self.playlist_uri)
        print(f'Set alarm: {self.alarm_time}, playlist URI: {self.playlist_uri}')

    
    #return current alarm#
    def get_alarm(self):
        return self.alarm_time

    
    #return current playlist URI#
    def get_playlist(self):
        return self.playlist_uri


    #start time check loop#
    def start_timecheck(self):
        while True:
            print('Checking time...')
            schedule.run_pending()
            time.sleep(30)


#testing#
alarm_time = '15:50'
playlist_uri = 'spotify:playlist:1U3QinJxrVEyirGUYUt7Pp'
backend = SpotifyPlayback()
alarmsys = Schedule(backend)
alarmsys.set_alarm(alarm_time, playlist_uri)
alarmsys.get_alarm()
alarmsys.get_playlist()
alarmsys.start_timecheck()