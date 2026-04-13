-- liquibase formatted sql
-- changeset firoz:create_tlqbase_table endDelimiter:@
-- comment: Liquibase pilot table for DB2 LUW testing

-- Ensure Db2 built-in functions are resolvable
SET CURRENT PATH = "SYSIBM","SYSFUN","SYSPROC","SYSIBMADM",${appSchema}
@

CREATE TABLE ${appSchema}.TLQBASE (
    TLQ_ID        CHAR(8)     NOT NULL
)
IN "USERSPACE1"
ORGANIZE BY ROW
@

CREATE UNIQUE INDEX ${appSchema}.X01TLQBASE
ON ${appSchema}.TLQBASE (TLQ_ID)
COMPRESS NO
INCLUDE NULL KEYS
DISALLOW REVERSE SCANS
@

ALTER TABLE ${appSchema}.TLQBASE
ADD CONSTRAINT PK_TLQBASE
PRIMARY KEY (TLQ_ID)
ENFORCED
@

-- Rollback section
-- rollback DROP TABLE ${appSchema}.TLQBASE
@