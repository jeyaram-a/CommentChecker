import sys
import re
import os
from optparse import OptionParser
from Trie import Trie
from TokenCollector import TokenCollector
from CommentChecker import CommentChecker


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('\r[%s] %s%s ...%s' % (bar, percents, '%', status))
    sys.stdout.flush()


parser = OptionParser()
parser.add_option('-i', '--include', dest = 'include', help ='Includes the file contents in dictionary', metavar = 'FILE')
parser.add_option('-e', '--exclude', dest = 'exclude', help ='Excludes anything that matches the pattern', metavar = 'FILE')
parser.add_option('-c', '--check', dest = 'check', help ='Includes the file contents in dictionary', metavar = 'FILE')

(options, args) = parser.parse_args()
print(options.include)
print(options.exclude)
if options.check == None:
    print("No files to check")
    print("Exiting")
    sys.exit()
    exclude = []
if options.exclude != None:
    exclude = re.split(" ",  options.exclude)
file = open('words.txt', 'r')
line = file.readline()
count = 0
t = Trie()
i = 0

while line != "":
    if i % 100 == 0:
        progress(i, 466454, status="Loading words")
    i += 1
    t.count += 1
    line = line[0:len(line)-1]
    t.add(line.lower())
    line = file.readline()
print("\n")

if not options.include == None:
    include = options.include
    include = re.split(" ", include)

    for f in include:
        file = open(str(os.path.join(os.getcwd(), f)), "r")
        line = file.readline()
        while line != "":
             i += 1
             t.count += 1
             line = line[0:len(line)-1]
             t.add(line.lower())
             line = file.readline()
print("\n")

token_collector = TokenCollector(options.check, exclude)
all_tokens = token_collector.get_tokens()
count = 0
token_count = len(all_tokens)


for token in all_tokens:
    count += 1
    progress(count, token_count, status="Loading tokens")
    t.add(token)
print("\n")
cc = CommentChecker(options.check, exclude)
cc.do_something(t)

