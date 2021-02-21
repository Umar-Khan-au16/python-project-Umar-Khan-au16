import pickle

class DataStore:

    def __init__(self):
        self.rider_filename = "assets/rider.pk1"
        self.driver_filename = "assets/driver.pk1"

    def write_file(self, filename, file_data):
        ffile=open(filename,'wb')
        pickle.dump(file_data,ffile)
        ffile.close()

    def read_file(self, filename):
        ffile=open(filename,'rb')
        file_data = pickle.load(ffile)
        ffile.close()
        return file_data
        
    def read_rider_info(self):
        return self.read_file(self.rider_filename)

    def write_rider_info(self, rider_info:dict):
        self.write_file(self.rider_filename, rider_info)
        print("Rider info has been stored to database")

    def read_driver_info(self):
        return self.read_file(self.driver_filename)
    
    def write_driver_info(self, driver_info:dict):
        self.write_file(self.driver_filename, driver_info)
        print("Driver info has been stored to database")
        
    
