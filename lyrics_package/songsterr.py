import json
import requests
import pandas as pd


def artists_songs(artist, title):
    """
    The function artists_songs is based on the user input.
    Once the user will choose the song he wants to listen and
    the artist of the song, these inputs will be the variable
    that will be inserted in the API to get the output.
    In this case, the output will be the URL of the song sheet
    and a dataframe containing other five songs of the same artist.
    """
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
    artist = artist.replace("_", " ")
    title = title.replace("_", " ")

    urlss = "http://www.songsterr.com/a/ra/songs.json?pattern={}"
    urlss_f = urlss.format(artist)
    reqss = requests.get(urlss_f)
    datass = json.loads(reqss.text)

    if len(datass) == 0:
        return "Songsterr couldn't find any tabs for this song"
    else:
        tabs_0 = "http://www.songsterr.com/a/wa/"
        tabs_1 = "bestMatchForQueryString?s={}&a={}"
        # Whitespaces are replaced with "%20" as required
        # by the API in order to make the link exploitable
        url_format = tabs_0 + tabs_1.format(title.replace(" ", "%20"),
                                            artist.replace(" ", "%20"))
        """
        In Songsterr, "datass" contains all the songs of the artist
        the user is searching for. We will search in datass the id of
        the artist in order to find the songs.
        "nl" is a list of tuples which has the name of the artist as
        the first element, and it has the types of song sheets as second
        element. This let the user obtain as output only the other five
        songs of the artist which have the songs sheets in Songsterr.
        The list of songs will be displayed in a dataframe.
        """
        nl = []
        for x in datass:
            if x["chordsPresent"] is True:
                nl += [(x["title"], len(x["tabTypes"]))]

        nl.sort(key=lambda x: x[1], reverse=True)
        df = pd.DataFrame({"-----------------\
        ---------------": [x[0] for x in nl[:5]]})
        return (url_format, df)
