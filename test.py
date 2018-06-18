
class Test:

    def __init__(self, x, y):
        self._x = x
        self.__y = y


    def print(self):
       print(self._x)
       print(self.__y)

test = Test(5, 6)

#print(test.print())
print(test._x)