
--Insert for categories & screwing around with json.
SELECT *,
	TRIM(BOTH '[]"' FROM unnest(categoryname))
FROM (SELECT json_object_keys(full_data) as object_keys,
	--json_each(full_data::json->>json_object_keys(full_data)),
    full_data->>json_object_keys(full_data),
	string_to_array(full_data->>json_object_keys(full_data),'", "','["') as categoryname
	--json_array_elements(full_data)
FROM scraperdata.steammarketplace steammarketplace
--INNER JOIN datamart.categorytype categorytype
WHERE id = '427570') AS A




--Select from all tables (per 3.25.2018)
SELECT *
FROM datamart.businessentity
LIMIT 10;

SELECT *
FROM datamart.category
LIMIT 10;

SELECT *
FROM datamart.categorytype
LIMIT 10;

SELECT *
FROM datamart.console
LIMIT 10;

SELECT *
FROM datamart.marketentry
LIMIT 10;

SELECT *
FROM datamart.marketplaceitem
LIMIT 10;

SELECT *
FROM datamart.source
LIMIT 10;

SELECT *
FROM datamart.marketplaceitemrelationship
LIMIT 10;

--Select max date
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'businessentity'
FROM datamart.businessentity
GROUP BY etlsource
UNION ALL
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'category'
FROM datamart.category
GROUP BY etlsource
UNION ALL
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'categorytype'
FROM datamart.categorytype
GROUP BY etlsource
UNION ALL
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'console'
FROM datamart.console
GROUP BY etlsource
UNION ALL
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'marketentry'
FROM datamart.marketentry
GROUP BY etlsource
UNION ALL
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'marketplaceitem'
FROM datamart.marketplaceitem
GROUP BY etlsource
UNION ALL
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'source'
FROM datamart.source
GROUP BY etlsource
UNION ALL
SELECT MAX(insertdatetime) as InsertTime
	, etlsource
    , 'marketplaceitemrelationship'
FROM datamart.marketplaceitemrelationship
GROUP BY etlsource;



--3-20-2018
INSERT INTO etltables.category (categoryid, categoryname, marketentryid, categorytypeid)

--Working query for insert into category.
SELECT (SELECT COALESCE(MAX(categoryid),1) from etltables.category) as categoryid,
	plus_sale as categoryname,
    as marketentryid,
    categorytype.categorytypeid as categorytypeid,
    'sonymarketplace_scraperdataTOdatamart' as etlsource,
    current_timestamp as insertdatetime
FROM scraperdata.sonywebsite sonywebsite
LEFT JOIN etltables.marketentry marketentry
ON sonywebsite.console_type = marketentry.
AND sonywebsite.game_name = marketentry.
AND sonywebsite.badge_sale = marketentry.
LEFT JOIN etltables.categorytype categorytype
ON 'plus_sale' = categorytype.categoryname





SELECT *
FROM scraperdata.sonywebsite;



--Market Item
SELECT (select COALESCE(max(marketplaceitemid),1) from etltables.marketplaceitem), 
sonywebsite.game_name as title,console.consoleid,businessentity.businessentityid,'sonymarketplace_scraperdataTOdatamart' as etlsource, current_timestamp as insertdatetime FROM scraperdata.sonywebsite sonywebsite LEFT JOIN etltables.console console ON COALESCE(sonywebsite.console_type,'Unknown') = console.consolename LEFT JOIN etltables.businessentity businessentity 
ON 'Unknown' = businessentity.businessname;




---market entry
SELECT (select COALESCE(max(marketentryid),1) from etltables.marketentry) as marketentryid,
	COALESCE(etlsource.sourceid,(SELECT sourceid from etltables.source WHERE sourcename = 'Unknown'))  as sourcemarketidentifier,
    to_number(sonywebsite.badge_sale,'9,999.99')  as primaryprice,
    NULL  as sourceurl,
    sonywebsite.image  as gameimageurl,
    NULL  as reviewsurl,
    marketplaceitem.marketplaceitemid as marketplaceitemid,
    'sonymarketplace_scraperdataTOdatamart' as etlsource,
    current_timestamp as insertdatetime 
FROM scraperdata.sonywebsite sonywebsite 
LEFT JOIN etltables.source etlsource 
ON 'Sony Online Store' = etlsource.sourcename 
LEFT JOIN etltables.console console 
ON COALESCE(sonywebsite.console_type,'Unknown') = console.consolename 
LEFT JOIN etltables.businessentity businessentity 
ON 'Unknown' = businessentity.businessname 
LEFT JOIN etltables.marketplaceitem marketplaceitem	
ON COALESCE(sonywebsite.game_name,'Unknown') = marketplaceitem.title 
AND console.consoleid = marketplaceitem.consoleid 
AND businessentity.businessentityid = marketplaceitem.businessentityid





--DROP TABLE scraperdata.sonywebsite;

CREATE TABLE scraperdata.sonywebsite (
    image VARCHAR(256) NULL,
    badge_sale VARCHAR(20) NULL,
    game_name VARCHAR(400) NULL
);

--Add column that I didn't add in at first
ALTER TABLE scraperdata.sonywebsite ADD COLUMN insert_time timestamp;

SELECT *
FROM scraperdata.sonywebsite

grant insert on scraperdata.sonywebsite to dataingestionpush;
grant usage on schema scraperdata to dataingestionpush;

--Add unique row constraint
alter table scraperdata.sonywebsite ADD CONSTRAINT unique_row UNIQUE (image, badge_sale, game_name)

--Set Default value
alter table scraperdata.sonywebsite ALTER COLUMN image SET DEFAULT 'Unknown';
alter table scraperdata.sonywebsite ALTER COLUMN badge_sale SET DEFAULT 'Unknown';
alter table scraperdata.sonywebsite ALTER COLUMN game_name SET DEFAULT 'Unknown';
ALTER TABLE scraperdata.sonywebsite ADD COLUMN insert_time timestamp set default current_timestamp;