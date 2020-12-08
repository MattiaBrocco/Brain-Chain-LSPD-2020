# Brain-Chain-LSPD-2020 :brain:

We welcome you to our repository “Brain Chain”. :wave:

With this repository, selecting a song title and its artist, you will be able to:
1) Get the lyrics of that song (API: [*lyrics.ovh*](https://lyrics.ovh));
2) Find out the link of the music sheet of that song of it is present (API: [*songsterr.com*](https://www.songsterr.com)) ;
3) Search for songs similar to the one selected by us (API: [*SearchLy.com*](http://www.searchly.com)) ;
4) Search for other songs by the same artist (API: [*songsterr.com*](https://www.songsterr.com)).

To reach our goal we will use some new public available APIs.

In this repository you can find a file named ```main.py```

If you run the program, executing the main file with: ```$ python main.py oasis wonderwall -history -v``` it will  give you results similar to the following: 

```
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

Link to tabs:http://www.songsterr.com/a/wa/bestMatchForQueryString?s=wonderwall&a=oasis

Listen to similar songs:

                      Title                Artist  Similarity
0  don't know what it means  tedeschi trucks band       95.08
1             father to son         collins, phil       94.87
2     first comes the night          isaak, chris       94.78
3    the walls of the world           katie melua       94.65
4                lights out           angel olsen       94.55
```
> **Note:** the project requires the following modules to run: *argparse*, *os*, *pandas*, *requests*, *json*, *unittest*, *coverage*, *pytest*, *sys*, *csv*, *collections*, *datetime*.


## COMMAND LINE PARAMETERS :computer:
 
Some command line parameters are required in order to run the main script.

Positional arguments:
- **"Artist"** of the song you are searching for.
- **"Title"** of the song you are searching for.
 
Optional argument:
- **-v:** be more verbose. Some modules also include verbosity. There is **one level** of verbosity in this first release.
- **-history:** it will let you get the history of the latest searches of users who have used the program before you.


Thanks for your attention!

Team Brain Chain :brain:

## AUTHORS :man_technologist::woman_technologist:

- [**Mattia Brocco**](https://www.linkedin.com/in/mattia-brocco-digital-student/)
- [**Anna Costa**](https://www.linkedin.com/in/annacosta99/)
- [**Alessandra Cancellari**](https://www.linkedin.com/in/alessandracancellari/)
- [**Eleonora Sartori**](https://www.linkedin.com/in/eleonorasartori97/)




