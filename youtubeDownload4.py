from pytube import YouTube, Playlist, exceptions
import os


class StreamsEmpty(Exception):
    pass


class Download:
    def __init__(self, videos: list, download_dir: str) -> None:
        self.videos = videos
        self.stream_qs = [video.streams for video in self.videos]
        self.download_dir = download_dir
        self.streams = []
        self.failed_downloads = []
        self.filtered = False

    def download(self, print_info=False) -> None:
        self.failed_downloads = []

        if not self.streams:
            raise StreamsEmpty

        for i, stream in enumerate(self.streams):
            if print_info:
                print(f"\n{i+1}: Downloading {stream.title}")

            try:
                stream.download(self.download_dir)
                if print_info:
                    print(f"{i+1}: Downloaded {stream.title}")

            except Exception as e:
                if print_info:
                    print(f"{i+1}: Failed to download {stream.title}. Error {e}")
                self.failed_downloads.append(stream)

    def get_streams_prompt(self):

        if self.filtered:
            streams_modes = {
                "Download by itag": self.itag
            }

        else:
            streams_modes = {
                "Download highest resolution": self.highest_resolution,
                "Download audio only": self.audio_only
            }

        answer = mode_select(streams_modes)
        
        if answer == "Download by itag":
            streams_modes[answer](get_num("Enter itag"))
            
        else:
            streams_modes[answer]()

    def get_download_prompt(self):
        if get_confirm("Continue to download", default="y"):
            self.download(print_info=True)

    def highest_resolution(self):
        self.streams = [stream_q.get_highest_resolution()
                        for stream_q in self.stream_qs]

    def audio_only(self):
        self.streams = [stream_q.get_audio_only()
                        for stream_q in self.stream_qs]

    def itag(self, itag):
        self.streams = [stream_q.get_by_itag(
            itag) for stream_q in self.stream_qs]

    def print_streams_filesize(self):

        if not self.streams:
            raise StreamsEmpty

        [print(f"{i+1:^4}| Filesize: {stream.filesize_mb}MB {'':^4}| Title: {stream.title}")
         for i, stream in enumerate(self.streams)]

    def print_stream_qs(self):
        # make the output nicer
        for video, stream_q in zip(self.videos, self.stream_qs):
            print("\nTitle: ", video.title)
            [print(line) for line in stream_q]

    def filter_audio(self):
        self.stream_qs = [stream_q.filter(only_audio=True)
                          for stream_q in self.stream_qs]

    def filter_video(self):
        self.stream_qs = [stream_q.filter(only_video=True)
                          for stream_q in self.stream_qs]

    def filter_adaptive(self):
        self.stream_qs = [stream_q.filter(adaptive=True)
                          for stream_q in self.stream_qs]

    def filters_prompt(self):
        MODES = {
            "None": self.do_nothing,
            "Filter Audio": self.filter_audio,
            "Filter Video": self.filter_video,
            "Filter Adaptive": self.filter_adaptive
        }

        MODES[mode_select(MODES)]()

        self.filtered = True

    def do_nothing(self):
        return


class PrintInfo:
    def __init__(self) -> None:
        pass


def mode_select(modes: dict) -> any:

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
    return True if start <= n and end >= n else False

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


def get_num(question, default=None):
    
    while True:
        answer = get_input(question, default)
        if answer.isdigit():
            return answer
        else:
            print("Enter a positve integer")

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


def selection_range(text, number_of_items, selection, array):
    start, end = text.split("-")

    try:

        start = int(start)
        end = int(end)

        if start < end and check_num_range(start, 1, number_of_items) and check_num_range(end, 1, number_of_items):
            selection.extend(
                [elem for elem in array[start-1:end] if elem not in selection])

    except ValueError:
        # add a statment here
        pass


def selection_single(text, number_of_items, selection, array):
    n = int(text)

    if check_num_range(n, 1, number_of_items):
        i = n-1
        if array[i] not in selection:
            selection.append(array[i])


def get_selection(array) -> list:
    selected_indexs = []
    number_of_items = len(array)
    selection = []
    answer = get_input("Enter selection (1-10 5)",
                       default="all").lower().strip()

    if answer == "all":
        return array

    answer = answer.split()

    # print(answer)

    for text in answer:

        if len(text.split("-")) == 2:
            selection_range(text, number_of_items, selection, array)

        elif text.isdigit():

            selection_single(text, number_of_items, selection, array)

    return selection


# handles downloading


# handles printing info


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

    selected_videos = get_selection(videos)

    download = Download(selected_videos, download_dir)
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


def test():
    array = ["a", "b", "c", "d", "e", 1, 2, 3, 4]

    print(array)
    selection = get_selection(array)

    print(selection)


if __name__ == "__main__":
    main()
