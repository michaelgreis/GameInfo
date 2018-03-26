import petl as etl
import psycopg2

class DataLoader():
    def ConnectEtl():
        connection=psycopg2.connect("dbname='landingzone' user='datamartetl' host='lz-scraper.czn1pljrayu4.us-east-2.rds.amazonaws.com' password='AlexMichael'")
        return connection

    def MarketplaceItem(
        source
        ):
        if source is 'sonymarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.executemany("INSERT INTO datamart.marketplaceitem (marketplaceitemid, title, consoleid, businessentityid, etlsource,insertdatetime) SELECT (select COALESCE(max(marketplaceitemid),1) from datamart.marketplaceitem)+row_number() over () as marketplaceitemid, sonywebsite.game_name as title,console.consoleid,businessentity.businessentityid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite LEFT JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename LEFT JOIN datamart.businessentity businessentity ON 'Unknown' = businessentity.businessname ON CONFLICT DO NOTHING;",marketplaceitem_insert)
            except:
                connection.commit()
        #elif source is 'steammarketplace':
            #connection = self.ConnectEtl()
        connection.commit()
        cur.close()
        connection.close()


    def InsertMarketEntry(
        source
        ):
        if source is 'sonymarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.executemany("INSERT INTO datamart.marketentry (marketentryid, sourceid, primaryprice, sourceurl, gameimageurl, reviewsurl, marketplaceitemid,etlsource,insertdatetime)  SELECT (select COALESCE(max(marketentryid),1) from datamart.marketentry)+row_number() over () as marketentryid,COALESCE(etlsource.sourceid,(SELECT sourceid from datamart.source WHERE sourcename = 'Unknown'))  as sourceid, CASE WHEN sonywebsite.badge_sale = 'Free' THEN 0 WHEN badge_sale = 'Unknown' THEN -1  ELSE to_number(sonywebsite.badge_sale,'L9999.99') END as primaryprice, NULL  as sourceurl,sonywebsite.image  as gameimageurl,NULL  as reviewsurl,marketplaceitem.marketplaceitemid as marketplaceitemid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite LEFT JOIN datamart.source etlsource ON 'Sony Online Store' = etlsource.sourcename LEFT JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename LEFT JOIN datamart.businessentity businessentity ON 'Unknown' = businessentity.businessname LEFT JOIN datamart.marketplaceitem marketplaceitem	ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid AND businessentity.businessentityid = marketplaceitem.businessentityid ON CONFLICT DO NOTHING;",marketentry_insert)
            except:
                connection.commit()
        #elif source is 'steammarketplace':
        connection.commit()
        cur.close()
        connection.close()



    def InsertCategory(
        source
        ):
        if source is 'sonymarketplace': # logic contained here is for two categories. Plus sale and item type (bundle, game, etc.). The plus sale has logic to convert "free" to 0, and currency to a number.
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.executemany("INSERT INTO datamart.category (categoryid, categoryname, marketentryid, categorytypeid, etlsource, insertdatetime) SELECT (SELECT COALESCE(MAX(categoryid),1) from datamart.category)+row_number() over () as categoryid,CASE WHEN plus_sale = 'Free' THEN 0 ELSE to_number(plus_sale,'L9999.99') END as categoryname,marketentry.marketentryid as marketentryid, categorytype.categorytypeid as categorytypeid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite LEFT JOIN datamart.source etlsource ON 'Sony Online Store' = etlsource.sourcename LEFT JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename LEFT JOIN datamart.businessentity businessentity 	ON 'Unknown' = businessentity.businessname LEFT JOIN datamart.marketplaceitem marketplaceitem ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid AND businessentity.businessentityid = marketplaceitem.businessentityid LEFT JOIN datamart.marketentry marketentry ON etlsource.sourceid = marketentry.sourceid AND CASE WHEN sonywebsite.badge_sale = 'Free' THEN 0 WHEN badge_sale = 'Unknown' THEN -1  ELSE to_number(sonywebsite.badge_sale,'L9999.99') END = marketentry.primaryprice AND marketplaceitem.marketplaceitemid = marketentry.marketplaceitemid LEFT JOIN datamart.categorytype categorytype ON 'plus_sale' = categorytype.categorytypename WHERE sonywebsite.plus_sale <> 'Unknown' ON CONFLICT DO NOTHING;",category_insert) #plus sale
            except:
                connection.commit()
            try:
                cur.executemany("INSERT INTO datamart.category (categoryid, categoryname, marketentryid, categorytypeid, etlsource, insertdatetime) SELECT (SELECT COALESCE(MAX(categoryid),1) from datamart.category)+row_number() over () as categoryid,item_type as categoryname,marketentry.marketentryid as marketentryid, categorytype.categorytypeid as categorytypeid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite LEFT JOIN datamart.source etlsource ON 'Sony Online Store' = etlsource.sourcename LEFT JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename LEFT JOIN datamart.businessentity businessentity 	ON 'Unknown' = businessentity.businessname LEFT JOIN datamart.marketplaceitem marketplaceitem ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid AND businessentity.businessentityid = marketplaceitem.businessentityid LEFT JOIN datamart.marketentry marketentry ON etlsource.sourceid = marketentry.sourceid AND CASE WHEN sonywebsite.badge_sale = 'Free' THEN 0 WHEN badge_sale = 'Unknown' THEN -1  ELSE to_number(sonywebsite.badge_sale,'L9999.99') END = marketentry.primaryprice AND marketplaceitem.marketplaceitemid = marketentry.marketplaceitemid LEFT JOIN datamart.categorytype categorytype ON 'item_type' = categorytype.categorytypename WHERE sonywebsite.item_type <> 'Unknown ON CONFLICT DO NOTHING;",category_insert)#item type
            except:
                connection.commit()
        #elif source is 'steammarketplace':
        connection.commit()
        cur.close()
        connection.close()


    
    def InsertCategoryType(
        source
        ):
        if source is 'sonymarketplace': #SonyMarketplace uses the schema as the driver for the load of this table.
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.execute("INSERT INTO datamart.categorytype (categorytypeid,categorytypename,etlsource,insertdatetime) SELECT (SELECT COALESCE(MAX(categorytype.categorytypeid),1) FROM datamart.categorytype)+row_number() over ()  as categorytypeid, isc.column_name as categorytypename,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM INFORMATION_SCHEMA.COLUMNS isc WHERE table_schema = 'scraperdata' AND table_name = 'sonywebsite' ON CONFLICT DO NOTHING;",categorytype_insert)
            except:
                connection.commit()
        #elif source is 'steammarketplace':
        connection.commit()
        cur.close()
        connection.close()

  
    #def InsertSource(self,source): Not necessary at this time. Faster to manual insert.

    #def InsertBusinessEntity(self,source): Not necessary at this time. Faster to manual insert.

    #def InsertConsole(self,source): Not necessary at this time. Faster to manually insert.