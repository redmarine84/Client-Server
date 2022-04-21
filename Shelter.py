from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:54861' % (username, password))
            self.database = self.client['AAC']
        else:
            self.client = MongoClient('mongodb://localhost:54861')
            self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD. self.database.animals.find(data,{"_id":False})
    def create(self, data):
        if data is not None:
            if data:
                self.database.animals.insert(data)
                return True
        else:
            return False

# Create method to implement the R in CRUD. 
    def read(self, search):
        if search is not None:
            if search:
                result = self.database.animals.find(search, {"_id":False})
                return result
        else:
            raise Exception("Nothing to search, because search parameter is empty")
            
# Create method to implement the ReadAll in CRUD.             
    def read_all(self):
        return self.database.animals.find({},{"_id":False})
        
              
 # Create method to implement the U in CRUD
    def update(self,old_data,new_data):
        if old_data is not None:
            if old_data:
                updated = self.database.animals.update(old_data,new_data)
                self.database.animals.delete_one(old_data)
            return dumps(self.read(AnimalShelter, updated))
        else:
            raise Exception("Nothing to update, because data parameter is empty")
           
            
# Create method to implement the D in CRUD
    def delete(self, remove):
        if remove is not None:
            if remove:
                deleted = self.database.animals.delete_one(remove)
            return deleted #dumps(self.read(deleted))
        else:
            raise Exception("Nothing to delete, because data parameter is empty")