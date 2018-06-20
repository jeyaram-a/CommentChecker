
SOW = '^'
EOW = '$'

class Trie_node:
    def __init__(self, letter):
        self.letter = letter
        self.next   = {}

    def toString(self):
        return str(self.letter)



class Trie:

    def __init__(self):
        self.start = Trie_node("^")
        self.count = 0

    def add(self, word):
        self.count += 1
        current = self.start

        for letter in word:
            if letter in current.next:
                current = current.next[letter]
            else:
                current.next[letter] = Trie_node(letter)
                current = current.next[letter]
        current.next[EOW] = Trie_node(EOW)

    @staticmethod
    def contains_assist(current, word, pos):

        if EOW in current.next and pos == len(word):
            return True

        if pos >= len(word):
            return False

        if word[pos] in current.next:
            return Trie.contains_assist(current.next[word[pos]], word, pos+1)
        else:
            return False

    def contains(self, word):
        if len(word) == 0:
            return False

        current = self.start
        if word[0] in current.next:
            if Trie.contains_assist(current.next[word[0]], word, 1) == True:
                return True

        return False


    @staticmethod
    def print_assist(current, word):

        if EOW in current.next:
            print(word)

        for letter in current.next:
            Trie.print_assist(current.next[letter], word+letter)

    def print(self):
        current = self.start
        word = ""
        for letter in current.next:
            Trie.print_assist(current.next[letter], word+letter)

