import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))

    print("printing directoreis ................")
    for name in dirs:
        print(os.path.join(root, name))


print("\n\n\n\n")

