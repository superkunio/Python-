import re
pattern = r'(ab)cd(ef)'
regex = re.compile(pattern)
s = 'abcdefghijklmnopqrstuvwxyz'
str = re.findall(pattern,s)
str1 = regex.findall(s)

print(str,str1)
print('-------------------------------------------------------')

l = re.split(r'\s+','Hello world nihao China')
print('split():',l)
print('-------------------------------------------------------')
l2 = re.sub(r'\s+','#','Hello world nihao China',2)
print(l2)
print('-------------------------------------------------------')
l3 = re.subn(r'\s+','#','Hello world nihao China',2)
print(l3)

