# top-country-tracks-api

This is an flask application that returns data of the top 10 most listened tracks of a given country.

# How to use

to access the data you can access https://top-country-tracks-api.herokuapp.com/ or https://top-country-tracks-api.herokuapp.com/top-tracks-"A country name ",
for example: https://top-country-tracks-api.herokuapp.com/top-tracks-Brazil. You can do this manually or by a Url request.
The returned data will be a dictionary/json with musics Names, position, genres, artists, and Spotify track Id. It will always be updated according to the playlist of the top 50 tracks of the chosen country. The list of available countries is in the index page: https://top-country-tracks-api.herokuapp.com/

# The code
The app is accessing the Spotify Api using the Spotipy Lib (https://spotipy.readthedocs.io/en/2.16.1/), the process of manipulating tge data happens in the class I've made called spotify_tracks
