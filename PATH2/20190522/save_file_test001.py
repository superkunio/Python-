#小容量文件写入mongodb的方法
#以直接转换为二进制格式插入到数据库的方法存储
import pymongo,bson

conn = pymongo.MongoClient('127.0.0.1',27017)

db = conn.video

mySet = db.video001

#存储内容
f = open('C:\\Users\\72654\\Desktop\\7B4E2C8C-4A72-41E3-B134-7E0DCBE3A733.mp4',
         'rb')
#将文件内容转换为可存储的二进制格式

content = bson.binary.Binary(f.read())

mySet.insert({'filename':'vedio.mp4','data':content,'size':'3.67 MB'})

f.close()
conn.close()