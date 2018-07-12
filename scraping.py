import requests
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def scrape(website):
	page = requests.get(website)
	soup = BeautifulSoup(page.content, 'html.parser')
	html_song_list = soup.body.find_all('span', attrs={'class':'tracklist-item__text__headline'})
	html_artist_list = soup.body.find_all('a', attrs={'class':'table__row__link--secondary'})

	song_list = [];

	for song in html_song_list:
		name = song.text[:-1]
		name = name[2:]
		songDict = {"name": name}
		song_list.append(songDict)

	index = 0
	for artist in html_artist_list:
		songDict = song_list[index]
		songDict["artist"] = artist.text
		song_list[index] = songDict
		index= index +1
	return song_list

