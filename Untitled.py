#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
import json

GENRE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'

def get_genre (artist, title):
    URL = GENRE_URL.format(artist,title)
    r= requests.get(URL)
    data= json.loads(r.text)
    try:
        genre= data['genre']
    except TypeError:
        pass
    return get_genre


# In[32]:


artist= 'Metallica'
title='Fade to Black'

genre= get_genre(artist,title)

print('{} by {}:'.format(artist,title) )
print(genre)


# In[ ]:




