DROP TABLE scraperdata.sonywebsite;
DELETE FROM scraperdata.sonywebsite;

SELECT COUNT(*) FROM scraperdata.steammarketplace;

CREATE TABLE scraperdata.steammarketplace(
    id VARCHAR(50) NULL,
    title VARCHAR(500) NULL,
    release_date VARCHAR(100) NULL,
    app_name VARCHAR(500) NULL,
    early_access VARCHAR(200) NULL,
    full_data json NULL,
    insert_time TIMESTAMP
);

/*alter table scraperdata.steammarketplace ADD CONSTRAINT unique_row_steam 
UNIQUE (id, title, release_date, app_name, early_access);
alter table scraperdata.steammarketplace  DROP CONSTRAINT unique_row_steam;*/
ALTER TABLE scraperdata.steammarketplace ALTER COLUMN insert_time set default current_timestamp;

grant usage on schema scraperdata to dataingestionpush;
grant insert on scraperdata.steammarketplace to dataingestionpush;
