from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import datetime
import json



def connect_mongo(host='localhost', port=27017, username=None, password=None, db='myapp-database'):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
        
    else:
        conn = MongoClient(host, port)

    try:
        # The ping command is cheap and does not require auth.
        conn.admin.command('ping')
        print("managed to ping the database")
        
    except ConnectionFailure:
        print("Server not available")

    return conn[db]

db = connect_mongo()





if __name__ == "__main__":

    # adding existing dta from json: 

    data_to_add = ["courses","users"]

    for dataset in data_to_add:

        Collection = db[dataset]
    
        # Loading or Opening the json file
        filename = str("datamodels/" + dataset + ".json")
        with open(filename) as file:
            file_data = json.load(file)
            
        # Inserting the loaded data in the Collection
        # if JSON contains data more than one entry
        # insert_many is used else inser_one is used
        if isinstance(file_data, list):
            Collection.insert_many(file_data)  
        else:
            Collection.insert_one(file_data)