from pytube import YouTube
from videos_download import VidosDownload
from user_input import *



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