import schedule
import time

class Schedule:
    def __init__(self, backend):
        self.backend = backend
        self.alarm_time = None
        self.playlist_uri = None

    def schedule_alarm(self, alarm_time, playlist_uri):
        schedule.every().day.at(alarm_time).do(lambda: self.backend.play_playlist(playlist_uri))

    def set_alarm(self, alarm_time, playlist_uri):
        self.alarm_time = alarm_time
        self.playlist_uri = playlist_uri
        self.schedule_alarm(self.alarm_time, self.playlist_uri)
        print(f'Set alarm: {self.alarm_time}, playlist URI: {self.playlist_uri}')

    def get_alarm(self):
        return self.alarm_time
        
    def get_playlist(self):
        return self.playlist_uri

    def start_timecheck(self):
        while True:

            try:
                print('Checking time... (Ctrl+C to stop)')
                schedule.run_pending()
                time.sleep(30)
                
            except KeyboardInterrupt:
                print('Stopping...')
                break
