--DROP TABLE datamart.RelationshipType;

CREATE TABLE datamart.RelationshipType (
    RelationshipTypeId SERIAL PRIMARY KEY,
    RelationshipName VARCHAR(100) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);

CREATE UNIQUE INDEX NaturalKey_RelationshipType ON datamart.RelationshipType (RelationshipName);

INSERT INTO datamart.RelationshipType (RelationshipName,EtlSource) VALUES ('Developer','ManualInsert');
INSERT INTO datamart.RelationshipType (RelationshipName,EtlSource) VALUES ('Publisher','ManualInsert');
INSERT INTO datamart.RelationshipType (RelationshipName,EtlSource) VALUES ('Unknown','ManualInsert');