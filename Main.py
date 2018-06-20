from Trie import Trie
import sys
import time

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
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

print("\n",t.contains("a-axzs"))




