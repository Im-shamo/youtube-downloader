from pytube import YouTube, Stream
from exceptions import *
from user_input import *
# import cli


class VideosDownload:
    def __init__(self, videos: list[YouTube], output_path: str):
        # check if is videos list empty
        if len(videos) == 0:
            raise NoVideosAvailable
        else:
            self.videos = videos

        self.stream_qs = [video.streams for video in videos]
        self.streams:list[Stream] = []
        self.output_path = output_path
        
    def print_stream_info(self):
        # todo
        for i, (video, stream_q) in enumerate(zip(self.videos, self.stream_qs), 1 ):
            print(f"{i:>3} | {video.title}")
            [print(line) for line in stream_q]

    def highest_resolution(self):
        self.streams = [stream_q.get_highest_resolution() for stream_q in self.stream_qs ]
    
    def best_audio_only(self):
        self.streams = [ stream_q.get_audio_only() for stream_q in self.stream_qs ]

    def by_itag(self, itag:int):
        self.streams = [ stream_q.get_by_itag(itag=itag) for stream_q in self.stream_qs]

    def filter_audio_only(self):
        self.stream_qs = [stream_q.filter(only_audio=True) for stream_q in self.stream_qs]

    def filter_video_only(self):
        self.stream_qs = [stream_q.filter(only_video=True) for stream_q in self.stream_qs]

    def filter_adaptive_only(self):
        self.stream_qs = [stream_q.filter(adaptive=True) for stream_q in self.stream_qs]
        
    def download(self, print_info = False):
        if not self.streams:
            raise NoStreamsAvailable

        for i, stream in enumerate(self.streams):
            if print_info:
                print(f"\n{i+1}: Downloading {stream.title}")

            try:
                stream.download(self.output_path)
                if print_info:
                    print(f"{i+1}: Downloaded {stream.title}")

            except Exception as e:
                if print_info:
                    print(f"{i+1}: Failed to download {stream.title}. Error {e}")

    def print_streams_filesize(self):

        if not self.streams:
            raise NoStreamsAvailable

        total_size = 0
        for i, stream in enumerate(self.streams):
            size = stream.filesize_mb
            total_size += size
            print(f"{i+1:^4}| Filesize: {stream.filesize_mb:.2f} MB {'':^4}| Title: {stream.title}")


        print(f"Total size is {total_size:.2f} MB")