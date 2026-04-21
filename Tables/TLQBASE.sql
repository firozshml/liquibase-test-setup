--liquibase formatted sql
--changeset firoz:create_tlqbase_table

-------------------------------------------------------------------------------
-- Create table TLQBASE
-- Schema is controlled by Liquibase via defaultSchemaName
-------------------------------------------------------------------------------

CREATE TABLE TLQBASE (
    ID          INTEGER NOT NULL,
    NAME        VARCHAR(50),
    CREATED_TS  TIMESTAMP DEFAULT CURRENT TIMESTAMP
);

-------------------------------------------------------------------------------
-- Add primary key
-------------------------------------------------------------------------------

ALTER TABLE TLQBASE
    ADD CONSTRAINT PK_TLQBASE PRIMARY KEY (ID);

-------------------------------------------------------------------------------
-- Rollback definitions
-------------------------------------------------------------------------------
--rollback ALTER TABLE TLQBASE DROP CONSTRAINT PK_TLQBASE
--rollback DROP TABLE TLQBASE;
