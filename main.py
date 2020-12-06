import os
import sys
import argparse
from lyrics_package import lyrics
from lyrics_package import history
from lyrics_package import searchly
from lyrics_package import songsterr


def parsing_input():
    # Parsing the input for our program.
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
                        action="store_true")
    # if the user doesn't input "-v" then verbosity is False
    parser.add_argument("-history", help="Show most searched songs",
                        action="store_true")
    # if the user doesn't input "-v" then verbosity is False
    args = parser.parse_args()
    return args


try:
    args = parsing_input()

    # Initial input check
    if args.history and args.v and len(sys.argv) > 5:
        print("**Use underscores (_) instead of spaces**")
        sys.exit()
    elif args.history and not args.v and len(sys.argv) > 4:
        print("**Use underscores (_) instead of spaces**")
        sys.exit()
    elif not args.history and args.v and len(sys.argv) > 4:
        print("**Use underscores (_) instead of spaces**")
        sys.exit()
    elif not args.history and not args.v and len(sys.argv) > 3:
        print("**Use underscores (_) instead of spaces**")
        sys.exit()

    # --------------------------------
    # Search history
    hist = history.create_hist(args.artist, args.title,
                               os.getcwd() + r"\lyrics_package\history.csv")
    if args.history:
        print("Most searched songs")
        print(hist)

    # --------------------------------
    # LYRICS
    song_l = lyrics.get_lyric(args.artist, args.title)

    if args.v:  # verbosity = False
        print("\n\nThis is {} by {}:".format(args.title, args.artist))
        print("\n\n{}\n\n".format(song_l))
    else:
        print("\n\n{}\n\n".format(song_l))

    # --------------------------------
    # SONGSTERR
    song_t = songsterr.artists_songs(args.artist, args.title)

    if args.v:  # verbosity = False
        print("Link to tabs:{}\n\n".format(song_t[0]))
        print("Some songs from *{}* you might be interested in:"
              .format(args.artist.capitalize()))
        print(song_t[1], "\n\n")
    else:
        print("Link to tabs:{}\n\n".format(song_t[0]))

    # --------------------------------
    # SEARCHLY
    sim_song = searchly.similarity(args.artist, args.title)
    print("{}".format(sim_song))

except ValueError:
    # ValueError includes the JSONDecodeError,
    # which sometimes arises from API calls
    print("Something wrong, please retry")
    sys.exit()

except PermissionError:
    print("Close the history.csv file before running the program!")

except ConnectionError:
    print("Bad conncetion error!")
