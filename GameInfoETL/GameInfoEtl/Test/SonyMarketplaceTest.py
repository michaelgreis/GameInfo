from ..DataMartEtl import DataLoader

EtlTest = DataLoader
# Test case 1, connection working?
try:
    DataLoader.ConnectEtl()
    #ConnectTest2 = DataMartEtl.DataLoader.ConnectEtl()
    print('Successful Connection Established.')
except:
    print('ConnectETL failed. Troubleshoot the ConnectEtl class/permissions/network.\r'+str(sys.exc_info()[0]))

#Test cases 2. Check each of the loads for the sony marketplace.
try:
    try:
        EtlTest.MarketplaceItem('sonymarketplace')
        print('Insert Marketplace Item - sonymarketplace - Success.')
    except:
        print('Insert Marketplace Item - sonymarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertMarketEntry('sonymarketplace')
        print('Insert Market Entry - sonymarketplace - Success.')
    except:
        print('Insert Market Entry - sonymarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertCategory('sonymarketplace')
        print('Insert Category - sonymarketplace - Success')
    except:
        print('Insert Category - sonymarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertCategoryType('sonymarketplace')
        print('Insert Category Type - sonymarketplace - Success')
    except:
        print('Insert Category Type - sonymarketplace - failed.'+str(sys.exc_info()[0]))
    try:
        EtlTest.InsertMarketitemRelationship('sonymarketplace')
        print('Insert Marketitem Relationship - sonymarketplace - Success')
    except:
        print('Insert Marketitem Relationship - sonymarketplace - failed.'+str(sys.exc_info()[0]))
except:
    print('sonymarketplace - ETL Failed')