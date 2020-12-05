# top-country-tracks-api

This is an flask application that returns data of the top 10 most listened tracks of a given country.

# How to use

to access the data you can access https://top-country-tracks-api.herokuapp.com/ or https://top-country-tracks-api.herokuapp.com/top-tracks-"A country name ",
for example: https://top-country-tracks-api.herokuapp.com/top-tracks-Brazil, or "Global", to get top10 of the world: https://top-country-tracks-api.herokuapp.com/top-tracks-Global. You can do this manually or by a Url request.
The returned data will be a dictionary/json with musics Names, position, genres, artists, and Spotify track Id. It will always be updated according to the playlist of the top 50 tracks of the chosen country. The list of available countries is in the index page: https://top-country-tracks-api.herokuapp.com/. You can also access http://mateusmedeiros.pythonanywhere.com/, there is a json with the data of all the countries and the global playlist, that is apdated daily by the Scheduled tasks from pythonanywhere, as this page is not directly making a request to Spotify api to get real time data, it is much faster.

# The code
The app is accessing the Spotify Api using the Spotipy Lib (https://spotipy.readthedocs.io/en/2.16.1/), the process of manipulating tge data happens in the class I've made called spotify_tracks
