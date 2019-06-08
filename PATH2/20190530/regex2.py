import re

pattern = r'(?P<dog>ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
match_obj = regex.search('abcdefghijlmnopq',pos = 0,endpos=6)

print(match_obj.pos)
print(match_obj.endpos)
print(match_obj.re)
print(match_obj.string)
print(match_obj.lastgroup)
print(match_obj.lastindex)
print(match_obj.start())
print(match_obj.end())
print(match_obj.span())
print(match_obj.lastindex)
print(match_obj.group(0))#获取整个match对象内容
print(match_obj.group(2))#获取第二个子组匹配内容
print(match_obj.group('dog'))#获取dog子组匹配内容
print(match_obj.groupdict())
print(match_obj.groups())












