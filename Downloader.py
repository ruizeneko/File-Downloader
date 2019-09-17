# Web to extract links from a website : https://hackertarget.com/extract-links/
# If the error "urllib.error.URLError: <urlopen error
# [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
# self signed certificate in certificate chain (_ssl.c:1076)>"
# arises, please visit : https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
# and install the recommended packages

from pathlib import Path as pt
import urllib.request


def folder_creator(direction):
    # creates a folder in the given direction folder
    direction.mkdir(exist_ok=False)


def data_obteiner(url, cut_world):

    # tool to find the names of the directory and the subdiretories where the file will be store
    #
    # Args : the original url and the world starting on which (included) we will create our directories
    # (for instance if the tree is ./me/name/is/xx.pdf and the cut world is me, the class
    # will create name/is directories)
    #
    # Return :
    #   direction : the tree as an array of the directories to be created
    #   file_name : the name of the file to be stored

    url_name_clean = url.split("/")  # the urls as an array
    file_name = url_name_clean[len(url_name_clean) - 1].strip()  # the name of the file

    for i in range(len(url_name_clean)):
        world = url_name_clean[i]

        if world == cut_world:
            direction = url_name_clean[i:len(url_name_clean) - 1]  # the direction tree

    return direction, file_name


class DownloaderCreator:

    # Downloads the file and the creates the whole directory tree to store it
    # Args:
    #   filename : the name of the .txt file where the urls are stored.
    #   cut_world : the world starting on we will create our tree
    #   store_directory : where the data will be stored (both directories and files

    def __init__(self, filename, cut_world, store_directory):
        self.filename = filename
        self.cut_world = cut_world
        self.store_directory = store_directory

    def download_save(self):

        files_txt = open(self.filename, mode="r", encoding="utf-8")
        # a list to store the already created files. If we try to create an existing directory an exception will arise.
        already_created = list()

        for file in files_txt:
            array = data_obteiner(file, self.cut_world)[0]
            file_name = data_obteiner(file, self.cut_world)[1]

            for el in range(len(array)):
                if array[el] not in already_created:
                    already_created.append(array[el])
                    final_path = self.store_directory / "/".join(array[0:el + 1])
                    folder_creator(final_path)

                # to create the folder the first time (including last one)
                if array[el] and el == len(array) - 1:
                    urllib.request.urlretrieve(file, str(final_path / file_name))

name_of_file = "THE NAME OF THE .TXT INCLUDING THE URLS"
name_of_directory = "WHERE THEY ARE (STARTING FROM YOUR HOME DIRECTORY)"

where_data_is = pt.home() / name_of_directory / name_of_file
cutWorld = "courses"
path = pt.cwd() / "Data"

if __name__ == "__main__":
    ob = DownloaderCreator(where_data_is, cutWorld, path)
    ob.download_save()

