from exceptions import *
from videos_download import VidosDownload
from utility import *
from user_input import *

from pytube import YouTube, Playlist
import os

# handles user inputs


def get_download_dir():

    while True:
        download_dir = get_input(
            "Enter download directory",
            os.path.join(os.path.expanduser("~"), "Videos")
        )
        # implemant path checking
        print(f"saving to {download_dir}")

        if get_confirm("Confirm location", "y"):

            return download_dir


def get_links():
    links = get_input("Enter links sperated by space")
    return links.split()


def shamo_videos(videos=None):

    while not (videos):
        try:
            videos = [YouTube(videos) for videos in get_links()]
            break

        except Exception as e:
            print(e)

    download_dir = get_download_dir()

    [print(f"{i+1} | Author: {video.author:<20} | Video title: {video.title:<40} | Length: {seconds_to_min(video.length)}")
     for i, video in enumerate(videos)]

    selected_videos = get_selection(videos)

    download = VidosDownload(selected_videos, download_dir)
    download.filters_prompt()

    if download.filtered:
        download.print_stream_qs()

    download.get_streams_prompt()
    download.print_streams_filesize()
    download.get_download_prompt()


def shamo_playlist():

    while True:
        try:
            playlists = [Playlist(videos) for videos in get_links()]
            break

        except Exception as e:
            print(e)

    [print(f"{i+1} | Author: {playlist.author:<20} | Playlist title: {playlist.title:<40}")
     for i, playlist in enumerate(playlists)]


def main():

    MODES = {
        "Videos": shamo_videos,
        "Playlist": shamo_playlist
    }

    MODES[mode_select(MODES)]()

if __name__ == "__main__":
    main()
