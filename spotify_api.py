import spotipy
import spotipy.util as util
import os
spotify = spotipy.Spotify()

#username = '12148372648'
scope = 'playlist-modify-private playlist-modify-public'
uri = 'http://localhost/'
client_id=os.environ['SPOTIPY_CLIENT_ID']
client_secret=os.environ['SPOTIPY_CLIENT_SECRET']

def fixArtists(text):
	new_text=''
	words = text.split(' ')
	if 'featuring' in words:
		for word in words:
			if(word!='featuring'):
				new_text = new_text + ' ' + word
			else:
				break;
	if(new_text!=''):
		return new_text
	else:
		return text

def fixRemixes(text):
	new_text=''
	words = text.split(' ')
	for word in words:
		if(word[0]!='('):
			new_text = new_text + ' ' + word
		else:
			break;
	if(new_text!=''):
		return new_text
	else:
		return text

def authenticate(username):
	token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=uri)
	return token