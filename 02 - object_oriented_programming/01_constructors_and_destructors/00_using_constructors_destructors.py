class Dog:
    def __init__(self, name, color, awake=True):
        print("Initializing the class...")
        self.name = name
        self.color = color
        self.awake = awake

    def __del__(self):
        print("Removing the class instance.")

    def bark(self):
        print("woof woof")


def create_dog():
    c = Dog("Zeus", "Black and white", False)
    print(c.name)


c = Dog("Chappie", "yellow")
c.bark()

print("Hello world")

del c

print("Hello world")
print("Hello world")
print("Hello world")

# create_dog()