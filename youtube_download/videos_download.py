from pytube import YouTube, Stream
from exceptions import *
from user_input import *


class VidosDownload:
    def __init__(self, videos: list[YouTube], download_dir: str) -> None:

        self.streams: list[Stream]
        self.failed_downloads: list[Stream]

        if videos:
            self.videos = videos
        else:
            raise NoVideosAvailable
        self.stream_qs = [video.streams for video in self.videos]
        self.download_dir = download_dir
        self.streams = []
        self.failed_downloads = []
        self.filtered = False

    def download(self, print_info=False) -> None:
        self.failed_downloads = []

        if not self.streams:
            raise NoStreamsAvailable

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
            raise NoStreamsAvailable

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
