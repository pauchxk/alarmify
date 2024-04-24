## Current Version: 1.0
Operation is split into two programs: schedule_backend.py handles requests to set alarm time and playlist URI - currently only possible through hard-coded inputs to the object - and runs the time check loop. On a successful check, schedule sends the play_playlist request along with the playlist URI to spotify_playback.py; this authenticates my user credentials, redirect URI and scope, and then checks for available devices to initialise playback on. If a device is found, the start_playback request is sent.

## Aims
Version 1.1 will be an executable using a CLI to accept user inputs of time and playlist. Then, the program will run in the background. Long-term, user inputs will be handled by a GUI in a separate frontend.py program, initialising on PC startup and remembering user preferences (time and playlist) by calling it from a text file.
