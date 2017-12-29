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