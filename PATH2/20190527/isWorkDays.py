import re

str = re.findall(r'(\d{2,4}/\d{1,2}/\d{1,2}))','2019/5/28 22:11:00')


for x in str:
    print(x)