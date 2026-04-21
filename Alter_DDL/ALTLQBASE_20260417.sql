-- liquibase formatted sql
-- changeset firoz:alter_tlqbase_v1 endDelimiter:@

SET CURRENT PATH = "SYSIBM","SYSFUN","SYSPROC","SYSIBMADM"
@

-- ========================
-- ALTER TYPE (3 alters)
-- ========================
ALTER TABLE TLQBASE ALTER COLUMN ID SET DATA TYPE INT
@
ALTER TABLE TLQBASE1 ALTER COLUMN CREATED_TS SET DATA TYPE TIMESTAMP
@
ALTER TABLE TLQBASE ALTER COLUMN NAME SET DATA TYPE VARCHAR(110)
@
-- ========================
-- REORG (MANDATORY for DB2)
-- ========================
CALL SYSPROC.ADMIN_CMD('REORG TABLE TLQBASE')
@