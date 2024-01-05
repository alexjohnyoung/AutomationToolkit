from os.path import isdir
from os import mkdir


class Util:

    @staticmethod
    def create_folders():
        if not isdir("resources"):
            mkdir("resources")

        if not isdir("procedures"):
            mkdir("procedures")

        if not isdir("events"):
            mkdir("events")
