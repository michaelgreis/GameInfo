--creation of the datamart database

-- Database: datamart

-- DROP DATABASE datamart;

/*CREATE DATABASE datamart
    WITH 
    OWNER = devadmin
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE datamart
    IS 'This is where data goes for ingestion by the different applications and uses.';*/


--create statements for the user datamartetl
CREATE USER datamartetl;
GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA datamart TO datamartetl;
GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA scraperdata TO datamartetl;
--GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA etltables TO datamartetl; --Schema no longer exists. Since foreign data wrapper removed
GRANT USAGE ON SCHEMA datamart TO datamartetl;
GRANT USAGE ON SCHEMA scraperdata TO datamartetl;
--GRANT USAGE ON SCHEMA etltables TO datamartetl; --Schema no longer exists. Since foreign data wrapper removed
GRANT CONNECT ON DATABASE landingzone TO datamartetl;
GRANT CONNECT ON DATABASE datamart TO datamartetl;

--grants privleges to the table containing the fwd objects which allow lookups to the datamart schema for FK relationships.
CREATE USER MAPPING FOR datamartetl
  SERVER datamart_database_link
  OPTIONS (user '', password '');

--refreshing the foreign data tables. Should be run on landingzone database.
--  Update: no longer needed. Can't implement unique indexes on foreign tables which is a deal breaker.
/*
DROP USER MAPPING FOR datamartetl SERVER datamart_database_link;
  
 DROP FOREIGN TABLE etltables.businessentity;
 DROP FOREIGN TABLE etltables.category ;
 DROP FOREIGN TABLE etltables.categorytype ;
 DROP FOREIGN TABLE etltables.console ;
 DROP FOREIGN TABLE etltables.marketentry ;
 DROP FOREIGN TABLE etltables.marketplaceitem ;
 DROP FOREIGN TABLE etltables.source ;


GRANT USAGE ON FOREIGN SERVER datamart_database_link TO datamartetl;

 IMPORT FOREIGN SCHEMA datamart
  FROM SERVER datamart_database_link
  INTO etltables;

GRANT USAGE ON SCHEMA etltables TO datamartetl;
GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA etltables TO datamartetl;*/
