#!/usr/bin/env python
# coding: utf-8

# In[78]:


import requests
import json

SONG_URL = 'https://api.lyrics.ovh/v1/{}/{}'

def get_lyrics (artist, title):
    URL = SONG_URL.format(artist,title)
    r= requests.get(URL)
    data= json.loads(r.text)
    try:
        song= data['lyrics']
    except TypeError:
        pass
    return song


# In[80]:


artist= 'Beyoncè'
title='Halo'

song= get_lyrics(artist,title)

print('{} by {}:'.format(artist,title) )
print("{}".format(song))


# In[ ]:




