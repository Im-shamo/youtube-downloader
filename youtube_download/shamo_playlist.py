from pytube import Playlist
from user_input import *



def shamo_playlist():

    while True:
        try:
            playlists = [Playlist(videos) for videos in get_links()]
            break

        except Exception as e:
            print(e)

    [print(f"{i+1} | Author: {playlist.author:<20} | Playlist title: {playlist.title:<40}")
     for i, playlist in enumerate(playlists)]