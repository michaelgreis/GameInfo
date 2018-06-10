from classes.databasepush import datapush
import os
import sys

data_location = '/crawlerdata/sony/'
data_source = 'sonymarketplace' #added for when this class started being used in multiple location (function insert_execute_script)

dp = datapush()

os.chdir(data_location) #changing directory to the file location
for filename in os.listdir(os.getcwd()):
    json_data = []
    #print(type(json_data))
    try:
        json_data = dp.read_data(filename)
        #print(type(json_data))
    except:
        print('failed to read '+filename)
    try:
        dp.push_data(json_data, data_source)
        os.remove(filename)
    except:
        os.rename(filename,"rejects/"+filename)
        print('failed to push '+filename,sys.exc_info()[0])
        #break #just used for testing. don't want it to run through every file.