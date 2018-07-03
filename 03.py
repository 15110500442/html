import re
f = open('01.txt','r')
a = str(f.read())

b = r'\n|<\w*>|</\w*>|&nbsp;'
ret = re.split(b,a)
print(ret[0])
