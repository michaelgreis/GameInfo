import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) #used to allow relative file imports.

from classes.DataMartEtl import DataLoader

EtlTest = DataLoader
# Test case 1, connection working?
try:
    DataLoader.ConnectEtl()
    #ConnectTest2 = DataMartEtl.DataLoader.ConnectEtl()
except:
    print('ConnectETL failed. Troubleshoot the ConnectEtl class/permissions/network.\r'+str(sys.exc_info()[0]))

#Test cases 2. Check each of the loads for the sony marketplace.
try:
    try:
        EtlTest.MarketplaceItem('steammarketplace')
        print('Insert Marketplace Item - SteamMarketplace - Successful.')
    except:
        print('Insert Marketplace Item - steammarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertMarketEntry('steammarketplace')
        print('Insert Market Entry Item - SteamMarketplace - Successful.')
    except:
        print('Insert Market Entry - steammarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertCategory('steammarketplace')
        print('Insert Category - SteamMarketplace - Successful.')
    except:
        print('Insert Category - steammarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertMarketitemRelationship('steammarketplace')
        print('Insert Market Item Relationship - SteamMarketplace - Successful.')
    except:
        print('Insert Market Item Relationship - steammarketplace - failed.' + str(sys.exc_info()[0]))
    try:
        EtlTest.InsertBusinessEntity('steammarketplace')
        print('Insert Business Entity - SteamMarketplace - Successful')
    except:
        print('Insert Business Entity - SteamMarketplace - Failed.')

except:
    print('steammarketplace - ETL Failed')