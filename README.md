# Spotify_to_YTMusic
 Free scrpit to (slowly) transfer songs and playlist from Spotify to YTMusic


First, setup spotipy with directions found here:
https://spotipy.readthedocs.io/en/2.21.0/

```
pip install spotipy
```

Hint: you have to enable spotify developer settings to get a SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET. You'll have to make system variables for these two values plus one for SPOTIPY_REDIRECT_URI which I set to http://127.0.0.1:9090

Next you have to set up ytmusicapi with irections found here:
https://ytmusicapi.readthedocs.io/en/latest/setup.html

```
pip install ytmusicapi
```

Hint: open youtube music in chrome, CTRL+SHIFT+i to open developer tools. Go to Network tab and put "browse" into the search bar. Click around the YTmusic page until something pops up that starts with something like: browse?ctoken=4qmFsgLf.... In the Request Header copy the value for Cookie (looks like CONSENT=YES+US.en+201905; LOGIN_INFO=....). Paste this value in the header.json file where is says: "ENTER COOKIE VALUE HERE:   Starts with: CONSENT=YES+US.en+201905; _ga=GA1.2XXXXXXXXXXXXXX; LOGIN_INFO="

Next run the save_all_spotify_songs.py which will get all your saved songs from Spotify. This creates a CSV and Pickle file so you can have a backup if needed. 
To transfer liked songs to YTmusic, run the transfer_saved_songs.ipynb file which will read the picke file you just created and add the songs to YTmusic

Be warned: this script works by taking the song title and artist and putting into the YTmusic search engine and picking the first result that shows up unless it's not a song (i.e. the first result is an album). It will try the second and third result add add them if it finds a song. If none of the results are a song or no results come up; the song is added to the "bad" bin. FYI, it always finds a song but sometimes it's wrong... I only have seen this for very obscure songs.


To Transfer playlist run transfer_playlist.ipynb. This works the same as adding a song but it just adds it to a playlist instead. PLaylist keep the same name as what you had on spotify.


FYI, these scripts take a long time to run but it's better thna paying 10 for the service that does this. For my 4300 songs the whole process took about an hour and a half.

I do not guarentee this code at all (but it worked for me).
