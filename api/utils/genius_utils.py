from lyricsgenius import Genius
from decouple import config
from spotify_utils import get_track_details

genius = Genius(config("GENIUS_TOKEN"))


def get_track_lyrics(track_id):
    '''
    Take's a Spotify track id to get track details.
    These track details are then fed into the Genius API to get the corresponding lyrics.
    '''
    spotify_track_details = get_track_details(track_id)
    track_name = spotify_track_details["name"]
    artist_name = spotify_track_details["artist"]   
    song = genius.search_song(track_name, artist_name)
    return song.lyrics


if __name__ == '__main__':
    fso_lyrics = get_track_lyrics("1ANYHWUz5NqPu2EBALGK9Z")
    print(fso_lyrics)
