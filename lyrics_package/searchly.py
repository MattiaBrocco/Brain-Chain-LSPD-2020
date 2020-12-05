import json
import requests
import pandas as pd


def similarity(artist, title):
    """
    With this function we will obtain similar songs to the one
    we have searched for. The user input that will start the function
    are the artist name and the title of the song he are looking for.
    """

    artist = artist.replace("_", " ")
    title = title.replace("_", " ")

    song = title
    url = 'https://searchly.asuarez.dev/api/v1/song/search'

    # Make the classify request
    response = requests.get(url, params={'query': song})

    # The response is formatted in JSON
    data = json.loads(response.text)
    if data["error"] is True:
        return "Error in the call to SearchLy"
        """
        Here, if the result is True, there will be an error in
        the use of the API. Otherwise, if the response is smaller than 1,
        this means the request is successful but the user will not
        receive the list of similar songs.
        If the response is bigger than 1, the user will not get the list
        of songs similar to the one he has looking for but the function
        will provide the user with some best suggestions.
        If the response is equal to 1, the user will get the right song!
        """

    else:
        if len(data["response"]["results"]) < 1:
            # This is the case when the request is successful, but empty
            return "Similar songs not found"
        elif len(data["response"]["results"]) > 1:
            # If more than one result is found, we must let
            # the user choose what to do by showing all the found results
            print("We couldn't find songs similar to your search,",
                  "our best suggestions are:", sep="\n", end="\n\n")
            df_res = pd.DataFrame({"--------------------------------":
                                   [x["name"] for x in
                                    data["response"]["results"]]})
            return df_res.head(5)
        else:
            # If only one result is found, with a certain degree
            # of confidence, this is the right song!
            song_id = data["response"]["results"][0]["id"]

            # The API that looks for similar songs works with a song ID,
            # retrieved the previous line of code
            sim_url = 'https://searchly.asuarez.dev/api/v1/similarity/by_song'
            sim_payload = {'song_id': song_id}

            sim_response = requests.get(sim_url, params=sim_payload)

            sim_data = json.loads(sim_response.text)
            print("Listen to similar songs:\n")

            df = pd.DataFrame({"Title": [x["song_name"]
                                         for x in
                                         sim_data["response"]
                                         ["similarity_list"]],
                               "Artist": [x["artist_name"]
                                          for x in
                                          sim_data["response"]
                                          ["similarity_list"]],
                               "Similarity": [x["percentage"]
                                              for x in
                                              sim_data["response"]
                                              ["similarity_list"]]})
            """
            Here we have created a dataframe which will display the title
            of the similar song, the artist and the similarity
            percentage of that song.
            """

            return df.head(5)
