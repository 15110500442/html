import re
f = open('01.txt','r')
a = str(f.read())

b = r'\n|<\w*>|</\w*>|&nbsp;'
ret = re.split(b,a)
for c in ret:
    if len(c) != 0:
        print(c)
