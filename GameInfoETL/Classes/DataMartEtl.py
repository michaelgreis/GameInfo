import petl as etl
import psycopg2

class DataLoader():
# each of the functions in this class are used for loading a single table. Right now, there are two sources for out data (4/7/2018). The first is sonywebsite. The second is steammarketplace, both in the scraperdata schema.
    def ConnectEtl():
        connection=psycopg2.connect("")
        return connection


    def MarketplaceItem(
        source
        ):
        if source is 'sonymarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.execute("INSERT INTO datamart.marketplaceitem (marketplaceitemid, title, consoleid, etlsource,insertdatetime) SELECT (select COALESCE(max(marketplaceitemid),1) from datamart.marketplaceitem)+row_number() over () as marketplaceitemid, sonywebsite.game_name as title,console.consoleid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite INNER JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
        elif source is 'steammarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.execute("INSERT INTO datamart.marketplaceitem (marketplaceitemid, title, alternatename, consoleid, etlsource, insertdatetime) SELECT (select COALESCE(max(marketplaceitemid),1) from datamart.marketplaceitem)+row_number() over () as marketplaceitemid, COALESCE(full_data::json->>'title',full_data::json->>'app_name') as title, CASE WHEN full_data::json->>'title' IS NOT NULL THEN full_data::json->>'app_name' ELSE NULL END AS alternatename, console.consoleid,    'steammarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.steammarketplace steammarketplace INNER JOIN datamart.console console ON 'PC' = console.consolename WHERE full_data::json->>'title' IS NOT NULL OR full_data::json->>'app_name' IS NOT NULL ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
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
                cur.execute("INSERT INTO datamart.marketentry (marketentryid, sourceid, primaryprice, sourceurl, gameimageurl, reviewsurl, marketplaceitemid,etlsource,insertdatetime)  SELECT (select COALESCE(max(marketentryid),1) from datamart.marketentry)+row_number() over () as marketentryid,COALESCE(etlsource.sourceid,(SELECT sourceid from datamart.source WHERE sourcename = 'Unknown'))  as sourceid, CASE WHEN sonywebsite.badge_sale = 'Free' THEN 0 WHEN badge_sale = 'Unknown' THEN -1  ELSE to_number(sonywebsite.badge_sale,'L9999.99') END as primaryprice, NULL  as sourceurl,sonywebsite.image  as gameimageurl,NULL  as reviewsurl,marketplaceitem.marketplaceitemid as marketplaceitemid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite INNER JOIN datamart.source etlsource ON 'Sony Online Store' = etlsource.sourcename INNER JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename INNER JOIN datamart.marketplaceitem marketplaceitem	ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
        elif source is 'steammarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.execute("INSERT INTO datamart.marketentry (marketentryid,releasedate, sourceid,primaryprice,sourceurl,gameimageurl,reviewsurl,marketplaceitemid, etlsource, insertdatetime) SELECT (select COALESCE(max(marketentryid),1) from datamart.marketentry)+row_number() over () as marketplaceitemid, LEFT(steammarketplace.full_data::json->>'release_date',25) as releasedate,etlsource.sourceid as sourceid, CAST(CASE WHEN steammarketplace.full_data::json->>'price' !~ '[0-9]' THEN '0' WHEN split_part(steammarketplace.full_data::json->>'price','$',2) <> '' THEN split_part(steammarketplace.full_data::json->>'price','$',2) ELSE steammarketplace.full_data::json->>'price' END AS DECIMAL(6,2)) as primaryprice,    steammarketplace.full_data::json->>'url' as sourceurl,steammarketplace.full_data::json->>'gameImage' as gameimageurl,steammarketplace.full_data::json->>'reviews_url' as reviewsurl, marketplaceitem.marketplaceitemid as marketplaceitemid, 'steammarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.steammarketplace steammarketplace INNER JOIN datamart.console console ON 'PC' = console.consolename INNER JOIN datamart.marketplaceitem marketplaceitem ON COALESCE(steammarketplace.full_data::json->>'title',steammarketplace.full_data::json->>'app_name') = marketplaceitem.title AND CASE WHEN steammarketplace.full_data::json->>'title' IS NOT NULL THEN steammarketplace.full_data::json->>'app_name' ELSE NULL END = marketplaceitem.alternatename AND console.consoleid = marketplaceitem.consoleid INNER JOIN datamart.source etlsource ON 'Steam Marketplace' = etlsource.sourcename ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
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
                cur.execute("INSERT INTO datamart.category (categoryid, categoryname, marketentryid, categorytypeid, etlsource, insertdatetime) SELECT (SELECT COALESCE(MAX(categoryid),1) from datamart.category)+row_number() over () as categoryid,CASE WHEN plus_sale = 'Free' THEN 0 ELSE to_number(plus_sale,'L9999.99') END as categoryname,marketentry.marketentryid as marketentryid, categorytype.categorytypeid as categorytypeid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite INNER JOIN datamart.source etlsource ON 'Sony Online Store' = etlsource.sourcename INNER JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename INNER JOIN datamart.businessentity businessentity 	ON 'Unknown' = businessentity.businessname INNER JOIN datamart.marketplaceitem marketplaceitem ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid INNER JOIN datamart.marketentry marketentry ON etlsource.sourceid = marketentry.sourceid AND CASE WHEN sonywebsite.badge_sale = 'Free' THEN 0 WHEN badge_sale = 'Unknown' THEN -1  ELSE to_number(sonywebsite.badge_sale,'L9999.99') END = marketentry.primaryprice AND marketplaceitem.marketplaceitemid = marketentry.marketplaceitemid INNER JOIN datamart.categorytype categorytype ON 'plus_sale' = categorytype.categorytypename WHERE sonywebsite.plus_sale <> 'Unknown' ON CONFLICT DO NOTHING;") #plus sale
            except:
                connection.commit()
            try:
                cur.execute("INSERT INTO datamart.category (categoryid, categoryname, marketentryid, categorytypeid, etlsource, insertdatetime) SELECT (SELECT COALESCE(MAX(categoryid),1) from datamart.category)+row_number() over () as categoryid,item_type as categoryname,marketentry.marketentryid as marketentryid, categorytype.categorytypeid as categorytypeid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite INNER JOIN datamart.source etlsource ON 'Sony Online Store' = etlsource.sourcename INNER JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename INNER JOIN datamart.marketplaceitem marketplaceitem ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid INNER JOIN datamart.marketentry marketentry ON etlsource.sourceid = marketentry.sourceid AND CASE WHEN sonywebsite.badge_sale = 'Free' THEN 0 WHEN badge_sale = 'Unknown' THEN -1  ELSE to_number(sonywebsite.badge_sale,'L9999.99') END = marketentry.primaryprice AND marketplaceitem.marketplaceitemid = marketentry.marketplaceitemid INNER JOIN datamart.categorytype categorytype ON 'item_type' = categorytype.categorytypename WHERE sonywebsite.item_type <> 'Unknown' ON CONFLICT DO NOTHING;")#item type
            except:
                connection.commit()
        elif source is 'steammarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try:
                cur.execute("INSERT INTO datamart.category (categoryid, categoryname, marketentryid, categorytypeid, etlsource,insertdatetime) SELECT (SELECT COALESCE(MAX(categoryid),1) FROM datamart.category) + row_number() over () as categoryid, LEFT(TRIM(BOTH '[]\"' FROM unnest(categoryname)),250) as categoryname, marketentry.marketentryid as marketentryid, categorytype.categorytypeid as categorytypeid,'steammarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM (SELECT full_data,json_object_keys(full_data) AS categorytypename, string_to_array(full_data->>json_object_keys(full_data),'\", \"','[\"') as categoryname FROM scraperdata.steammarketplace) AS steammarketplace INNER JOIN datamart.categorytype categorytype ON steammarketplace.categorytypename = categorytype.categorytypename INNER JOIN datamart.source etlsource ON 'Steam Marketplace' = etlsource.sourcename INNER JOIN datamart.console console ON 'PC' = console.consolename INNER JOIN datamart.marketplaceitem marketplaceitem ON COALESCE(steammarketplace.full_data::json->>'title',steammarketplace.full_data::json->>'app_name') = marketplaceitem.title AND CASE WHEN steammarketplace.full_data::json->>'title' IS NOT NULL THEN steammarketplace.full_data::json->>'app_name' ELSE NULL END = marketplaceitem.alternatename AND console.consoleid = marketplaceitem.consoleid INNER JOIN datamart.marketentry marketentry ON CAST(CASE WHEN steammarketplace.full_data::json->>'price' !~ '[0-9]' THEN '0' WHEN split_part(steammarketplace.full_data::json->>'price','$',2) <> '' THEN split_part(steammarketplace.full_data::json->>'price','$',2) ELSE steammarketplace.full_data::json->>'price' END AS DECIMAL(6,2)) = marketentry.primaryprice AND etlsource.sourceid = marketentry.sourceid AND marketplaceitem.marketplaceitemid = marketentry.marketplaceitemid AND LEFT(steammarketplace.full_data::json->>'release_date',25) = marketentry.releasedate ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
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
                cur.execute("INSERT INTO datamart.categorytype (categorytypeid,categorytypename,etlsource,insertdatetime) SELECT (SELECT COALESCE(MAX(categorytype.categorytypeid),1) FROM datamart.categorytype)+row_number() over ()  as categorytypeid, isc.column_name as categorytypename,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM INFORMATION_SCHEMA.COLUMNS isc WHERE table_schema = 'scraperdata' AND table_name = 'sonywebsite' ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
        connection.commit()
        cur.close()
        connection.close()

    def InsertBusinessEntity(
        source
        ): #necessary for the steam marketplace dataset.
        if source is 'steammarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try: # insert for publisher info into business entity
                cur.execute("INSERT INTO datamart.businessentity (businessentityid, businessname, etlsource, insertdatetime) SELECT (SELECT COALESCE(MAX(businessentityid),1) FROM datamart.businessentity)+row_number () over() as businessentityid, full_data::json->>'publisher' as businessname,'steammarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.steammarketplace as steammarketplace WHERE full_data::json->>'publisher' IS NOT NULL ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
            try: # insert into business entity for development studio.
                cur.execute("INSERT INTO datamart.businessentity (businessentityid, businessname, etlsource, insertdatetime) SELECT (SELECT COALESCE(MAX(businessentityid),1) FROM datamart.businessentity)+row_number () over() as businessentityid, steammarketplace.full_data::json->>'developer' as businessname,'steammarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.steammarketplace as steammarketplace WHERE steammarketplace.full_data::json->>'developer' IS NOT NULL ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
        connection.commit()
        cur.close()
        connection.close()

    def InsertMarketitemRelationship(
        source
        ):
        if source is 'sonymarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try: #define the relationship between themarketplaceitems and the business entitys.
                cur.execute("INSERT INTO datamart.MarketItemRelationship (marketplaceitemrelationshipid,relationshiptypeid, businessentityid, marketplaceitemid,etlsource,insertdatetime) SELECT (SELECT MAX(marketplaceitemrelationshipid) FROM datamart.marketplaceitemrelationship)+row_number() over() as marketplaceitemrelationshipid, relationshiptype.relationshiptypeid, businessentity.businessentityid as businessentityid, marketplaceitem.marketplaceitemid, 'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite INNER JOIN datamart.console console ON COALESCE(TRIM(split_part(sonywebsite.console_type,'|',1)),'Unknown') = console.consolename INNER JOIN datamart.marketplaceitem marketplaceitem ON sonywebsite.game_name = marketplaceitem.title AND console.consoleid = marketplaceitem.consoleid INNER JOIN datamart.RelationshipType relationshiptype ON 'Unknown' = relationshiptype.relationshipname INNER JOIN datamart.businessentity businessentity ON 'Unknown' = businessentity.businessname ON CONFLICT DO NOTHING;")
            except:
                connection.commit()
        if source is 'steammarketplace':
            connection = DataLoader.ConnectEtl()
            cur = connection.cursor()
            try: #this inserts business relationships into the relationship table. This is a complicated one. It first turns a single row into multiple rows (one for developer, one for publisher) the joins to the market entry table to get market items, and finally establishes the rleationship between the market entry and the business by joining to the relationshiptype and business entity table. So 3 steps. 1. create rows for developer and publisher, 2. establish relationship to market entry. 3. Relate the market entry to the business.
                cur.execute("INSERT INTO datamart.marketplaceitemrelationship (marketplaceitemrelationshipid,relationshiptypeid, businessentityid, marketplaceitemid, etlsource,insertdatetime) SELECT (SELECT MAX(marketplaceitemrelationshipid) FROM datamart.marketplaceitemrelationship)+row_number () over () as marketplaceitemrelationshipid,relationshiptype.relationshiptypeid as relationshiptypeid, businessentity.businessentityid as businessentityid,marketplaceitem.marketplaceitemid as marketplaceitemid,'steammarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM (SELECT COALESCE(steammarketplace_developer.full_data::json->>'title', steammarketplace_developer.full_data::json->>'app_name') as title, CASE WHEN steammarketplace_developer.full_data::json->>'title' IS NOT NULL THEN  steammarketplace_developer.full_data::json->>'app_name' ELSE NULL END AS alternatename,      steammarketplace_developer.full_data::json->>'developer' as businessname,'Developer' as relationshipname FROM scraperdata.steammarketplace steammarketplace_developer WHERE (steammarketplace_developer.full_data::json->>'title' IS NOT NULL OR steammarketplace_developer.full_data::json->>'app_name' IS NOT NULL) AND steammarketplace_developer.full_data::json->>'developer' IS NOT NULL UNION ALL SELECT COALESCE(steammarketplace_publisher.full_data::json->>'title', steammarketplace_publisher.full_data::json->>'app_name') as title, CASE WHEN steammarketplace_publisher.full_data::json->>'title' IS NOT NULL THEN  steammarketplace_publisher.full_data::json->>'app_name' ELSE NULL END AS alternatename, steammarketplace_publisher.full_data::json->>'publisher' as businessname, 'Publisher' as relationshipname FROM scraperdata.steammarketplace steammarketplace_publisher WHERE (steammarketplace_publisher.full_data::json->>'title' IS NOT NULL OR steammarketplace_publisher.full_data::json->>'app_name' IS NOT NULL) AND steammarketplace_publisher.full_data::json->>'publisher' IS NOT NULL ) steammarketplace INNER JOIN datamart.console console ON 'PC' = console.consolename INNER JOIN datamart.marketplaceitem marketplaceitem ON steammarketplace.title = marketplaceitem.title AND steammarketplace.alternatename = marketplaceitem.alternatename AND console.consoleid = marketplaceitem.consoleid INNER JOIN datamart.businessentity businessentity ON businessentity.businessname = businessentity.businessname INNER JOIN datamart.relationshiptype relationshiptype ON steammarketplace.relationshipname = relationshiptype.relationshipname")
            except:
                connection.commit()
