import requests
import json


def artists_songs(artist, title):
    urlss = "http://www.songsterr.com/a/ra/songs.json?pattern={}"
    urlss_f = urlss.format(artist)
    reqss = requests.get(urlss_f)
    datass = json.loads(reqss.text)
    
    if len(datass) == 0:
        print("Artist not found")
    else:
        tabs_url = "http://www.songsterr.com/a/wa/bestMatchForQueryString?s={}&a={}"
        # Whitespaces are replaced with "%20" as required by the API
        # in order to make the link exploitable
        url_format =  tabs_url.format(title.replace(" ", "%20"), artist.replace(" ", "%20"))
        print("Link to tabs:", url_format,"\n\n")
        print("Some songs from *{}* you might be interested in".format(artist))
        nl = [(x["title"], len(x["tabTypes"]))
              for x in datass if x["chordsPresent"] == True]
        nl.sort(key = lambda x:x[1], reverse = True)
        for x in nl[:10]:
            print(x[0])
    return None