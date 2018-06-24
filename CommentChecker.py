import re
import os

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
        print("file is ", file)
        file = open(file, "r+")
        contents = file.read()

        regex = r"/\*(.*?)\*/"
        regex1 = r"//(.*?)\n"
        
        matches = re.finditer(regex, contents, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.groups())):
                comment = match.group(1)
                comment = re.split("_| |\n|\.", comment)
                comment = [i.lower() for i in comment if (len(i) == 1 and (i == 'a' or i =='i')) or len(i) > 1]
                for word in comment:
                    if not trie.contains(word):
                        print("Not in dictionary ", word)
        print("second")
        matches = re.finditer(regex1, contents, re.MULTILINE | re.DOTALL)
        for matchNum, match in enumerate(matches):
            for groupNum in range(0, len(match.groups())):
                comment = match.group(1)
                print("Comment is ", comment)
                comment = re.split("_| |\n|\.|/|-", comment)
                comment = [i.lower() for i in comment if (len(i) == 1 and (i == 'a' or i =='i')) or len(i) > 1]
                print("Comment list is ", comment)
                for word in comment:
                    word_l = list(word)
                    #for i, letter in enumerate(word_l):
                       # if letter in ['(', ')','[', ']', '{', '}', '"', ';', ',', '+',
                       #   '-', '!','<', '>', '%', '*', '&', '=', '/', '#', "'", '|', ':' ]:
                         #   del(word_l[i])
                    word = CommentChecker.list_to_string(word_l)
                                                
                    if not trie.contains(word.lower()):
                        print("Not in dictionary ", word)
            

        
        
    def do_something(self, trie):
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
                    CommentChecker.check_comments(os.path.join(root, entry), trie)
            if len(dir) == 0:
                break
            root = dir[0]
            del[dir[0]]


