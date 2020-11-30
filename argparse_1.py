import sys
import argparse
from Lyrics import get_lyric

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
                        action="store_false")
    args = parser.parse_args()
    return args


# the following code gives the value of the stock price of the input companies

#try:
args= parsing_input()
song_l = get_lyric(args.artist, args.title)


if args.verbosity is False: # verbosity = False
    print("{}".format(song_l))
else:
    print("This is {} by {}:".format(args.title, args.artist))
    print("{}".format(song_l))
    
    
#this code helps the user to check if he wrote correctly the inputs

#except:
if len(sys.argv)>4:
    print("Use underscores (_) instead of spaces")





