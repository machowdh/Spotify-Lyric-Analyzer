import spotipy
from decouple import config
from spotipy.oauth2 import SpotifyClientCredentials

# Set up the client credentials manager
client_credentials_manager = SpotifyClientCredentials(client_id=config("SPOTIFY_CLIENT_ID"), client_secret=config("SPOTIFY_CLIENT_SECRET"))
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_details(track_id):
    """
    Fetch details of a track using its Spotify ID.
    """
    track = sp.track(track_id)
    details = {
        "id": track["id"],
        "name": track["name"],
        "artist": track["artists"][0]["name"],  # Taking the first artist for simplicity
        "album": track["album"]["name"],
        "release_date": track["album"]["release_date"],
        "duration_ms": track["duration_ms"],
        "popularity": track["popularity"]
    }
    return details

def search_tracks(query, limit=10):
    """
    Search for tracks based on a query string.
    """
    results = sp.search(q=query, limit=limit, type="track")
    tracks = results["tracks"]["items"]
    return [get_track_details(track["id"]) for track in tracks]

if __name__ == '__main__':
    fso = get_track_details('1ANYHWUz5NqPu2EBALGK9Z')
    print(fso)