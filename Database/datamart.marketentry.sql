--DROP TABLE datamart.MarketEntry

CREATE TABLE datamart.MarketEntry (
    MarketEntryId SERIAL NOT NULL,
    ReleaseDate DATE NULL ,
    SourceMarketIdentifier VARCHAR(30) NULL,
    PrimaryPrice DECIMAL(6,2) NULL,
    SourceUrl VARCHAR(300) NULL,
    GameImageUrl VARCHAR(300) NULL,
    ReviewsUrl VARCHAR(300) NULL,
    GameId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);