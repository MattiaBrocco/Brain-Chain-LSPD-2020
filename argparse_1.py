import sys
import argparse
from Lyrics import get_lyric
from SearchLy import similarity
from Songsterr import artists_songs

def parsing_input():
    #Parsing the input for our program.
    #This function requires two positional arguments
    
    parser = argparse.ArgumentParser()
    #positional arguments
    parser.add_argument("artist", help='the arstist of song you are searching for')
    parser.add_argument("title", help='the title of the song you are searching for')
    
    #optional arguments
    parser.add_argument("-verbosity",
                        help='increases verbosity of the program',
                        action="store_true") # if the user doesn't input "-v" then verbosity is False
    args = parser.parse_args()
    return args

# ------------------------------------
# LYRICS
#try:
args= parsing_input()
song_l = get_lyric(args.artist, args.title)


if args.verbosity: # verbosity = False
    print("This is {} by {}:".format(args.title, args.artist))
    print("{}\n\n".format(song_l))
else:
    print("{}\n\n".format(song_l))

#except:
if len(sys.argv)>4:
    print("Use underscores (_) instead of spaces")

# ------------------------------------
# SONGSTERR
song_t = artists_songs(args.artist, args.title)

if args.verbosity: # verbosity = False
    print("Link to tabs:{}\n\n".format(song_t[0]))
    print("Some songs from *{}* you might be interested in:".format(args.artist.capitalize()))
    print(song_t[1],"\n\n")
else:
    print("Link to tabs:{}\n\n".format(song_t[0]))

# ------------------------------------
# SEARCHLY
sim_song = similarity(args.artist, args.title)

print("{}".format(sim_song))


