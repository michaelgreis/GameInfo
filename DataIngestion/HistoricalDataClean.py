from classes.databasepush import datapush

dp = datapush()

source_to_clean = {"steammarketplace"}
day_number = 2

for source in source_to_clean:
    try:
        dp.history_removal(source,day_number)
    except:
        print('Failed to clean historical data for '+source+'.')