import re

path = 'C:\\Users\\72654\\Desktop\\001.txt'

f = open(path)

Info = f.read()
result = re.findall('\w*@\w*.\w*',Info)

print(Info)

print(result)