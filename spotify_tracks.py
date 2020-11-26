import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

class SpotifyCountryPlaylist():
    def __init__(self, playlist):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.id = playlist[0]
        self.country = playlist[1]
        self.tracks = get_tracks(self.spotify, self.spotify.playlist_tracks(self.id, limit=10), self.country)

    def get_top_10(self):
        top = {}
        for track in self.tracks:
            top[track.name] = track.get_track_dict_data()
        return top
            
def get_tracks(spotify, spotify_tracks, country):
    position = 1
    tracks = []
    for track in spotify_tracks['items']:
        tracks.append(Track(track, position, spotify, country))
        position += 1
    return tracks

class Track():
    def __init__(self, spotify_track_data, position, spotify, country):
        self.name = spotify_track_data['track']['name']
        self.id = spotify_track_data['track']['id']
        self.position = position
        self.country = country
        self.artists = []
        for artist in spotify_track_data['track']['album']['artists']:
            self.artists.append(Artist(spotify.artist(artist['id'])))
        self.genres = []
        for artist in self.artists:
            self.genres += artist.genres

    def get_track_dict_data(self):
        artists = []
        for artist in self.artists:
            artists.append(artist.name)
        return { 
                'Name': self.name, 
                'SID': self.id,
                'Position': self.position,
                'Country': self.country,
                'Artists': artists,
                'Genres': self.genres}
    
class Artist():
    def __init__(self, spotify_artist_data):
        self.name = spotify_artist_data["name"]
        self.genres = spotify_artist_data["genres"]