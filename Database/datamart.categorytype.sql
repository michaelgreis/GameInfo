--DROP TABLE datamart.CategoryType;

CREATE TABLE datamart.CategoryType (
    CategoryTypeId SERIAL PRIMARY KEY,
    CategoryTypeName VARCHAR(100) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);


CREATE UNIQUE INDEX NaturalKey_category_type ON datamart.CategoryType (CategoryTypeName);

INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('sentiment','ManualEntry');
INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('specs','ManualEntry');
INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('genres','ManualEntry');
INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('early_access','ManualEntry');
INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('metascore','ManualEntry');
INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('tags','ManualEntry');
INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('discount_price','ManualEntry');
INSERT INTO datamart.categorytype (categorytypename,etlsource) VALUES ('id','ManualEntry');