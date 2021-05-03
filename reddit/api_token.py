import requests
import requests.auth
import yaml
from pprint import pprint

def get_token(config):
    client_auth = requests.auth.HTTPBasicAuth(config["app_id"], config["app_secret"])
    post_data = {"grant_type": "password", "username": config["username"], "password": config["password"]}
    headers = {"User-Agent": f"{config['app_name']} by {config['username']}"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

    return response.json()

def get_top_entires(config, token):
    headers = {"Authorization": f"bearer {token['access_token']}", "User-Agent": f"{config['app_name']} by {config['username']}"}
    response = requests.get("https://oauth.reddit.com/r/listentothis/top?t=week", headers=headers)
    return response.json()

def get_config():
    with open("configs/reddit.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def get_song_list():
    config = get_config()
    token = get_token(config)
    entries = get_top_entires(config, token)
    song_list = [i["data"]["title"] for i in entries["data"]["children"]]
    print(len(song_list))
    cleaned_list = []
    for song in song_list:
        song = song.replace("--", "-")
        
        brackets = [("(", ")"), ("[", "]")]

        try:
            for bracket in brackets:
                while bracket[0] in song and bracket[1] in song:
                    start = song.find(bracket[0])
                    end = song.find(bracket[1])
                    song = song[:start]+song[end+1:]
        except:
            continue

        song = song.split("-")
        for i,word in enumerate(song):
            song[i] = word.strip()
        
        if len(song) >= 2:
            artist = song[0]
            title = song[1]
            cleaned_list.append({
                "artist": artist,
                "title": title
            })

    return cleaned_list

if __name__ == "__main__":
    get_song_list()