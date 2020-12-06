import requests
import json


def get_lyric(artist, title):
<<<<<<< HEAD
    
    if type(artist) != str or type(title) != str:
        raise AttributeError("Invalid input type")
    
    blacklist = ["\n", "\t", "\\"]
    for bl in blacklist:
        if bl in artist or bl in title:
            raise Exception("Invalid character: ", bl)
    """
    This first block came from testing on
    valid/invalid and edge cases.
    """
       
    artist = artist.replace("_"," ")
    title = title.replace("_"," ")
    
=======
    """
    With this function we will obtain the lyrics of the song the user
    has searched for. The user input that will start the function
    are the artist name and the title of the song he are looking for.
    """

    artist = artist.replace("_", " ")
    title = title.replace("_", " ")

>>>>>>> origin/docstrings2
    song_url = 'https://api.lyrics.ovh/v1/{}/{}'

    url = song_url.format(artist, title)

    lyrics_req = requests.get(url)
    data = json.loads(lyrics_req.text)

    song = data['lyrics']
    if len(song) == 0:
        return "Lyrics of this song were not found"
    else:
        return song
