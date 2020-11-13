from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from countries import get_top_tracks_playlist, get_countries
from spotify_tracks import SpotifyPlaylistTopTracks
    
app = Flask(__name__)

@app.route("/")
def home():
    countries = get_countries()
    return render_template("home.html", countries=countries)

@app.route("/top-tracks-<country>")
def toptracks(country):
    country.replace("\xa0", " ")
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    playlist = get_top_tracks_playlist(country)
    tracks = SpotifyPlaylistTopTracks(playlist)
    return {'Musics': tracks.get_musics(), 'Artists': tracks.get_artists(), 'Genres': tracks.get_genres()}