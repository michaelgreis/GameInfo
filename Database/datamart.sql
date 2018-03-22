--creation of the datamart database

-- Database: datamart

-- DROP DATABASE datamart;

CREATE DATABASE datamart
    WITH 
    OWNER = devadmin
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE datamart
    IS 'This is where data goes for ingestion by the different applications and uses.';


--create statements for the user datamartetl
CREATE USER datamartetl;
GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA datamart TO datamartetl;
GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA landingzone TO datamartetl;
GRANT USAGE ON SCHEMA datamart TO datamartetl;
GRANT USAGE ON SCHEMA scraperdata TO datamartetl;

--grants privleges to the table containing the fwd objects which allow lookups to the datamart schema for FK relationships.
CREATE USER MAPPING FOR datamartetl
  SERVER datamart_database_link
  OPTIONS (user '', password '');