import reddit.api_token as reddit
import deezer.playlist_api as deezer

deezer_config = deezer.get_config()

song_list = reddit.get_song_list()
new_songs = deezer.get_song_ids(song_list)
existing_songs = deezer.get_playlist_song_ids(deezer_config["playlist_id"])
songs_to_add = set(new_songs) - set(existing_songs)

deezer.add_songs_to_playlist(songs_to_add, deezer_config)
