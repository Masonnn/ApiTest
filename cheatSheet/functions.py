# # learn function
#
# def greet_user(username='Hey'):
#     """Display a simple greeting."""
#     print('Hello, ' + username + '!')
#
#
# def des_pet(animal='spider', name=None):
#     print('I hava a ' + animal)
#     if name:
#         print('Its name is ' + name)
#
#
# greet_user()
# greet_user('Mason')
#
# des_pet('hamster', 'harry')
#
# des_pet(name='willie', animal='dog')
#
# des_pet('cat')
#
#
# def get_full_name(first, last):
#     full_name = first + ' ' + last
#     return full_name.title()
#
#
# hello = 'ni hao \n 呼噜娃'
#
# print(hello)
# print(hello.title())
# musician = get_full_name('jimi', 'hendrix')
# print(musician)
# print(musician.title())

def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name + '!'
        print(msg.title())


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


def print_models(unprinted, printed):
    while unprinted:
        cur_model = unprinted.pop()
        print('Printing ' + cur_model)
        printed.append(cur_model)


unprinted = ['phone case', 'pendant', 'ring']
printed = []
print_models(unprinted[:], printed)

print("\nUnprinted: ", unprinted)
print('Printed: ', printed)
