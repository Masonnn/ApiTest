from collections import OrderedDict

# 列表嵌套存储字典
users = [{
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi'
}, {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie'
}]

# new_user = {
#     'last': 'fermi',
#     'first': 'enrico',
#     'username': 'efermi'
# }
# users.append(new_user)
#
# new_user = {
#     'last': 'curie',
#     'first': 'marie',
#     'username': 'mcurie'
# }
# users.append(new_user)

for user_dict in users:
    for k, v in user_dict.items():
        print(k + " : " + v)
    print("\n")

# 字典嵌套存储列表
fav_lang = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, langs in fav_lang.items():
    print(name + ": ")
    for lang in langs:
        print("  - " + lang)

# 字典嵌套字典

users = {
    'aeinstein': {
        'first': 'Albert',
        'last': 'Einstein',
        'location': 'Princeton'
    },
    'mcurie': {
        'first': 'Marie',
        'last': 'Curie',
        'location': 'Paris'

    }
}

# order dict
fav_languages = OrderedDict()

