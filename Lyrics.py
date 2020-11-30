import requests
import json


def get_lyric(artist, title):
    
    artist=artist.replace("_"," ")
    title=title.replace("_"," ")
    
    song_url = 'https://api.lyrics.ovh/v1/{}/{}'

    url = song_url.format(artist, title)

    lyrics_req = requests.get(url)
    data = json.loads(lyrics_req.text)

    try:
        song = data['lyrics']
        if len(song) == 0:
            return "This song is not found"
        else:
            return song
    