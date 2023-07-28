import pymongo
from tabulate import tabulate

class MongoDBHelper:

    def __init__(self, collection='customer'):
        uri = "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        self.db = client['gw2023pds1']
        self.collection = self.db[collection]
        print("MongoDB Connected")

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document Inserted:", result)

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted:", result)

    def fetch(self):
        documents = self.collection.find()
        # for document in documents:
        #     print(document)

        print(tabulate(documents, headers="keys", tablefmt="grid"))
