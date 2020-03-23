filename = 'test'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

filename = 'journal.txt'
with open(filename, 'w') as file_object:
    file_object.write('I Love Porgramming, 你试试. ')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

filename = '3.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games.")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

