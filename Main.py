from Trie import Trie
from TokenCollector import TokenCollector
from CommentChecker import CommentChecker
import sys

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('\r[%s] %s%s ...%s' % (bar, percents, '%', status))
    sys.stdout.flush()



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
token_collector = TokenCollector("./test",[".git", ".idea", "__pycache__", "words.txt"])
all_tokens = token_collector.get_tokens()
count = 0
token_count = len(all_tokens)

for token in all_tokens:
    count += 1
    progress(count, token_count, status="Loading tokens")
    t.add(token)
print("\n")
print("-------------------------", t.contains("apache"))
cc = CommentChecker("./test",[".git", ".idea", "__pycache__", "words.txt"])
cc.do_something(t)



    




