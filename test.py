class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(1, 2)
b = A(3, 4)

l = []
l.append(a)
l.append("hello")
l.append(b)

print(l)

for x in l:
    if x == "hello":
        print("found")