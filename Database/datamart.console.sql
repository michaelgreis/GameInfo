--DROP TABLE datamart.Console

CREATE TABLE datamart.Console (
    ConsoleId SERIAL NOT NULL,
    ConsoleName VARCHAR(100) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);

CREATE UNIQUE INDEX Console ON datamart.Console (ConsoleName);

INSERT INTO datamart.Console (ConsoleName,EtlSource) VALUES ('PS4','ManualEntry');
INSERT INTO datamart.Console (ConsoleName,EtlSource) VALUES ('PC','ManualEntry');
INSERT INTO datamart.Console (ConsoleName,EtlSource) VALUES ('Unknown','ManualEntry')