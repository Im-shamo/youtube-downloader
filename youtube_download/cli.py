from videos_download import VideosDownload
from utility import *
from pytube import YouTube, Playlist, exceptions
from os import path, mkdir
from typing import Optional


def video_cli(
        urls: list[str],
        ouput_path: str,
        verbose: bool,
        high_res: bool = False,
        high_audio: bool = False,
        itag: Optional[int] = None
) -> None:

    ouput_path = path.abspath(ouput_path)
    if not path.exists(ouput_path):
        raise FileNotFoundError

    while True:
        try:
            videos = [YouTube(link) for link in urls]
            break
        except Exception as e:
            if verbose:
                print(e)

    if verbose:
        print_videos_details(videos=videos)

    download = VideosDownload(videos, ouput_path)
    if high_res:
        download.highest_resolution()
    elif high_audio:
        download.audio_only()
    elif itag:
        download.itag(itag)

    if verbose:
        download.print_streams_filesize()
    download.download(print_info=verbose)


def playlist_cli(
        urls: list[str],
        output_path: str,
        verbose: bool,
        create_dir: bool = False,
        high_res: bool = False,
        high_audio: bool = False,
        itag: Optional[int] = None
) -> None:

    output_path = path.abspath(output_path)
    if not path.isdir(output_path):
        raise FileNotFoundError



    while True:
        try:
            playlists = [Playlist(link) for link in urls]
            break

        except Exception as e:
            print(e)


    if verbose:
        print_playlists_details(playlists=playlists)

    if create_dir:
        base_dir = output_path

    for playlist in playlists:
        if create_dir:
            title = playlist.title
            output_path = path.join(base_dir, title)
            mkdir(output_path)
            print(f"Created directory: {output_path}")

        videos = playlist.videos
        if verbose:
            print_videos_details(videos=videos)
        download = VideosDownload(videos, output_path)
        if high_res:
            download.highest_resolution()
        elif high_audio:
            download.audio_only()
        elif itag:
            download.itag(itag)

        if verbose:
            download.print_streams_filesize()
        download.download(verbose)


def print_videos_details(
        urls: Optional[list[str]] = None,
        videos: Optional[list[YouTube]] = None,
) -> None:

    if urls:
        try:
            videos = [YouTube(url) for url in urls]

        except Exception as e:
            print(e)

    output_text = ""
    for i, video in enumerate(videos):
        author = video.author[:15] + \
            "..." if len(video.author) > 15 else video.author
        title = video.title
        length = seconds_to_min(video.length)
        num = str(i+1)

        output_text += f"{num:<4} | Author: {author:<15} | Length: {length:^5} | Video title: {title}\n"

    print(output_text)


def print_playlists_details(
    urls: Optional[list[str]] = None,
    playlists: Optional[list[Playlist]] = None,
    print_videos: bool = False,
) -> None:

    if urls:
        videos = [YouTube(url) for url in urls]
    [print(f"{i+1} | Playlist title: {playlist.title:<40} | No. vidoes: {playlist.length}")
     for i, playlist in enumerate(playlists)]

    if print_videos:
        for playlist in playlists:
            videos = playlist.videos
            print_videos_details(videos=videos)
            print("\n")
