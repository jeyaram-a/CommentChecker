
class DAWG_node :

    def __init__(self, char) :
        self.char = char
        self.next = None

class DAWG :

    def __init__(self):
        self.start = {}
        char = 'a'

        for i in range(0, 26) :
            self.start[char] = DAWG_node(char)
            char = chr(ord(char)+1)


    def print(self):
        char = 'a'
        for i in range(0, 26) :
            node = self.start[char]

            while node != None :
                print(node.char)
                node = node.next

            char = chr(ord(char)+1)

