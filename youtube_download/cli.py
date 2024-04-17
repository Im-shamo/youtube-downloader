from videos_download import VideosDownload
from utility import *
from pytube import YouTube, Playlist, exceptions
from os import path


def video_cli(
        url: list[str],
        ouput_path: str,
        verbose: bool,
        **options
) -> None:

    ouput_path = path.abspath(ouput_path)
    if not path.exists(ouput_path):
        raise FileNotFoundError

    while True:
        try:
            videos = [YouTube(url) for url in url]
            break
        except Exception as e:
            if verbose:
                print(e)

    if verbose:
        output_text = ""
        for i, video in enumerate(videos):
            author = video.author[:10] + \
                "..." if len(video.author) > 10 else video.author
            title = video.title
            length = seconds_to_min(video.length)
            num = str(i+1)

            output_text += f"{num:<4} | Author: {author:<15} | Length: {length:^5} | Video title: {title}\n"

        print(output_text)

    download = VideosDownload(videos, ouput_path)
    if options["high_res"]:
        download.highest_resolution()
    elif options["high_audio"]:
        download.audio_only()
    elif options["itag"]:
        download.itag(options["itag"])

    if verbose:
        download.print_streams_filesize()
    download.download(print_info=verbose)


def playlist_cli() -> None:
    pass
