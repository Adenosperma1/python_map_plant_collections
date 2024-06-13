# speciesClass.py
# public functions:
# get_locations() returns lats, longs : for all colections
# get_details_Nuytsia_formatted() returns string : for all collection details formatted for Nuytsia Journal


import csv
from class_collection import Collection

class Species:
    def __init__(self, genus, species, color, csvFilePath):
        self.genus = genus
        self.species = species
        self.label = genus + ' ' + species
        self.file_path = csvFilePath
        self.color = color
        self.collections = self._set_collections()
        self.locations = self._set_locations()
        
    

    def _set_locations(self):
        return [(collection.latitude, collection.longitude) for collection in self.collections]
           
    def _set_collections(self):
        collections = []

        try:
            with open(self.file_path, newline='') as csvfile:
                print("class_species.py: Reading cvs file for: " + str(self.species) + ".")
                reader = csv.DictReader(csvfile)
                for row in reader:
                    collection = Collection(row)
                    collections.append(collection)

        except FileNotFoundError:
            print("class_species.py: Error: CSV File not found:" + self.file_path)
            exit()
        collections_sorted = self._sort(collections)
        return collections_sorted

    def _sort(self, collections):
        return sorted(collections, key=lambda x: (x.state, x.region))
    
    def _replace_last(self, string, old, new):
        #not really sure how this works...
        line = string.rsplit(old, 1) #Split only once
        return new.join(line)
 
 
    

     
    #public functions ######################################################
    def get_locations(self):
        lats, longs = zip(*[(lat, long) for lat, long in self.locations if lat != "???" and long != "???"])
        return lats, longs

    #public function list collection details for Nuytsia Journal``
    def get_details_Nuytsia_formatted(self):
        details = "Selected specimens examined. "
        current_state = "" #only show the state once
        current_region = "" #only show the region once for each state
        
        for collection in self.collections:
            new_state = collection.state.upper()
            new_region = collection.region.upper()
            
            if not current_state or current_state != new_state:
                current_state = new_state
                details += current_state + ": "
            
            if not current_region or current_region != new_region:
                current_region = new_region
                details += current_region + ": "
                
            if collection.type == "type???": #dodgy if the default is changed in the class it will break here...
                # details += "TYPESTATUS: " + collection.type + ", "
                details += collection.get_details()
            
        result = self._replace_last(details, ';', '.')
        return result
   
            
