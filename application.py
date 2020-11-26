from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from countries import get_top_tracks_playlist, get_countries
from spotify_tracks import SpotifyCountryPlaylist
    
app = Flask(__name__)

@app.route("/")
def home():
    countries = get_countries()
    return render_template("home.html", countries=countries)

@app.route("/top-tracks-<country>")
def toptracks(country):
    country = country.replace("\xa0", " ")
    country = country.replace("%C2%A0", " ")
    playlist_id = get_top_tracks_playlist(country)
    playlist = SpotifyCountryPlaylist(playlist_id)
    tracks = playlist.get_top_10()
    return tracks