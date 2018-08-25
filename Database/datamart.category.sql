--8.22.2018: altered table to use marketplaceitemid, as opposed to market entry...waaaay too much duplicate data.

--DROP TABLE datamart.Category;

CREATE TABLE datamart.Category (
    CategoryId SERIAL PRIMARY KEY,
    CategoryName VARCHAR(250) NOT NULL,
    MarketPlaceItemId INTEGER NOT NULL,
    CategoryTypeId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);

CREATE UNIQUE INDEX NaturalKey_category ON datamart.Category (categoryName, MarketPlaceItemId, CategoryTypeId);