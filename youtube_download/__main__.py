#!/home/shamokwok/Git/random-stuff/.venv/bin/python
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
    parser.add_argument("--output", "-o", type=str, help=f"Download location: default = {path.expanduser('~/Videos')}", default=path.expanduser("~/Videos"))

    video_group = parser.add_argument_group("videos options")
    video_group.add_argument("--video", type=str, nargs="+", help="video url(s)")

    playlist_group = parser.add_argument_group("playlist options")
    playlist_group.add_argument("--playlist", type=str, nargs="+", help="playlist url(s)")
    playlist_group.add_argument("--create-dir", action="store_true", help="create a directory with the name of the playlist title in output_path")


    download_options_group = parser.add_argument_group("Download option for videos and playlist")
    download_options_group.add_argument("--high-res", default=False, action="store_true", help="Download highest resolution")
    download_options_group.add_argument("--high-audio", default=False, action="store_true", help="Download hightest quality audio")
    download_options_group.add_argument("--itag", type=int, help="Download by itag: int")

    parser.add_argument("--print-info", "-p", default=False, action="store_true", help="print info about videos or playlists")


    # https://stackoverflow.com/questions/15935092/creating-mutually-inclusive-positional-arguments-with-argparse
    argvs = parser.parse_args()
    if argvs.video or argvs.playlist:
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

    elif argvs.video:
        if argvs.print_info:
            print_videos_details(argvs.video)
        else:
            video_cli(
                argvs.video,
                argvs.output_path,
                argvs.verbose,
                high_res=argvs.high_res,
                high_audio=argvs.high_audio,
                itag=argvs.itag
            )
        quit()

    elif argvs.playlist:
        if argvs.print_info:
            print_playlists_details(argvs.playlist, print_videos=True)
        else:
            playlist_cli(
                argvs.playlist,
                argvs.output,
                argvs.verbose,
                high_res=argvs.high_res,
                high_audio=argvs.high_audio,
                itag=argvs.itag,
                create_dir=argvs.create_dir
            )
        quit()





if __name__ == "__main__":
    main()
