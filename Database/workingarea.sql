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