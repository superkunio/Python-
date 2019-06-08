import re

f = open('C:\\Users\\72654\\Desktop\\test001.txt','rb')

novelInfo = f.read().decode('utf-8')
Number = r'-?\d+\.?/?\d*%?'#出现0~1次-、1~n次数字、0~1次.、
Capital = r'[A-Z]\w*'
result1 = re.findall(Capital,novelInfo)
result2 = re.findall(Number,novelInfo)
print(result1)
print(result2)