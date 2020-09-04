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

Note the redirect URL can be a valid URL, just ensure it matches with what you have entered in the developer console & in the environment variable above.

Create your YouTube API key & fetch the keys from Google Developer Console. Set the key as YOUTUBE_DEV_KEY environment variable as mentioned above.

Run the script using spotify_dl. spotify_dl accepts different parameters, for more details run spotify_dl -h.

For most users spotify_dl -l spotify_playlist_link -o download_directory should do where

spotify_playlist_link is a link to Spotify's playlist. You can get it from the 3-dot menu.
