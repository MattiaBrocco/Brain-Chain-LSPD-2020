import sys
import argparse
from lyrics_package import Lyrics
from lyrics_package import SearchLy
from lyrics_package import Songsterr


def parsing_input():


# Parsing the input for our program
# This function requires two positional arguments
    parser = argparse.ArgumentParser()

# positional arguments
    parser.add_argument("artist",
                        help='the arstist of song you are searching for')
    parser.add_argument("title",
                        help='the title of the song you are searching for')

# optional arguments
    parser.add_argument("-v",
                        help='increases verbosity of the program',
                        action="store_true")  # if the user doesn't
    # input "-v" then verbosity is False
    args = parser.parse_args()
    return args

# ------------------------------------
# LYRICS

try:
    args = parsing_input()
    song_l = Lyrics.get_lyric(args.artist, args.title)

    if len(sys.argv) > 4:
        print("**Use underscores (_) instead of spaces**")
        sys.exit()

    if args.v:  # verbosity = False
        print("This is {} by {}:".format(args.title, args.artist))
        print("{}\n\n".format(song_l))
    else:
        print("{}\n\n".format(song_l))

# ------------------------------------
# SONGSTERR
    song_t = Songsterr.artists_songs(args.artist, args.title)

    if args.v:  # verbosity = False
        print("Link to tabs:{}\n\n".format(song_t[0]))
        print("Some songs from *{}* you might be interested in:"
              .format(args.artist.capitalize()))
        print(song_t[1], "\n\n")
    else:
        print("Link to tabs:{}\n\n".format(song_t[0]))

# ------------------------------------
# SEARCHLY
    sim_song = SearchLy.similarity(args.artist, args.title)

    print("{}".format(sim_song))

except ValueError:
    # ValueError includes the JSONDecodeError,
    # which sometimes arises from API calls
    print("Something wrong, please retry")
    sys.exit()
