import datetime

fileName = 'time.txt'
f = open('time.txt')
open(fileName, 'w').write(str(datetime.date.today()))

print(open(fileName, 'r').read(4))

open(fileName, 'a').write(' \nI love making games.')

f.close()

