import requests
import json


def get_lyric(artist, title):
    """
    With this function we will obtain the lyrics of the song the user
    has searched for. The user input that will start the function
    are the artist name and the title of the song he are looking for.
    """

    artist = artist.replace("_", " ")
    title = title.replace("_", " ")

    song_url = 'https://api.lyrics.ovh/v1/{}/{}'

    url = song_url.format(artist, title)

    lyrics_req = requests.get(url)
    data = json.loads(lyrics_req.text)

    song = data['lyrics']
    if len(song) == 0:
        return "Lyrics of this song were not found"
    else:
        return song
