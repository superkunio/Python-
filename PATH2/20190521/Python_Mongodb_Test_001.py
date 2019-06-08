import pymongo

#创建mongodb的数据库连接对象
conn = pymongo.MongoClient('localhost',27017)
#生成数据库对象
db = conn.stu
#生成class0的集合对象
mySet = db.class0
#操作集合

cursor = mySet.find({'$or':[{'sex':'F'},{'age':{'$lt':19}}]},{'_id':0})

for x in cursor:
    print(x)



conn.close()