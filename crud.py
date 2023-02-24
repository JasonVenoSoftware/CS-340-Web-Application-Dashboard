from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self):
        self.client = MongoClient('mongodb://aacuser:Password1234@localhost:29721/AAC')
        self.database = self.client['AAC']


    # 'C' in CRUD, inserts document into database
    def create(self, data):
        if data is not None:
            insert_result = self.database.animals.insert(data) # data (dictionary) is inserted into 'animals' collection
            if insert_result is not None: # Checks whether insert was successful
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    # 'R' in CRUD, querys for documents and returns results
    def read(self, data):
        if data is not None: # Verify that search criteria was provided
            animalsCollection = list(self.database.animals.find(data, {"_id": False}))
            return animalsCollection
        else:
            raise Exception("No search criteria provided")
            return False


    # 'U' in CRUD, querys for document and updates it
    def update_document(self, query, data):
        if data is not None: # Verify that search criteria was provided
            data_update = self.database.animals.update_one(query, data) # Updates data
            return data_update
        else:
            raise Exception("Nothing to update, because data parameter is empty")


    # 'D' in CRUD, querys for document and deletes it
    def delete(self, data):
        if data is not None:
            data_delete = self.database.animals.delete_one(data)
            return data_delete
        raise Exception("Nothing to delete, because data parameter is empty")
