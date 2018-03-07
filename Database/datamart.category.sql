--DROP TABLE datamart.Category

CREATE TABLE datamart.Category (
    CategoryId SERIAL PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    MarketEntryId INTEGER NOT NULL,
    CategoryTypeId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);