--DROP TABLE datamart.CategoryType;

CREATE TABLE datamart.CategoryType (
    CategoryTypeId SERIAL PRIMARY KEY,
    CategoryTypeName VARCHAR(100) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);


CREATE UNIQUE INDEX NaturalKey_category_type ON datamart.CategoryType (CategoryTypeName);