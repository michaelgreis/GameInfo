from classes.databasepush import datapush
import os

data_location = 'outputfiles/'

dp = datapush() #creating db object
dp.connect_to_db() #connecting to the database

os.chdir(data_location) #changing directory to the file location
json_data = dp.read_data('sony_scraper1512348947.1428585.json') #is json data being read correctly?
#print(json_data)
#print(json_data[3])
#print(json_data[3]['game_name'])

dp.push_data()