import requests
import requests.auth
import yaml
from pprint import pprint

def get_config():
    with open("./config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def get_me(config):
    response = requests.get(f"https://api.deezer.com/user/me/playlists?access_token={config['access_token']}")
    ans = response.json()
    for i in ans["data"]:
        print(i["id"], i["title"])

def get_playlist_song_ids(playlist_id):
    response = requests.get(f"https://api.deezer.com/playlist/{playlist_id}")
    ans = response.json()
    print(ans)
    for i in ans["tracks"]["data"]:
        print(i["id"], i["title"])
    
def get_song_ids(song_list):
    for song in song_list:
        artist = song["artist"]
        title = song["title"]
        search_result = requests.get(f'https://api.deezer.com/search?q=artist:"{artist}" track:"{title}')
        ans = search_result.json()

if __name__ == "__main__":
    config = get_config()
    get_playlist_song_ids(config["playlist_id"])