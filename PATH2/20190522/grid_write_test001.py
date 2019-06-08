#将文件以grid方案存放到数据库
import pymongo,gridfs

conn = pymongo.MongoClient('127.0.0.1',27017)

db = conn.grid

#获取gridfs对象，就可以将文件存入数据库
fs = gridfs.GridFS(db)

file = open('C:\\Users\\72654\\Desktop\\C9885986-6865-46B7-BF5A-C59141C28599.mp4',
            'rb'
            )
#将内容写入到数据库
fs.put(file.read(),filename = 'video.mp4')


file.close()
conn.close()