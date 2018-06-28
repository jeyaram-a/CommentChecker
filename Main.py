import sys
import re
import os

from optparse import OptionParser
from Trie import Trie
from TokenCollector import TokenCollector
from CommentChecker import CommentChecker

#Prints the progress bar
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('\r[%s] %s%s ...%s' % (bar, percents, '%', status))
    sys.stdout.flush()

#For command-line arguments
parser = OptionParser()
#Adding command-line options
parser.add_option('-i', '--include', dest = 'include', help ='Includes the file/files ie words that the user doesn\'t want to be flagged as spelling mistakes', metavar = 'FILE')
parser.add_option('-e', '--exclude', dest = 'exclude', help ='Includes the file/files ie words that the user doesn\'t want to be flagged as spelling mistakes', metavar = 'FILE')
parser.add_option('-c', '--check', dest = 'check', help ='Includes the file/files ie words that the user doesn\'t want to be flagged as spelling mistakes', metavar = 'FILE')
#Parse command-line arguments
(options, args) = parser.parse_args()

#If no files to check exit
if options.check == None:
    print("No files to check")
    print("Exiting")
    sys.exit()
    exclude = []
    
#Splitting exclude folders into list
if options.exclude != None:
    exclude = re.split(" ",  options.exclude)
    
#If not a valid path
if not (os.path.isdir(options.check) or os.path.isfile(options.check)):
    print("Check path \033[1;31m",options.check, "\033[0m not found")
    sys.exit()

#Opening the dictionary file
file = open('words.txt', 'r')

#Creating a trie
trie = Trie()

i = 0
line = file.readline()

#For every word in words.txt add the word to trie
while line != "":
    if i % 100 == 0:
        progress(i, 466454, status="Loading words")
    i += 1
    trie.count += 1
    line = line[0:len(line)-1]
    trie.add(line.lower())
    line = file.readline()
print("\n")

#If include file is specified
#   For every word in included file add it to trie
if not options.include == None:
    include = options.include
    include = re.split(" ", include)

    for f in include:
        try:
            file = open(os.path.join(os.getcwd(), f), "r")
            line = file.readline()
            while line != "":
                trie.count += 1
                line = line[0:len(line)-1]
                trie.add(line.lower())
                line = file.readline()
        except FileNotFoundError:
            print("Include file \033[1;31m",os.path.join(os.getcwd(), f), "\033[0m not found")
            sys.exit()
print("\n")

#Collect all tokens from the files
token_collector = TokenCollector(options.check, exclude)
all_tokens = token_collector.get_tokens()

count = 0
token_count = len(all_tokens)

#Add collected tokens to the trie
for token in all_tokens:
    count += 1
    progress(count, token_count, status="Loading tokens")
    trie.add(token)
print("\n")

#Check the comments
cc = CommentChecker(options.check, exclude)
cc.check_comments(trie)

