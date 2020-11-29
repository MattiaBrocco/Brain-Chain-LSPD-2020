from base import get_lyric

artist = "Beatles"
title= "Across the Universe"

song = get_lyric(artist, title)

print("{} by {}:".format(title, artist))
print("{}".format(song))