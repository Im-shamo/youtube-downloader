from user_input import mode_select
from shamo_videos import shamo_videos
from shamo_playlist import shamo_playlist



def main():

    MODES = {
        "Videos": shamo_videos,
        "Playlist": shamo_playlist
    }

    MODES[mode_select(MODES)]()

if __name__ == "__main__":
    main()
