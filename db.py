import  json

class DB:
    def __init__(self,db_path):
        self.db_path= db_path

    def read(self):
        with open(self.db_path,'r') as f:
            self.data = json.load(f)

        return self.data
    def city(self,city):
        with open(self.db_path,'r') as f:
            self.data = json.load(f)

        return self.data['city'][f"{city}"]
    
