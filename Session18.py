"""

    mongodb.com
    1. Create Account on MongoDB Atlas
    2. Network Access -> 0.0.0.0/0
    3. Create DataBase user and password
    4. Navigate to Browse Collections > Create DataBase and a Colellction

    Reference Documentation -> https://pymongo.readthedocs.io/en/stable/
    pip install pymongo
    pip install pymongo[srv]

    If facing SSL certificate error


"""

import pymongo
import certifi # pip install certifi | If SSL error

# ca = certifi.where() # If SSL error

uri = "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
# client = pymongo.MongoClient(uri, tlsCAFile=ca) # If SSL error
db = client['gw2023pds1']
collections = db.list_collection_names()
# print(collections)

for collection in collections:
    print(collection)

documents = db['customer'].find()
for document in documents:
    print(document)
