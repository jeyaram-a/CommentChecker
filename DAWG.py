
SOW = '^'
EOW = '$'

class DAWG_node :

    def __init__(self, char):
        self.char = char
        self.next = {}


class DAWG :

    def __init__(self):
        self.count = 0
        self.start = DAWG_node(SOW)
        self.start.next = {}

    @staticmethod
    def print_assist(current, word):

        if EOW in current.next:
            print(word)
            return

        for letter in current.next:
            DAWG.print_assist(current.next[letter], word+letter)

    def print(self):
        current = self.start
        word = ""

        for letter in current.next:
            DAWG.print_assist(current.next[letter], word+letter)


    def add(self, word):

        self.count += 1
        current = self.start
        for letter in word:
            if letter not in current.next:
                current.next[letter] = DAWG_node(letter)
                current = current.next[letter]
                continue
            else:
                current = current.next[letter]

        current.next[EOW] = DAWG_node(EOW)




d = DAWG()
d.add("amma")
d.add("achan")
d.add("cat")
d.add("company")
d.add("zeta")
d.print()
