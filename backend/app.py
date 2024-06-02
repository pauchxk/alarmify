from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import os

from schedule_backend import Schedule
from spotify_playback import SpotifyPlayback

app = Flask(__name__)
CORS(app)

# Initialize the backend
backend = SpotifyPlayback()
alarmsys = Schedule(backend)

# Route to set the alarm
@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    data = request.json
    alarm_time = data.get('alarm_time')
    playlist_uri = data.get('playlist_uri')
    
    alarmsys.set_alarm(alarm_time, playlist_uri)
    return jsonify({'message': 'Alarm set successfully'})

# Route to get the current alarm
@app.route('/get_alarm', methods=['GET'])
def get_alarm():
    alarm_time = alarmsys.get_alarm()
    playlist_uri = alarmsys.get_playlist()
    return jsonify({'alarm_time': alarm_time, 'playlist_uri': playlist_uri})

# Route to start the time check loop
@app.route('/start_timecheck', methods=['POST'])
def start_timecheck():
    # Use threading to run the time check loop in the background
    threading.Thread(target=alarmsys.start_timecheck).start()
    return jsonify({'message': 'Time check started'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)