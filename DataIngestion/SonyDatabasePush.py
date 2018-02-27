from classes.databasepush import datapush
import os

data_location = '/crawler/data/'
data_source = 'sonymarketplace' #added for when this class started being used in multiple location (function insert_execute_script)

dp = datapush()

os.chdir(data_location) #changing directory to the file location
for filename in os.listdir(os.getcwd()):
    json_data = []
    #print(type(json_data))
    try:
        json_data = dp.read_data(filename)
        #print(type(json_data))
        dp.push_data(json_data, data_source)
        #break #just used for testing. don't want it to run through every file.
        os.remove(filename)
    except:
        print('failed to read '+filename)