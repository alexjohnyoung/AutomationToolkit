from os.path import isdir, isfile, join
from os import listdir


class ResourceManager:
    def __init__(self):
        self.resources = []
        self.tag = "[Resource Manager]"
        self.path = "resources"

    def load_resources(self):
        if isdir(self.path):
            print(f"{self.tag} Loading {self.path}...")

            for filename in listdir(self.path):
                self.resources.append(filename)

        for resource in self.resources:
            print(f"{self.tag} Loaded resource '{resource}'")

        print(f"{self.tag} Loaded {len(self.resources)} {self.path}")

    def get_resource(self, name):
        return self.resources[name]

    def get_resources(self):
        return self.resources

