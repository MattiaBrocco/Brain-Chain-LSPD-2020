import requests
import json


def get_lyric(artist, title):
    
    song_url = 'https://api.lyrics.ovh/v1/{}/{}'

    url = song_url.format(artist, title)

    lyrics_req = requests.get(url)
    data = json.loads(lyrics_req.text)

    try:
        song = data['lyrics']
        if len(song) == 0:
            print("This song was not found")
        else:
            print("{} by {}:".format(title, artist))
            print("{}".format(song))
    except TypeError:
        pass

    return song