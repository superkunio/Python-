import pymongo


conn = pymongo.MongoClient('localhost',27017)

db = conn.grade

mySet = db.stuInfo
#按照性别分组，统计每组人数
agg = [{'$group':{'_id':'$sex','count':{'$sum':1}}},
       {'$match':{'count':{'$gt':9}}}
       ]
#按照性别分组，统计每组人数
agg2 = [{'$group':{'_id':'$sex','count':{'$sum':1}}},]
#统计每名男生的语文成绩
agg3 = [{'$match':{'sex':'m'}},
        {'$project':{'_id':0,'name':1,'score.yu':1}}]
#将女生按照英语成绩降序排列
agg4 = [{'$match':{'sex':'f'}},
        {'$sort':{'score.wai':-1}},
        {'$project':{'_id':0,'sex':1,'score.wai':1}}]
cursor = mySet.aggregate(agg4)

for x in cursor:
    print(x)


conn.close()