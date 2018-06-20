import os
import re

class TokenCollector:

    def __init__(self, root_path, ignore_pattern):
        self.root_path      = root_path
        self.ignore_pattern = ignore_pattern

    @staticmethod
    def get_tokens_from_file(file_name):
        file = open(file_name, "r")
        

    def get_tokens(self):
        root = self.root_path
        dir = []

        while True:
            for entry in os.listdir(root):
                if os.path.isdir(entry):
                    if entry in self.ignore_pattern:
                        continue
                    dir.append(os.path.join(root, entry))
                else:
                    if entry in self.ignore_pattern:
                        continue
                    TokenCollector.get_tokens_from_file(os.path.join(root, entry))

            if len(dir) == 0:
                break
            root = dir[0]
            del[dir[0]]



t = TokenCollector(os.getcwd(),[".git", ".idea", "__pycache__", "words.txt"])
t.get_tokens()