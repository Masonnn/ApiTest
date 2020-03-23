# 啦啦啦

class Dog():
    """Represent a dog."""

    def __init__(self, name):
        """Initialize dog object."""
        self.name = name

    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")


my_dog = Dog('Peso')

print(my_dog.name + " is a great dog!")
my_dog.sit()


