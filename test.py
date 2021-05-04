import reddit.api_token as reddit
import deezer.playlist_api as deezer

config = deezer.get_config()
print(deezer.get_me(config))