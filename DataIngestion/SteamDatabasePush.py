from classes.databasepush import datapush
import os

data_location = '/crawlerdata/steam/'
data_source = 'steammarketplace'

dp = datapush()
os.chdir(data_location)
for filename in os.listdir(os.getcwd()):
    json_data = []
    try:
        json_data = dp.read_data(filename)
        #print(type(json_data))
    except:
        print('failed to read '+filename)
    try:
        dp.push_data(json_data,data_source)
        #break #just used for testing. don't want it to run through every file.
        os.remove(filename)
    except:
        try:
            os.rename(filename,"/crawlerdata/rejects/"+filename)
        except:
            print('Unable to relocate file to rejects.')
        print('failed to read '+filename)
        raise