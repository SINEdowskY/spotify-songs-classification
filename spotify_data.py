import pandas as pd
import tekore as tk
from config import CLIENT_ID, CLIENT_SECRET


class SpotifyData:

    def get_one_song_data(self, query):
        token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
        spotify = tk.Spotify(token)
        searched_track = spotify.search(query, types=('track',), market='pl')
        artist_id = searched_track[0].items[0].artists[0].id
        id = searched_track[0].items[0].id
        af = spotify.track_audio_features(id)
        output = [
            [af.danceability,
             af.energy,
             af.loudness,
             af.acousticness,
             af.instrumentalness,
             af.liveness,
             af.speechiness,
             af.valence]
        ]
        print("Znaleziono:", searched_track[0].items[0].artists[0].name, "-", searched_track[0].items[0].name)
        print("Gatunek:", spotify.artist(artist_id).genres[0])
        return pd.DataFrame(output, columns=['danceability', 'energy', 'loudness', 'acousticness', 'instrumentalness',
                                             'liveness', 'speechiness', 'valence'])

    def get_data(self, genres):
        genres_names = genres
        token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
        spotify = tk.Spotify(token)
        output = pd.DataFrame(
            columns=['genre', 'danceability', 'energy', 'loudness', 'acousticness', 'instrumentalness',
                     'liveness', 'speechiness', 'valence'])
        for genre in genres_names:
            print('now: ', genre)
            tracks_id = []
            tracks_af = []

            try:
                searched_playlists = spotify.search(genre, types=('playlist',), market='pl', limit=50, offset=0)
                playlist_id = None
                for i in range(100):
                    if searched_playlists[0].items[i].tracks.total >= 100:
                        playlist_id = searched_playlists[0].items[i].id
                        break
                    elif i == 100:
                        playlist_id = searched_playlists[0].items[0].id

                playlist = spotify.playlist(playlist_id)
                playlist_tracks = playlist.tracks.items

                for i in range(100):
                    tracks_id.append(playlist_tracks[i].track.id)

                afs = spotify.tracks_audio_features(track_ids=tracks_id)
                print(len(afs))
                for af in afs:
                    tracks_af.append(
                        [genre, af.danceability, af.energy, af.loudness, af.acousticness, af.instrumentalness,
                         af.liveness,
                         af.speechiness, af.valence])
                x = pd.DataFrame(tracks_af,
                                 columns=['genre', 'danceability', 'energy', 'loudness', 'acousticness',
                                          'instrumentalness',
                                          'liveness', 'speechiness', 'valence'])
                output = pd.concat([output, x])
            except AttributeError:
                print('tekore attribute error')
                continue
            except IndexError:
                print('playlist index error')
                continue
            except TypeError:
                print('audio features type error')
                continue

        return output
