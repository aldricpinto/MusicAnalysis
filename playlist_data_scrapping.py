# -*- coding: utf-8 -*-
"""
author = 'Vincy Hu'

"""

#import packages
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
from requests.exceptions import HTTPError
import time
from spotipy.exceptions import SpotifyException
from config import *

# client_id = # enter your client id
# client_secret = #  enter your client secret
# username = # enter your username

# create a dataframe to store infomation of my playlists 
my_playlist =  pd.DataFrame(columns=["id", "spotify_id", "list_name"])

# getting playlist info from spotify
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlists = sp.user_playlists(username) # input your spotify account id here
data = []
# converting spotify data into dataframe
while playlists:
    for i, playlist in enumerate(playlists['items']): 
        spotifyid = playlist['id'] 
        listname = playlist['name'] 
        rec = {'id':i+1 , 
                'spotify_id': spotifyid,
                'list_name': listname
              }
        data.append(rec)
        
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

my_playlist = pd.DataFrame(data)
# dataframe for song
my_song =  pd.DataFrame(columns=["list_id", "song_id","song_name","artist","popularity",'release_date']
                       )
songData = []
# getting song info from each playlist
for listid in my_playlist["spotify_id"]:
    songs = []
    content = sp.user_playlist_tracks(username, listid, fields=None, limit=100, offset=0, market=None)
    songs += content['items']
    for song in songs:
        songRec = {"list_id" : listid,
                                  "song_id":song['track']['id'],
                                  "song_name":song['track']['name'],
                                  "artist":song['track']['artists'][0]['name'],
                                  "popularity": song['track']['popularity'],
                                  "release_date": song['track']['album']['release_date']
                }
        songData.append(songRec)

my_song = pd.DataFrame(songData)

featureData = []
max_retries = 5  # Set a maximum number of retries
backoff_time = 5 
# song feature dataframe
my_feature = pd.DataFrame(columns=["song_id","energy", "liveness","tempo","speechiness",
                                "acousticness","instrumentalness","danceability",
                                "duration_ms","loudness","valence",
                                "mode","key"])
# playlist songs' features
for song in my_song['song_id']:

    features = sp.audio_features(tracks = [song])[0]
    featureRec = {"song_id":song,
                                    "energy":features['energy'], 
                                    "liveness":features['liveness'],
                                    "tempo":features['tempo'],
                                    "speechiness":features['speechiness'],
                                    "acousticness":features['acousticness'],
                                    "instrumentalness":features['instrumentalness'],
                                    "danceability":features['danceability'],
                                    "duration_ms":features['duration_ms'],
                                    "loudness":features['loudness'],
                                    "valence":features['valence'],
                                    "mode":features['mode'],
                                    "key":features["key"],
                                 }
   
    featureData.append(featureRec)

my_feature = pd.DataFrame(featureData)

# merging the song info and song features dataframe
song_feature = pd.merge(my_song,my_feature,how='left',left_on='song_id', right_on='song_id')
list_song_feature = pd.merge(my_playlist,song_feature,how='left',left_on='spotify_id', right_on='list_id')

# exporting to csv file
list_song_feature.to_csv('playlist.csv')