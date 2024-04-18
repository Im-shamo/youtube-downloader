from user_input import mode_select
from shamo_videos import shamo_videos
from shamo_playlist import shamo_playlist
from cli import video_cli, playlist_cli, print_playlists_details, print_videos_details
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


    download_options_group = parser.add_mutually_exclusive_group()
    download_options_group.add_argument("--high-res", default=False, action="store_true", help="Download highest resolution")
    download_options_group.add_argument("--high-audio", default=False, action="store_true", help="Download hightest quality audio")
    download_options_group.add_argument("--itag", type=int, help="Download by itag: int")

    parser.add_argument("--print-info", "-p", default=False, action="store_true", help="print info about videos or playlists")


    # https://stackoverflow.com/questions/15935092/creating-mutually-inclusive-positional-arguments-with-argparse
    argvs = parser.parse_args()
    if argvs.video_url or argvs.playlist_url:
        if not (argvs.high_res or argvs.high_audio or argvs.itag) and not argvs.print_info:
            print("must at least have one download option: --high-res --high-audio --itag")
            quit()
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
        quit()

    elif argvs.video_url:
        if argvs.print_info:
            print_videos_details(argvs.video_url)
        else:
            video_cli(argvs.video_url, argvs.output_path, argvs.verbose, high_res=argvs.high_res, high_audio=argvs.high_audio, itag=argvs.itag)
        quit()

    elif argvs.playlist_url:
        if argvs.print_info:
            print_playlists_details(argvs.playlist_url)
        else:
            playlist_cli(argvs.playlist_url, argvs.output_path, argvs.verbose, high_res=argvs.high_res, high_audio=argvs.high_audio, itag=argvs.itag)
        quit()





if __name__ == "__main__":
    main()
