def make_pizza(size, *toppings):
    print("Making a " + size + " pizza.")
    print("\n Toppings: ")

    for toppings in toppings:
        print("- " + toppings)


make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')


def build_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_0 = build_profile('Albert', 'Einstein', location='Princeton')
user_1 = build_profile('Marie', 'Curie', location='Paris', field='Chemistry')

print(user_0)
print(user_1)
