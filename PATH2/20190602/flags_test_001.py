import re

s = 'hello world'
str = '''hello world
hello kitty
你好，北京'''

pattern = r'Hello'
pattern2 = r'.+'
pattern3 = r'kitty$'
regex = re.compile(pattern3,flags = re.M)
try:
    s = regex.search(str).group()
except AttributeError as e:
    print('没有匹配到内容',e)
else:
    print(s)
