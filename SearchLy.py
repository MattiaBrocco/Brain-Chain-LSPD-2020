#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests


# In[25]:


def similarity(artist, title):
    song = title
    url = 'https://searchly.asuarez.dev/api/v1/song/search'

    # Make the classify request
    response = requests.get(url, params = {'query': song})

    # The response is formatted in JSON
    data = json.loads(response.text)
    if data["error"] == True:
        print("Error in the request")
    else:
        if len(data["response"]["results"]) < 1:
            # This is the case when the request is successful, but empty
            print("Similars song not found")
        elif len(data["response"]["results"]) > 1:
            # If more than one result is found, we must let
            # the user choose what to do by showing all the found results
            print("We couldn't find songs similar to your search,",
                  "our suggestions are:", sep="\n", end = "\n\n" )
            for x in data["response"]["results"]:
                print( x["name"] )
        else:
            # If only one result is found, with a certain degree
            # of confidence, this is the right song!
            song_id = data["response"]["results"][0]["id"]
            
            # The API that looks for similar songs works with a song ID,
            # retrieved the previous line of code
            sim_url = 'https://searchly.asuarez.dev/api/v1/similarity/by_song'
            sim_payload = {'song_id': song_id}

            sim_response = requests.get(sim_url, params = sim_payload)

            sim_data = json.loads(sim_response.text)
            print("Listen to similar songs:")
            for x in sim_data["response"]["similarity_list"]:
                print("Title:", x["song_name"],"| Artist:", x["artist_name"],
                      " | Similarity: ", x["percentage"],"%")
    return True


# In[27]:


sid = similarity("chris webby", "paparazzi")


# In[ ]:




