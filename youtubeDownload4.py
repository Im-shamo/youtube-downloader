from pytube import YouTube, Playlist
import os

#test

def mode_select(modes: dict) -> str:
    
    question = f"\nPlease select mode (1 - {len(modes)})"
    for i, name in enumerate(modes):
        question += f"\n({i + 1}) {name}"

    question += "\n(-1) Quit\n>"

    while True:

        try:
            mode = int(input(question))

            if mode == -1:
                quit()

            elif mode >= 1 and mode <= len(modes):
                return list(modes)[mode-1]

        except ValueError:
            print("\nMode not found. Please try again")

def seconds_to_min(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"


def get_input(question, default=None):

    if default is not None:
        question += f". Default is {str(default)}"

    question = "\n" + question + "\n>"
    while True:

        answer = input(question)
        if answer:
            return answer

        if default is not None:
            return default

def get_confirm(question, default=None):

    question += " [y/n]"

    while True:
        answer = get_input(question, default)

        if answer.lower().strip() in ["yes", "y"]:
            return True

        elif answer.lower().strip() in ["no", "n"]:
            return False

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

def get_videos_modes(videos, download_dir):
    MODES = {
        "By itag": download_by_itag,
        "Highest progressive resolution": download_highest_resolution,
    }

    MODES[mode_select(MODES)](videos, download_dir)

def download_highest_resolution(videos: list, download_dir: str):

    streams = [video.streams.get_highest_resolution() for video in videos]
    download_streams(streams, download_dir)


def download_by_itag(videos: list, download_dir: str):

    [print_stream_data(video) for video in videos]

    itag = int(get_input("Enter itag"))

    streams = [video.streams.get_by_itag(itag) for video in videos]
    download_streams(streams, download_dir)


def download_streams(streams: list, download_dir: str):

    failed_downloads = []
    if get_confirm("Download videos?"):

        for i , stream in enumerate(streams):
            print(f"\n{i+1}: Downloading {stream.title}")

            try:
                stream.download(download_dir)
                print(f"{i+1}: Downloaded {stream.title}")
            
            except Exception as e:
                print(f"{i+1}: Failed to download {stream.title}. Error {e}")
                failed_downloads.append(stream)

        if failed_downloads and get_confirm("Retry download", "n"):
            download_streams(failed_downloads, download_dir)


    else:
        print("Fail to Download")
    

def print_stream_data(video):

    print("\n",video.title)
    [print(line) for line in video.streams]


def shamo_videos(videos = None|list):

    while not(videos):
        try:
            videos = [YouTube(videos) for videos in get_links()]
            break

        except Exception as e:
            print(e)

    download_dir = get_download_dir()

    [print(f"{i+1} | Author: {video.author:<40} | Video title: {video.title:<40} | Length: {seconds_to_min(video.length)}")
    for i, video in enumerate(videos)]

    get_videos_modes(videos, download_dir)


def shamo_playlist():
    while True:
        try:
            playlists = [Playlist(videos) for videos in get_links()]

        except Exception as e:
            print(e)


    

def main():

    MODES = {
        "Videos": shamo_videos,
        "Playlist": shamo_playlist
    }

    MODES[mode_select(MODES)]()

if __name__ == "__main__":
    main()