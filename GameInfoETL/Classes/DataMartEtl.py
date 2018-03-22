import petl as etl
import psycopg2

class DataLoader():
    
    def ConnectEtl():
        connection=psycopg2.connect()
        return connection

    def MarketplaceItem(
        self,source
        ):
        if source is 'sonymarketplace':
            connection = self.ConnectEtl()
            etl.fromdb(lambda: connection.cursor(name='InsertMarketplaceItem'),"INSERT INTO etltables.marketplaceitem (marketplaceitemid, title, consoleid, businessentityid, etlsource,insertdatetime) SELECT (select COALESCE(max(marketplaceitemid),1) from etltables.marketplaceitem), sonywebsite.game_name as title,console.consoleid,businessentity.businessentityid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite LEFT JOIN etltables.console console ON COALESCE(sonywebsite.console_type,'Unknown') = console.consolename LEFT JOIN etltables.businessentity businessentity ON 'Unknown' = businessentity.businessname;")
        elif source is 'steammarketplace':
            connection = self.ConnectEtl()



    def InsertMarketEntry(
        self,source
        ):
        if source is 'sonymarketplace':
            connection = self.ConnectEtl()
            etl.fromdb(lambda: connection.cursor(name='InsertMarketEntry'),"INSERT INTO etltables.marketentry (marketentryid, sourcemarketidentifier, primaryprice, sourceurl, gameimageurl, reviewsurl, marketplaceitemid,etlsource,insertdatetime)  SELECT (select COALESCE(max(marketentryid),1) from etltables.marketentry) as marketentryid,COALESCE(etlsource.sourceid,(SELECT sourceid from etltables.source WHERE sourcename = 'Unknown'))  as sourcemarketidentifier,to_number(sonywebsite.badge_sale,'9,999.99')  as primaryprice,NULL  as sourceurl,sonywebsite.image  as gameimageurl,NULL  as reviewsurl,marketplaceitem.marketplaceitemid as marketplaceitemid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite LEFT JOIN etltables.source etlsource ON 'Sony Online Store' = etlsource.sourcename LEFT JOIN etltables.console console ON COALESCE(sonywebsite.console_type,'Unknown') = console.consolename LEFT JOIN etltables.businessentity businessentity ON 'Unknown' = businessentity.businessname LEFT JOIN etltables.marketplaceitem marketplaceitem	ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid AND businessentity.businessentityid = marketplaceitem.businessentityid")
        elif source is 'steammarketplace':

    def InsertCategory(
        self,source
        ):
        if source is 'sonymarketplace':
            connection = self.ConnectEtl()
            etl.fromdb(lambda: connection.cursor(name='InsertCategory'),"")

        elif source is 'steammarketplace':

    
    def InsertCategoryType(
        self,source
        ):
        if source is 'sonymarketplace': #SonyMarketplace uses the schema as the driver for the load of this table.
            connection = self.ConnectEtl()
            etl.fromdb(lambda: connection.cursor(name='InsertCategory'),"INSERT INTO etltables.categorytype (categorytypeid,categorytypename,etlsource,insertdatetime) SELECT (SELECT COALESCE(MAX(categorytype.categorytypeid),1) FROM etltables.categorytype) as categorytypeid, isc.column_name as categorytypename,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM INFORMATION_SCHEMA.COLUMNS isc WHERE table_schema = 'scraperdata' AND table_name = 'sonywebsite';)")
        elif source is 'steammarketplace':
  
    #def InsertSource(self,source): Not necessary at this time. Faster to manual insert.

    #def InsertBusinessEntity(self,source): Not necessary at this time. Faster to manual insert.

    #def InsertConsole(self,source): Not necessary at this time. Faster to manually insert.