#!usr/bin/evn python

import requests

def download(url):
    get_responce = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name,'wb') as out_file:
        out_file.write(get_responce.content)

download("https://www.google.com")