--DROP TABLE scraperdata.sonywebsite;

CREATE TABLE scraperdata.sonywebsite (
    image VARCHAR(256) NULL,
    badge_sale VARCHAR(20) NULL,
    game_name VARCHAR(400) NULL
);

SELECT *
FROM scraperdata.sonywebsite

grant insert on scraperdata.sonywebsite to dataingestionpush;
grant usage on schema scraperdata to dataingestionpush;