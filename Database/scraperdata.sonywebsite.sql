DROP TABLE scraperdata.sonywebsite;
DELETE FROM scraperdata.sonywebsite;


SELECT COUNT(*) FROM scraperdata.sonywebsite;


CREATE TABLE scraperdata.sonywebsite (
    image VARCHAR(256) NULL,
    badge_sale VARCHAR(20) NULL,
    game_name VARCHAR(400) NULL,
	plus_sale VARCHAR(100) NULL,
	console_type VARCHAR(50) NULL,
	item_type VARCHAR(100),
	insert_time TIMESTAMP
);

alter table scraperdata.sonywebsite ADD CONSTRAINT unique_row UNIQUE (badge_sale, game_name,plus_sale,item_type,console_type)
alter table scraperdata.sonywebsite ALTER COLUMN image SET DEFAULT 'Not Available';
alter table scraperdata.sonywebsite ALTER COLUMN badge_sale SET DEFAULT 'Not Available';
alter table scraperdata.sonywebsite ALTER COLUMN game_name SET DEFAULT 'Not Available';
alter table scraperdata.sonywebsite ALTER COLUMN plus_sale SET DEFAULT 'Not Available';
alter table scraperdata.sonywebsite ALTER COLUMN console_type SET DEFAULT 'Not Available';
alter table scraperdata.sonywebsite ALTER COLUMN item_type SET DEFAULT 'Not Available';
ALTER TABLE scraperdata.sonywebsite ALTER COLUMN insert_time set default current_timestamp;

grant insert on scraperdata.sonywebsite to dataingestionpush;
grant usage on schema scraperdata to dataingestionpush;


-- First test. Are the new columns flowing through correctly?
SELECT console_type, item_type, COUNT(*)
FROM scraperdata.sonywebsite
GROUP BY console_type, item_type;

