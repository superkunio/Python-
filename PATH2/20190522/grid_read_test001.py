#大容量文件对数据库的读取和写入
import pymongo,gridfs

conn = pymongo.MongoClient('localhost',27017)
db = conn.grid
#获取gridfs对象
fs = gridfs.GridFS(db)

files = fs.find()

#分别取每一个文件
for x in files:
    #打印每个文件名称
    print(x.filename)
    if x.filename =='video.mp4':
        with open(x.filename,'wb') as f:
            #从数据库读取内容
            data = x.read()
            #写入到本地
            f.write(data)


conn.close()