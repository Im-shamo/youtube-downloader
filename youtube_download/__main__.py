from user_input import mode_select
from shamo_videos import shamo_videos
from shamo_playlist import shamo_playlist
from cli import video_cli
import argparse
from sys import argv
from os import path

def get_args() -> vars:
    parser = argparse.ArgumentParser(description="Youtube downloader")
    parser.add_argument("-v", "--verbose", default=False, action="store_true")
    parser.add_argument("--output-path", "-o", type=str, help="Download location: default = $HOME/Videos", default=path.expanduser("~/Videos"))

    url_group = parser.add_mutually_exclusive_group()
    url_group.add_argument("--video-url", type=str, nargs="+", help="video url(s)")
    url_group.add_argument("--playlist-url", type=str, nargs="+", help="playlist url(s)")


    options_group = parser.add_mutually_exclusive_group()
    options_group.add_argument("--high-res", default=False, action="store_true", help="Download highest resolution")
    options_group.add_argument("--high-audio", default=False, action="store_true", help="Download hightest quality audio")
    options_group.add_argument("--itag", type=int, help="Download by itag: int")


    # https://stackoverflow.com/questions/15935092/creating-mutually-inclusive-positional-arguments-with-argparse
    argvs = parser.parse_args()
    if argvs.video_url or argvs.playlist_url:
        if not (argvs.high_res or argvs.high_audio or argvs.itag):
            print("must at least have one download option: --high-res --high-audio --itag")
    return argvs


def main():
    argvs = get_args()

    # https://stackoverflow.com/questions/10698468/argparse-check-if-any-arguments-have-been-passed
    if len(argv) == 1:
        MODES = {
            "Videos": shamo_videos,
            "Playlist": shamo_playlist
        }

        MODES[mode_select(MODES)]()

    elif argvs.video_url:
        video_cli(argvs.video_url, argvs.output_path, argvs.verbose, high_res=argvs.high_res, high_audio=argvs.high_audio, itag=argvs.itag)


if __name__ == "__main__":
    main()
