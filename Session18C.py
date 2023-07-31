from Session18A import Customer
from Session18B import MongoDBHelper
from bson.objectid import ObjectId


def main():

    db = MongoDBHelper()

    # customer = Customer()
    # customer.read_customer_data()
    #
    # document = vars(customer)
    #
    # db.insert(document)

    # query = {'phone': '+91 99999 11111'}
    query = {'email': 'george@example.com'}
    # query = {'_id': ObjectId('64c36bf9d883cf37f2fee6db')}
    # db.delete(query)

    # db.fetch()
    db.fetch(query=query)

    document_data_to_update = {'name': 'George W', 'phone': '+91 87654 87654', 'age': 33}
    db.update(document_data_to_update, query)


if __name__ == "__main__":
    main()