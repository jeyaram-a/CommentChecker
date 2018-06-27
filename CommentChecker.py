import re
import os
import sys

class CommentChecker:

    def __init__(self, root_path, ignore_pattern):
        self.root_path      = root_path
        self.ignore_pattern = ignore_pattern

    @staticmethod
    def list_to_string(list_):
        file_contents = ""
        for letter in list_:
            file_contents += letter
        return file_contents

    def check_comments(file, trie):
        print("Checking file ", file)
        file = open(file, "r+")
        contents = file.read()

        regex = r"/\*(.*?)\*/"
        regex1 = r"//(.*?)\n"
        split_regex = "_| |\n|\.|/|'|!|@|\(|\)|,|\"|:|\>|\<|;|#|\?|\*|-|{|}|[0-9]|\|"
        print("   Checking block comments")
        matches = re.finditer(regex, contents, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.groups())):
                comment = match.group(1)
                comment = re.split(split_regex, comment)
                comment = [i.lower() for i in comment if (len(i) == 1 and (i == 'a' or i =='i')) or len(i) > 1]
                for word in comment:
                    if not trie.contains(word):
                        sys.stdout.write("      Not in dictionary \033[1;31m%s\033[0m\n"%word)
        print("   Checking single line comments")
        matches = re.finditer(regex1, contents, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.groups())):
                comment = match.group(1)
                comment = re.split(split_regex, comment)
                comment = [i.lower() for i in comment if (len(i) == 1 and (i == 'a' or i =='i')) or len(i) > 1]
                for word in comment:
                    if not trie.contains(word):
                        sys.stdout.write("      Not in dictionary \033[1;31m%s\033[0m\n"%word)
        print("-----------------------------------------------")

    def do_something(self, trie):
        root = self.root_path
        dir = []
        print("Root is ", root)
        while True:
            for entry in os.listdir(root):
                if os.path.isdir(os.path.join(root, entry)):
                    if entry in self.ignore_pattern:
                        continue 
                    dir.append(os.path.join(root, entry))
                else:
                    if entry in self.ignore_pattern:
                        continue
                    if re.match(".*\.c|.*\.h",os.path.join(root, entry)):
                        CommentChecker.check_comments(os.path.join(root, entry), trie)
            if len(dir) == 0:
                break
            root = dir[0]
            del[dir[0]]


