
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


cid = "3834026abc8f4c4ca4649552cada0b8f"
secret = "c37ea7694e024e808e759263ca65b7b9"

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])