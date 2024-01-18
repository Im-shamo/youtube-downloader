from pytube import YouTube, Playlist
import os




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


def check_num_range(n, start, end):
    if start <= n and end >= n:
        return True
    else:
        return False

# handles user inputs


def get_input(question, default=None):

    if default is not None:
        question += f". Default is {str(default)}."

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


def get_selection(number_of_things, array) -> list:

    selection = []
    answer = get_input("Enter selection (1-10 5)",
                       default="all").lower().strip()

    if answer == "all":
        return array

    answer = answer.split()

    print(answer)

    for x in answer:
        try:
            if len(x.split("-")) == 2:

                start, end = x.split("-")

                start = int(start)
                end = int(end)

                if (start < end and check_num_range(start, 1, number_of_things) and
                check_num_range(end, 1, number_of_things)):

                    selection.extend([elem for elem in array[start-1:end] if elem not in selection])

            elif x.isdigit():

                n = int(x)

                if check_num_range(n, 1, number_of_things):
                    if not array[n-1] in selection:
                        selection.append(array[n-1])

        except ValueError:
            pass

    return selection


# handles downloading

def get_videos_modes():
    MODES = {
        "Highest progressive video": download_highest_resolution,
        "By itag": download_by_itag,
        "Filter Audio": filter_audio,
        "Filter Video": filter_video,
        "Filter Adaptive": filter_adaptive
    }

    return MODES[mode_select(MODES)]


def download_highest_resolution(videos: list, download_dir: str):

    streams = [video.streams.get_highest_resolution() for video in videos]
    download_streams(streams, download_dir)


def download_by_itag(videos: list, download_dir: str, itag=None, print_info=True):

    if print_info:
        [print_stream_data(video) for video in videos]

    if itag is None:
        itag = int(get_input("Enter itag"))

    streams = [video.streams.get_by_itag(itag) for video in videos]
    download_streams(streams, download_dir)


def filter_audio(videos: list, download_dir: str):

    for video in videos:
        print("\nTitle: ", video.title)
        [print(line) for line in video.streams.filter(only_audio=True)]

    download_by_itag(videos, download_dir, print_info=False)


def filter_video(videos: list, download_dir: str):

    for video in videos:
        print("\nTitle: ", video.title)
        [print(line) for line in video.streams.filter(only_video=True)]

    download_by_itag(videos, download_dir, print_info=False)


def filter_adaptive(videos: list, download_dir: str):

    for video in videos:
        print("\nTitle: ", video.title)
        [print(line) for line in video.streams.filter(adaptive=True)]

    download_by_itag(videos, download_dir, print_info=False)


def download_streams(streams: list, download_dir: str):

    failed_downloads = []

    if get_confirm("Display filesize", default="n"):
        print_streams_filesize(streams)

    if get_confirm("Download videos?"):

        for i, stream in enumerate(streams):
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


# handles printing info

def print_streams_filesize(streams: list):

    [print(f"{i+1:^4}| Filesize: {stream.filesize_mb}MB {'':^4}| Title: {stream.title}")
     for i, stream in enumerate(streams)]


def print_streams_info(videos: list):

    for video in videos:
        print("\nTitle: ", video.title)
        [print(line) for line in video.streams]

# the modes


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

    get_videos_modes()(videos, download_dir)


def shamo_playlist():

    while True:
        try:
            playlists = [Playlist(videos) for videos in get_links()]

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


def test():
    array = ["a", "b", "c", "d", "e", 1, 2, 3, 4]

    selection = get_selection(len(array), array)

    print(selection)


if __name__ == "__main__":
    # main()
    test()
