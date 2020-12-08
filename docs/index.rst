.. "Brain Chain Project" documentation master file, created by
   sphinx-quickstart on Mon Dec  7 22:31:40 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to "Brain Chain Project"'s documentation!
=================================================

We welcome you to our repository “Brain Chain”.

With this repository, selecting a song title and its artist, you will be able to:

1) Get the lyrics of that song (API: *lyrics.ovh* <https://lyrics.ovh> );

2) Find out the link of the music sheet of that song of it is present (API: *songsterr.com* <https://www.songsterr.com> ) ;

3) Search for songs similar to the one selected by us (API: *SearchLy.com* <http://www.searchly.com> ) ;

4) Search for other songs by the same artist (API: *songsterr.com* <https://www.songsterr.com> ).

To reach our goal we will use some new public available APIs.

In this repository you can find a file named ``main.py``

If you run the program, executing the main file with: ``$ python main.py oasis wonderwall -history -v`` it will  give you results similar to the following: 



$ python main.py oasis wonderwall -history -v

Most searched songs
 ---------------- ----------------
0        lady gaga        paparazzi
1            oasis       wonderwall


Today is gonna be the day
That they're gonna throw it back to you
By now you should've somehow
Realized what you gotta do
I don't believe that anybody
Feels the way I do about you now [...]

Link to tabs: <http://www.songsterr.com/a/wa/bestMatchForQueryString?s=wonderwall&a=oasis>

Listen to similar songs:

                    Title                  Artist  Similarity
0  don't know what it means  tedeschi trucks band       95.08
1             father to son         collins, phil       94.87
2     first comes the night          isaak, chris       94.78
3    the walls of the world           katie melua       94.65
4                lights out           angel olsen       94.55

 **Note:** the project requires the following modules to run: *argparse*, *os*, *pandas*, *requests*, *json*, *unittest*, *coverage*, *pytest*, *sys*, *csv*, *collections*, *datetime*.

In this repository there is also a folder named ``lyrics_package``

In this folder you can find the following list of files:
1) ```lyrics.py```
2) ```searchly.py```
3) ```songsterr.py```

Each one of the above files contains the code of the implementation of an API (precisely lyrics.ovh, SearchLy and Songsterr).

- In the ```lyrics.py``` file, we exploited the lyrics.ovh API with the aim of developing a function which, given the song author and title, would be able to return the lyrics of the song.

- In the ```searchly.py``` file, we have used the SearchLy API. With the function _similarity_ the user will obtain similar songs to the one he has searched for. The user input that will start the function are the artist name and the title of the song he are looking for.
If the API doesn't return an error, the function controls the lenght of the results of the response which is in JSON format and it returns a table with the best suggestions for the user or the right song. 

- In the ```songsterr.py``` file, we have exploited the Songsterr API. With the function _artists_songs_ the user will obtain as output the URL of the song sheet of the song they are looking for and a dataframe containing other five songs of the same artist. We will search the songs in Songsterr using the id of the searched artist. The user input that will start the function are the artist name and the title of the song they are looking for.


## COMMAND LINE PARAMETERS
 
Some command line parameters are required in order to run the main script.

Positional arguments:
- **"Artist"** of the song you are searching for.
- **"Title"** of the song you are searching for.
 
Optional argument:
- **-v:** be more verbose. Some modules also include verbosity. There is **one level** of verbosity in this first release.
- **-history:** it will let you get the history of the latest searches of users who have used the program before you.


Thanks for your attention!

Team Brain Chain
