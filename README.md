# numbergame
this is multiplayer number game

How do I get this thing running?
Pre-requisite: You need Python 3.6+

Install using pip sudo pip3 install spotify_dl (use pip if your distro natively provides Python 3)

Create your Spotify app & fetch the client id and client secret from Spotify Developer Console. These keys then need to be assigned as SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET and SPOTIPY_REDIRECT_URI environment variables.

You can set environment variables in Linux like so:

     export SPOTIPY_CLIENT_ID='your-spotify-client-id'
     export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
     export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
Windows users, check for this question for details on how you can set environment variables.
