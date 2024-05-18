from pytube import YouTube
from videos_download import VideosDownload
from user_input import *


def shamo_videos(videos=None, verbose=False):

    while not (videos):
        try:
            videos = [YouTube(videos) for videos in get_links()]
            break

        except Exception as e:
            print(e)

    download_dir = get_download_dir()

    # [print(f"{i+1:^4} | Author: {video.author:.20} | Video title: {video.title:<40} | Length: {seconds_to_min(video.length)}")
    #  for i, video in enumerate(videos)]

    output_text = ""
    for i, video in enumerate(videos):
        author = video.author[:10] + \
            "..." if len(video.author) > 10 else video.author
        title = video.title
        length = seconds_to_min(video.length)
        num = str(i+1)

        output_text += f"{num:<4} | Author: {author:<15} | Length: {length:^5} | Video title: {title}\n"

    print(output_text)

    selected_videos = get_selection(videos)
    
    download = VideosDownload(selected_videos, download_dir)
    
    get_streams_mode(download)

    download.print_streams_filesize()
    download.download(print_info=True)
    
def get_streams_mode(download: VideosDownload):
    
    GET_STREAMS_MODE = {
        "Highest Resolution": download.highest_resolution,
        "Best Audio": download.best_audio_only,
        "Filter": get_filter_mode,
    }

    mode = mode_select(GET_STREAMS_MODE)   

    if mode == "Filter":
        GET_STREAMS_MODE["Filter"](download)
    else:
        GET_STREAMS_MODE[mode]()

def get_filter_mode(download: VideosDownload):
    
    GET_FILTER_MODE = {
        "Video only": download.filter_video_only,
        "Audio only": download.filter_audio_only,
        "Adaptive": download.filter_adaptive_only,
    }

    GET_FILTER_MODE[mode_select(GET_FILTER_MODE)]()
    download.print_stream_info()
    itag = get_num("Enter itag")
    download.by_itag(itag)


    
    
    

if __name__ == "__main__":
    shamo_videos()
