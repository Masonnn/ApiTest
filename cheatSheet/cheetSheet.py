# created for learn

def greet_user(username):
    # """Display a personalized greeting."""
    print("Hello, " + username + "!")


greet_user("Jesse")


def make_pizza(topping='bacon'):
    """Make a single-topping pizza."""
    print("Have a " + topping + " pizza!")


make_pizza()
make_pizza('pepper oni')


def add_number(x, y):
    """Add two numbers and return the sum."""
    return x + y


sumValue = add_number(3, 5)
print(sumValue)
