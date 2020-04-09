import requests
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request


api_key = 'amh8giT5uiMRuUSvvs6C4Tktyr_XQCOT6XK5qdV_pgShCuWX9N7O0GQXJe4fNXsq'


def make_request(song, artist):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + api_key}
    search_url = base_url + '/search'
    data = {'q': song + ' ' + artist}
    response = requests.get(search_url, data=data, headers=headers)
    return response.json()


def get_lyrics(song_name, artist=None):
    if artist:
        print(f"Given: {song_name} | {artist}")
        json = make_request(song_name, artist)
    else:
        print(f"\nGiven: {song_name}")
        json = make_request(song_name, "")

    hit_data = []

    for hit in json['response']['hits']:
        hit = hit['result']
        hit_data.append({'artist': hit['primary_artist']['name'], 'song': hit['full_title'].replace("\xa0", " "), 'song_url': hit['url'], 'artist_url': hit['primary_artist']['url']})

    print(f"Found: {hit_data[0]['song']} by {hit_data[0]['artist']}")

    req = Request(hit_data[0]['song_url'], headers={'User-Agent': 'Mozilla/5.0'})
    html = uReq(req).read()
    page_soup = soup(html, "html.parser")

    lyrics = page_soup.find('div', {'class': 'lyrics'}).get_text()[1:]
    return lyrics
