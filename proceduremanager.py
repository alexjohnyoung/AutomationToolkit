from os.path import isdir, isfile, join
from os import listdir


class ProcedureManager:
    def __init__(self):
        self.procedures = []
        self.tag = "[Procedure Manager]"
        self.path = "procedures"

    def load_procedures(self):
        if isdir(self.path):
            print(f"{self.tag} Loading {self.path}...")

            for procedure in listdir(self.path):
                procedure = procedure.replace(".txt", "")
                self.procedures.append(procedure)

        for procedure in self.procedures:
            print(f"{self.tag} Loaded {self.path} '{procedure}'")

        print(f"{self.tag} Loaded {len(self.procedures)} {self.path}")

    @staticmethod
    def save_procedure(self, name, text):
        procedure = open(f"procedures/{name}.txt", "w")
        procedure.write(text)
        procedure.close()

    def get_procedure(self, name):
        return self.procedures[name]

    def get_procedures(self):
        return self.procedures

