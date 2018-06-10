from classes.DataMartEtl import DataLoader
import sys

EtlTest = DataLoader()

try:
    EtlTest.MarketplaceItem('sonymarketplace')
    EtlTest.InsertMarketEntry('sonymarketplace')
    EtlTest.InsertCategory('sonymarketplace')
    EtlTest.InsertCategoryType('sonymarketplace')
    EtlTest.InsertMarketitemRelationship('sonymarketplace')
except:
    print('sonymarketplace - failed.'+str(sys.exc_info()[0]))
