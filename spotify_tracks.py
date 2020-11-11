import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyPlaylistTopTracks():
    def __init__(self, playlist):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.id = playlist[0]
        self.country = playlist[1]
        self.tracks = get_tracks(self.spotify, self.spotify.playlist_tracks(self.id, limit=10), self.country)

    def get_musics(self):
        musics = []
        for track in self.tracks:
            musics.append(track.get_music_dict_data())
        return musics

    def get_artists(self):
        artists = []
        for track in self.tracks:
            artists += track.get_artists_list_data()
        return artists

    def get_genres(self):
        genres = []
        for track in self.tracks:
            genres += track.get_genres_list_data()
        return genres

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

    def get_music_dict_data(self):
        return { 
                'Name': self.name, 
                'SID': self.id,
                'Position': self.position,
                'Country': self.country }
    
    def get_artists_list_data(self):
        artists = []
        for artist in self.artists:
            artists.append(
                {
                    'Music_SID': self.id,
                    'Name': artist.name
                }
                )
        return artists
            
    def get_genres_list_data(self):
        genres = []
        for genre in self.genres:
            genres.append(
                {
                    'Music_SID': self.id,
                    'Genre': genre
                }
            )
        return genres

class Artist():
    def __init__(self, spotify_artist_data):
        self.name = spotify_artist_data["name"]
        self.genres = spotify_artist_data["genres"]