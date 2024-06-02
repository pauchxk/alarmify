## Current Version: 1.2
Backend is handled by Python, split into 3 programs. spotify_playback.py handles the Spotify API requests when the alarm is triggered; schedule_backend.py handles the scheduling of the alarm and the time check loop; app.py uses Flask API to connect the backend with the frontend through http requests to and from a local server. 
Frontend is handled by Flutter, which at the moment is a rudimentary GUI as it is still an early prototype. Interaction with the GUI causes event handlers to send and receive information from the backend.

## Aims
1.3 will introduce a more elegant GUI on the frontend, better formatting and organisation of program files across the board, and better error-handling/durability in the backend for the purpose of long-term usage of the app (i.e. setting an alarm and having it trigger multiple times across several days), 
as the ultimate aim is to have the program run in the background constantly.
