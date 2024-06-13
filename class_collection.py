#hand in a row from the csv file and try to get each var from it...


class Collection:
    def __init__(self, row):
        self.row = row #from csv file pulled apart for the vars below
        self.id = "ID???"
        self.collector = "Collector???"
        self.collectorsID = "CollectorID???"
        self.day = 0
        # self.month = "month???"
        self.monthInt = 0
        self.month = "month???"
        self.state = "state???"
        self.locality = "locality???"
        self.herbarium = "herbarium???"
        self.latitudeString = "???" #check it exists before converting to float
        self.longitudeString = "???" #check it exists before converting to float
        self.latitude = "lat???"
        self.longitude = "long???"
        self.region = "region???"
        self.type = "type???"
        
        
        #Private Functions ##################################################
        def _set_month_name(month_index):
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            if month_index != '':
              self.month = months[int(month_index)]
              
        ##collection id               
        try:
             self.id = row['catalogNumber']
        except KeyError:
            print("class_collection.py: catalogNumber column not found.")
        
        ##collector   
        try:
             self.collector = row['recordedBy']
        except KeyError:
            print("class_collection.py: recordedBy column not found.")
            
        ##collector id
        try:
             self.collectorsID = row['recordNumber']
        except KeyError:
            print("class_collection.py: recordNumber column not found.")
            
        ##day
        try:
            self.day = row['day']
        except KeyError:
            print("class_collection.py: day column not found.")
            
        ##month
        try:
             self.monthInt = row['month']
             _set_month_name(row['month'])
        except KeyError:
            print("class_collection.py: month column not found.")
            
        ##year
        try:
             self.year = row['year']
        except KeyError:
            print("class_collection.py: year column not found.") 
            
        ##state
        try:
             self.state = row['stateProvince']
        except KeyError:
            print("class_collection.py: stateProvince column not found.")
            
        ##location
        try:
             self.locality = row['locality']
        except KeyError:
            print("class_collection.py: locality column not found.")
            
        ##herbarium 
        try:
             self.herbarium = row['institutionCode']
        except KeyError:
            print("class_collection.py: institutionCode column not found.")
            
        ##latitude 
        try:
            lat_string = row['decimalLatitude']
            if lat_string != "":
                self.latitude = float(lat_string)
        except KeyError:
            print("class_collection.py: decimalLatitude column not found.")
        
        ##longitude
        try:
            long_string = row['decimalLongitude']
            if long_string != "":
                self.longitude = float(long_string)
        except KeyError:
            print("class_collection.py: decimalLongitude column not found.")
            
        ##bioregion
        try:
            if len(row['bioRegion']) > 1:
             self.region = row['bioRegion']
        except KeyError:
            print("class_collection.py: bioRegion column not found.")
            
        ##type status
        try:
             if len(row['typeStatus']) > 1:
                  self.type = row['typeStatus'] 
        except KeyError:
            print("class_collection.py: typeStatus column not found.")
     
     
     
     
    
    ##Format details for this collection ##################################################     
    def _formatLocality(self):
        if self.locality.endswith("."):
            self.locality = self.locality[:-1]
        result = "" if not self.locality else self.locality + ", "
        return result 
    
    def _formatCollectors(self):
        collectors = self.collector.split(" | ")
        result = ""
        for collector in collectors:
                result += self._formatCollector(collector)
        lastCharRemoved = result.rsplit(" & ", 1)
        result = " ".join(lastCharRemoved) # replace the last &
        return result
               
    
    def _formatCollector(self, collector):
        parts = collector.split(", ")
        if len(parts) > 1:
            result = parts[1] + " " + parts[0] 
        else:
            result = collector
        return result + " & "
    
    def _formatCollectorsID(self):
        result = "" if not self.collectorsID else self.collectorsID + ", "
        return result
    
    def _formatDate(self):
        shortened_month = self.month[:3] + "." if len(self.month) > 4 else self.month
        return self.day + " " + shortened_month + " " + self.year + ", "
            
    def _formatID(self):
        return "(" + self.id.split('.')[0] + "); " 
    
    # def _formatTypeStatus(self):
    #     # result = "" if self.type == "???" else self.type.upper() + ": "
    #     result = self.type.upper() + ": "
    #     return result
    
    
    #Public function ################################################################# 
    def details(self):
        return( self._formatLocality() + self._formatCollectors() + self._formatCollectorsID() + self._formatDate() + self._formatID())
        
    

    

            
        


