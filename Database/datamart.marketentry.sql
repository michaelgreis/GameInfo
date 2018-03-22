--DROP TABLE datamart.MarketEntry

CREATE TABLE datamart.MarketEntry (
    MarketEntryId SERIAL NOT NULL,
    ReleaseDate DATE NULL ,
    SourceMarketIdentifier VARCHAR(30) NULL,
    PrimaryPrice DECIMAL(6,2) NULL,
    SourceUrl VARCHAR(300) NULL,
    GameImageUrl VARCHAR(300) NULL,
    ReviewsUrl VARCHAR(300) NULL,
    MarketplaceItemId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);

CREATE UNIQUE INDEX MarketEntry ON datamart.MarketEntry (ReleaseDate, SourceMarketIdentifier, PrimaryPrice,MarketplaceItemId);

