from classes.DataMartEtl import DataLoader

try:
    EtlTest.MarketplaceItem('steammarketplace')
    EtlTest.InsertMarketEntry('steammarketplace')
    EtlTest.InsertCategory('steammarketplace')
    EtlTest.InsertMarketitemRelationship('steammarketplace')
    EtlTest.InsertBusinessEntity('steammarketplace')
except:
    print('steammarketplace - failed.')