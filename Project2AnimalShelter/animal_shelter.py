from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33019
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None:
                self.database.animals.insert_one(data)  # data should be dictionary            
            else:
                raise Exception("Nothing to save, because data parameter is empty")
            return True
        except Exception as e:
            print(f"failed to create data: {e}")
            return False

# Create method to implement the R in CRUD.
    def read(self, query):
        try:
            cursor = self.collection.find(query);

            results = list(cursor)
          
            return results if results else []
        except Exception as e:
            print(f"failed to read data: {e}")
            return []
        
    # Update (U in CRUD)
    def update(self, query, update_data, multiple=False):
        try:
            if multiple:
                result = self.collection.update_many(query, update_data)
            else:
                result = self.collection.update_one(query, update_data)
                
            return result.modified_count
        except Exception as e:
            print(f"Failed to update data: {e}")
            return 0

    # Delete (D in CRUD)
    def delete(self, query, multiple=False):
        try:
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)

            return result.deleted_count
        except Exception as e:
            print(f"Failed to delete data: {e}")
            return 0
        
animal = AnimalShelter()