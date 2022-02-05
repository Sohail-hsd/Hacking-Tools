#!usr/bin/evn python

import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]          # this will extract the file name from url.
    with open(file_name,'wb') as out_file:   # this will open a file (wb) mean write binery.
        out_file.write(get_response.content) # this will write the bineries on the file.

download("https://image.freepik.com/free-vector/flat-car-poster-with-photo-horizontal_52683-64510.jpg")