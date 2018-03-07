--DROP TABLE datamart.Game

CREATE TABLE datamart.Game (
    GameId SERIAL PRIMARY KEY,
    Title VARCHAR(500) NOT NULL,
    AlternateName VARCHAR(500) NULL,
    ConsoleId INTEGER NOT NULL,
    BusinessEntityId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
    );

