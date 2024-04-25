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
            try:
                print('Checking time... (Ctrl+C to stop)')
                schedule.run_pending()
                time.sleep(30)
            except KeyboardInterrupt:
                print('Stopping...')
                break


#testing#
alarm_time = '09:05'
playlist_uri = 'spotify:playlist:230kXxkxNUviyASkzwiW61'
backend = SpotifyPlayback()
alarmsys = Schedule(backend)
alarmsys.set_alarm(alarm_time, playlist_uri)
print(alarmsys.get_alarm())
print(alarmsys.get_playlist())
alarmsys.start_timecheck()
#on breaking loop, change alarm time - proof of concept#
alarmsys.set_alarm('09:10', playlist_uri)
print(alarmsys.get_alarm())
alarmsys.start_timecheck()