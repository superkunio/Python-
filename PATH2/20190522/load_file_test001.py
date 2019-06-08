import pymongo

conn = pymongo.MongoClient('127.0.0.1',27017)

db = conn.video

mySet = db.video001

dataInfo = mySet.find_one({'filename':'vedio.mp4'})

with open('vedio002.mp4','wb') as f:
    f.write(dataInfo['data'])

conn.close()