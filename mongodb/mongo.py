import pymongo

MONGODB_URI = "mongodb+srv://root:pass@myfirstcluster-2scdt.mongodb.net/myTestDB?retryWrites=true&w=majority"
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

'''
new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'gender': 'm',
            'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}

coll.insert(new_doc)
'''
'''
new_docs =[{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1946', 'gender': 'm',
            'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'},
            {'first': 'george', 'last': 'rr martin', 'dob': '29/09/1948', 'gender': 'm',
            'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]

coll.insert_many(new_docs)
'''
'''
coll.remove({'first': 'douglas'})
'''
'''
coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})
'''

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find()

for doc in documents:
    print(doc)
