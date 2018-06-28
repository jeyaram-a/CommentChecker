import os
import re
import sys

class TokenCollector:
    #root_path =start location for searching
    #ignore_pattern = folder or file to be ignored
    def __init__(self, root_path, ignore_pattern):
        self.root_path      = root_path
        self.ignore_pattern = ignore_pattern

    #returns all tokens (other than comments)
    @staticmethod
    def get_code(file_name):
        file_ = open(file_name, "r")
        file_contents = file_.read()
        file_contents_list = list(file_contents)
        file_length = len(file_contents_list)
        i = 0
        while file_length > 0:
            #dealing with block comments
            if i+1 < len(file_contents_list) and file_contents_list[i] == '/' and file_contents_list[i+1] == '*':
                del(file_contents_list[i])
                del(file_contents_list[i])
                while i+1 < len(file_contents_list) and ((file_contents_list[i] != '*' or file_contents_list[i+1] != '/')):
                    del(file_contents_list[i])
                    file_length -= 1
                del(file_contents_list[i])
                del(file_contents_list[i])
                file_length -= 4
            #dealing with single line comments
            if i+1 < len(file_contents_list) and file_contents_list[i] == '/' and file_contents_list[i+1] == '/' :
                del(file_contents_list[i])
                del(file_contents_list[i])
                while file_contents_list[i] != '\n':
                    del(file_contents_list[i])
                    file_length -= 1
                file_length -= 2
            i+=1
            file_length -= 1

        file_contents = ""
        i = 0
        while i < len(file_contents_list):
            if file_contents_list[i] in ['(', ')','[', ']', '{', '}', '"', ';', ',', '+',
                          '-', '!','<', '>', '%', '*', '&', '=', '/', '#', "'", '|', ':' ]:
                i += 1
                file_contents += " "
                continue
            if file_contents_list[i] == "\\" and file_contents_list[i+1] == 'n':
                i+=2
                continue
            file_contents += file_contents_list[i]
            i+=1
        return file_contents

    #Gets tokens from file contents
    @staticmethod
    def get_tokens_from_file(file_name):
        file_contents = TokenCollector.get_code(file_name)
        split_regex = "_| |\n|\.|=|\+|/|'|!|@|\(|\)|,|\"|:|\>|\<|;|#|\?|\*|-|{|}|[0-9]|\\\|\|\[|\]|&|\|"
        list_ = re.split(split_regex, file_contents)
        list_ = [i.lower() for i in list_ if (len(i) == 1 and (i == 'a' or i =='i')) or len(i) > 1]
        return list_

    #Reads all .c and .h files from root_path recursively and collects tokens
    def get_tokens(self):
        root = self.root_path
        dir = []
        all_tokens = []

        while True:
            for entry in os.listdir(root):
                if entry in self.ignore_pattern or os.path.isdir(os.path.join(root, entry)) in self.ignore_pattern:
                    continue
                if os.path.isdir(os.path.join(root, entry)):
                    dir.append(os.path.join(root, entry))
                else:
                    #Read only .c or .h files
                    if re.match(".*\.c$|.*\.h$",os.path.join(root, entry)):
                        sys.stdout.write("Collecting tokens from %s ..\n"%os.path.join(root, entry))
                        contents = TokenCollector.get_tokens_from_file(os.path.join(root, entry))
                        for token in contents:
                           if token not in all_tokens:
                                all_tokens.append(token)
            if len(dir) == 0:
                break
            root = dir[0]
            del[dir[0]]
        return all_tokens
