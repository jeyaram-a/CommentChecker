
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

    @staticmethod
    def enqueue(list, node):
        list.append(node)

    @staticmethod
    def dequeue(list):
        first = list[0]
        del list[0]
        return first

    @staticmethod
    def find_unique_node_for_each_letter(children):
        alphabets = {}
        for node in children[0:len(children)-1]:
            if node.char not in alphabets:
                alphabets[node.char] = node

        return alphabets


    @staticmethod
    def enqueue_children(children):
        i = 0
        while children[i] != "NULL":
            for letter in children[i].next:
                children.append(children[i].next[letter])
            i += 1

        DAWG.enqueue(children, "NULL")

    @staticmethod
    def detach_parents(parent, children):

        while children[0] != "NULL":
            DAWG.enqueue(parent, children[0])
            DAWG.dequeue(children)

        DAWG.dequeue(children)

    @staticmethod
    def remap(parent, unique_nodes_for_each_letter):
        for parent_node in parent:
            for key in parent_node.next:
                next_letter = parent_node.next[key]
                parent_node.next[key] = unique_nodes_for_each_letter[key]

    def reduce(self):
        parent = []
        children = []

        current = self.start

        for letter in current.next:
            children.append(current.next[letter])

        children.append("NULL")

        #while len(children) != 0:
        for i in range(0,1):
            DAWG.enqueue_children(children)
            DAWG.detach_parents(parent, children)
            unique_nodes_for_each_letter = DAWG.find_unique_node_for_each_letter(children)
            print("starting to remap")
            DAWG.remap(parent, unique_nodes_for_each_letter)
            print("done remapping")



def print_(l):
    for x in l:
        if type(x) == str:
            print(x)
        else:
            print(x.char)





d = DAWG()
d.add("achan")
d.add("aaryan")
d.add("ball")
d.add("cat")
d.print()
d.reduce()
d.print()
