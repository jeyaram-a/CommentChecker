import re
import os
import sys

class CommentChecker:
    #root_path =start location for searching
    #ignore_pattern = folder or file to be ignored
    def __init__(self, root_path, ignore_pattern):
        self.root_path      = root_path
        self.ignore_pattern = ignore_pattern

    @staticmethod
    #Splits contents with split_regex and if
    #   splitted contents matches regex adds to trie
    def check_words(contents, regex, split_regex, trie):
        matches = re.finditer(regex, contents, re.MULTILINE | re.DOTALL)

        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.groups())):
                comment = match.group(1)
                comment = re.split(split_regex, comment)
                comment = [i for i in comment if (len(i) == 1 and (i == 'a' or i =='i'or i =='A' or i == 'I')) or len(i) >1]
                for word in comment:
                    if not trie.contains(word.lower()):
                        sys.stdout.write("      Not in dictionary \033[1;31m%s\033[0m\n"%word)
            
            
    #Splits the file-comments into words and adds to the trie
    def split_file(file, trie):
        print("Checking file ", file)
        file = open(file, "r+")
        contents = file.read()

        regex_multiline = r"/\*(.*?)\*/"
        regex_singleline = r"//(.*?)\n"
        split_regex = "_|%| |\n|\.|=|\+|/|'|!|@|\(|\)|,|\"|:|\>|\<|;|#|\?|\*|-|{|}|[0-9]|\||\[|\]|\\\|&"
        CommentChecker.check_words(contents, regex_multiline, split_regex, trie)
        CommentChecker.check_words(contents, regex_singleline, split_regex, trie)
        print("-----------------------------------------------")

    #Check comments from the .c and .h from root_path recursively
    def check_comments(self, trie):
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
                    if re.match(".*\.c$|.*\.h$",os.path.join(root, entry)):
                        CommentChecker.split_file(os.path.join(root, entry), trie)
            if len(dir) == 0:
                break
            root = dir[0]
            del[dir[0]]


