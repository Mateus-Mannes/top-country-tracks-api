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
    country = country.replace("\xa0", " ")
    country = country.replace("%C2%A0", " ")
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    playlist = get_top_tracks_playlist(country)
    tracks = SpotifyPlaylistTopTracks(playlist)
    return {'Musics': tracks.get_musics(), 'Artists': tracks.get_artists(), 'Genres': tracks.get_genres()}

@app.route("/all")
def allcountries():
    countries = get_countries()
    all_top_tracks = {'Musics': [], 'Artists': [], 'Genres': []}
    for country in countries:
        top_tracks = toptracks(country)
        all_top_tracks['Musics'] += top_tracks['Musics']
        all_top_tracks['Artists'] += top_tracks['Artists']
        all_top_tracks['Genres'] += top_tracks['Genres']
    return all_top_tracks
