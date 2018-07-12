import math
import scraping
import spotify_api
import spotipy
import sys

if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_name = sys.argv[2]
    apple_url = sys.argv[3]
else:
    print "Usage: %s username playlist_id track_id ..." % (sys.argv[0],)
    sys.exit()


song_list = scraping.scrape(apple_url)

# for song in song_list:
# 	print song

token = spotify_api.authenticate(username)

tracks = []
failed = []

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    new_playlist = sp.user_playlist_create(username, playlist_name, public=False)
    if new_playlist:
    	playlist_id = new_playlist['id']
    	for song in song_list:
    		artist = spotify_api.fixArtists(song['artist'])
    		name = spotify_api.fixRemixes(song['name'])
    		query = name + ' ' + artist
    		result =  sp.search(query, limit=1, offset=0, type='track', market=None)
    		try:
    			song_id = result['tracks']['items'][0]['id']
    			tracks.append(song_id)
    		except:
    			failed.append(name)
	results = sp.user_playlist_add_tracks(username, playlist_id, tracks)
else:
    print "Can't get token for", username
print len(tracks)
