# Web to extract links from a website : https://hackertarget.com/extract-links/
# We will create a class to create a directory from the link

import os
from pathlib import Path as pt
import urllib.request
import numpy as np


path = pt.cwd() / "Data"

class Directory_creator():

    def __init__(self, url, cut_world):
        self.url = url
        self.cut_world = cut_world

    def data_obteiner(self):

        url_name = self.url.split("/")
        file_name = url_name[len(url_name)-1].strip()

        for i in range(len(url_name)):
            world = url_name[i]

            if world == self.cut_world:
                direction = url_name[i+1:len(url_name)-1]

        return direction,file_name


def folder_creator(direction):
    direction.mkdir(exist_ok = False)

name_of_file = "THE NAME OF YOUR FILE HERE"
where_data_is = pt.home() / name_of_file
files_txt = open(where_data_is, mode = "r", encoding = "utf-8")

already_created = list()

for file in files_txt:
    array = Directory_creator(file,"Lehre").data_obteiner()[0]
    file_name = Directory_creator(file,"Lehre").data_obteiner()[1]
    print(file)

    for el in range(len(array)):

        if array[el] not in already_created:
            already_created.append(array[el])
            folder_creator(path / "/".join(array[0:el+1]))
            final_path = path / "/".join(array[0:el+1])
        if array[el] and el == len(array)-1:
            urllib.request.urlretrieve(file, str(final_path / file_name))
