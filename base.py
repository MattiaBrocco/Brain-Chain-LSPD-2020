import requests
import json

SONG_URL = 'https://api.lyrics.ovh/v1/{}/{}'

def get_lyric(artist, title):

    URL = SONG_URL.format(artist, title)

    r = requests.get(URL)
    data = json.loads(r.text)

    try:
        song = data['lyrics']
    except TypeError:
        pass

    return r.text