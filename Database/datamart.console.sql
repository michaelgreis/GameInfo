--DROP TABLE datamart.Console

CREATE TABLE datamart.Console (
    ConsoleId SERIAL PRIMARY KEY,
    ConsoleName VARCHAR(100) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);