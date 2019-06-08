import re

it = re.finditer(r'\d+','2008-2018 这10年间中国发生了翻天覆地的变化')

for x in it:
    print(x.group())
#相当于绝对匹配
try:
    it2 = re.fullmatch(r'\w+','abcdef123#')
    print(it2.group())
except AttributeError as e:
    print(e,'result == None')

#相当于使用^
try:
    it3 = re.match(r'foo+','Foo,food on the ground')
    print(it3.group())
except AttributeError as e:
    print(e,'result == None')


#之匹配一处

try:
    it4 = re.search(r'fpp','Fpp,fpppp,fffpp')
    print(it4.group())
except AttributeError as e:
    print(e)

print(re.findall(r'\bis','This is a boy'))