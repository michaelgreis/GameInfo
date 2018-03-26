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
        EtlTest.MarketplaceItem('sonymarketplace')
    except:
        print('Insert Marketplace Item - sonymarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertMarketEntry('sonymarketplace')
    except:
        print('Insert Market Entry - sonymarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertCategory('sonymarketplace')
    except:
        print('Insert Category - sonymarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertCategoryType('sonymarketplace')
    except:
        print('Insert Category Type - sonymarketplace - failed.'+str(sys.exc_info()[0]))
except:
    print('sonymarketplace - ETL Failed')