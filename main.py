from tokenize import String
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import requests
from lyricsgenius import Genius
import numpy as np
from twilio.rest import Client
from flask import Flask, request, redirect

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                                           client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")))

genius = Genius(os.getenv("GENIUS_ACCESS_TOKEN"))

# A function to remove features from song titles to optimize searching
def cleanString(string): 
    length = len(string)
    for i in range(len(string)):
        if (string[i] == "("):
            return string[0:i-1]
    return string
    
class Track:
    def __init__(self, artist, title, track_number, uri):
        self._artist = artist
        self._title = title
        self._track_number = track_number
        self._uri = uri
        song = genius.search_song(title, artist)
        if (song != None):
            self._lyrics = song.lyrics
        else:
            self._lyrics = "Could not find lyrics for this track :("
    
    def getArtist(self):
        return self._artist

    def getTitle(self):
        return self._title

    def getTrackNumber(self):
        return self._track_number
    
    def getUri(self):
        return self._uri
    
    def getLyrics(self):
        return self._lyrics


def getAlbumLyrics():
    
    # Get album ID from top result of search
    ALBUM = str(input("Enter the name of the album you want: "))
    results = sp.search(q = "album:" + ALBUM, type = "album")
    ALBUM_ID = results['albums']['items'][0]['uri']

    # Getting raw album tracks
    album_tracks_raw = sp.album_tracks(ALBUM_ID, market="CA")
    length = len(album_tracks_raw['items'])

    # New array of tracks
    album_tracks = np.empty(length, Track)

    # Parsing data into custom objects
    for i in range(length):
        album_tracks[i] = Track(album_tracks_raw['items'][i]['artists'][0]['name'], 
                                cleanString(album_tracks_raw['items'][i]['name']), 
                                album_tracks_raw['items'][i]['track_number'], 
                                album_tracks_raw['items'][i]['uri'])


    for track in album_tracks:
        message = "\n" + f"{track.getArtist()} - {track.getTitle()}" + "\n" + track.getLyrics()
        parts = [message[i:i+1550] for i in range(0, len(message), 1550)]
        for part in parts:   
            print(len(part))    
            client.messages.create(
               body=part,
               from_='+12054902704',
               to="+14378810757"
            )
            

getAlbumLyrics()



    