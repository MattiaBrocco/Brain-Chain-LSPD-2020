## List of APIs and codes of their implementation

In this folder you can find the following list of files:
1) ```lyrics.py```
2) ```searchly.py```
3) ```songsterr.py```

Each one of the above files contains the code of the implementation of an API (precisely lyrics.ovh, SearchLy and Songsterr).

- In the ```lyrics.py``` file, we exploited the lyrics.ovh API with the aim of developing a function which, given the song author and title, would be able to return the lyrics of the song.

- In the ```searchly.py``` file, we have used the SearchLy API. With the function _similarity_ the user will obtain similar songs to the one he has searched for. The user input that will start the function are the artist name and the title of the song he are looking for.
If the API doesn't return an error, the function controls the lenght of the results of the response which is in JSON format and it returns a table with the best suggestions for the user or the right song. 

- In the ```songsterr.py``` file, we have exploited the Songsterr API. With the function _artists_songs_ the user will obtain as output the URL of the song sheet of the song they are looking for and a dataframe containing other five songs of the same artist. We will search the songs in Songsterr using the id of the searched artist. The user input that will start the function are the artist name and the title of the song they are looking for.



