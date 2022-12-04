import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
import pickle


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope)) #If you get error here, see the spoitpy page to see how to set it up right
point = 0
list_song = []
while True:
    
    try:
        songs = sp.current_user_saved_tracks(limit=20, offset= point)['items'] #FYI you can oly read 20 songs per request
        point = point + 20
        for idx, track in enumerate(songs):
            list_song.append(track['track'])
            print(point, "   |||   Artist: ", track['track']['artists'][0]['name'], "  |||   Title: ",track['track']['name'])
        if len(songs) == 0:
            print("empty")
            break
    except KeyboardInterrupt:
        break





keys = track['track'].keys()

with open('all_spotify_tracks.csv', 'w',encoding='utf8', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_song)


with open('all_spotify_tracks.pickle', 'wb') as handle:
    pickle.dump(list_song, handle, protocol=pickle.HIGHEST_PROTOCOL)

