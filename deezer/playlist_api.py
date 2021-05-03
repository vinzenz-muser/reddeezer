import requests
import requests.auth
import yaml
from pprint import pprint

def get_config():
    with open("configs/deezer.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def get_me(config):
    response = requests.get(f"https://api.deezer.com/user/me/playlists?access_token={config['access_token']}")
    ans = response.json()

    for i in ans["data"]:
        print(i["id"], i["title"])

def get_playlist_song_ids(playlist_id):
    ans_ids = []
    response = requests.get(f"https://api.deezer.com/playlist/{playlist_id}")
    ans = response.json()
    
    for i in ans["tracks"]["data"]:
        ans_ids.append(i["id"])
    
    return ans_ids
    
def get_song_ids(song_list):
    song_ids = []
    
    for song in song_list:
        artist = song["artist"]
        title = song["title"]
        search_result = requests.get(f'https://api.deezer.com/search?q=artist:"{artist}" track:"{title}"')
        ans = search_result.json()
        if len( ans["data"]) > 0:
            first_res = ans["data"][0]
            song_ids.append(first_res["id"])
    
    return song_ids

def add_songs_to_playlist(song_ids, config):
    playlist_id = config["playlist_id"]
    token = config["access_token"]
    base_str = f'https://api.deezer.com/playlist/{playlist_id}/tracks?songs='+",".join([str(i) for i in song_ids])
    req_string = base_str+f"&access_token={token}"
    ans = requests.post(req_string)

if __name__ == "__main__":
    config = get_config()
    get_playlist_song_ids(config["playlist_id"])