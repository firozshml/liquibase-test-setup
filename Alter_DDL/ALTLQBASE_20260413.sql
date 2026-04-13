-- liquibase formatted sql
-- changeset firoz:alter_tlqbase_v1 endDelimiter:@
-- comment: Liquibase pilot - alter TLQBASE (add columns, modify TLQ_ID length)

-- Ensure Db2 built-in functions and schema resolution
SET CURRENT PATH = "SYSIBM","SYSFUN","SYSPROC","SYSIBMADM",${appSchema}
@

-- 1. Modify existing column length
ALTER TABLE ${appSchema}.TLQBASE ALTER COLUMN TLQ_ID SET DATA TYPE CHAR(12)
@
CALL SYSPROC.ADMIN_CMD('REORG TABLE ${appSchema}.TLQBASE')
@

-- 2. Add new column
ALTER TABLE ${appSchema}.TLQBASE ADD COLUMN TLQ_STATUS CHAR(1) NOT NULL WITH DEFAULT 'A'

@
CALL SYSPROC.ADMIN_CMD('REORG TABLE ${appSchema}.TLQBASE')
@

-- ======================
-- Rollback section
-- ======================

-- rollback CALL SYSPROC.ADMIN_CMD('REORG TABLE ${appSchema}.TLQBASE')
-- rollback ALTER TABLE ${appSchema}.TLQBASE DROP COLUMN TLQ_STATUS
-- rollback ALTER TABLE ${appSchema}.TLQBASE ALTER COLUMN TLQ_ID SET DATA TYPE CHAR(8)
-- rollback CALL SYSPROC.ADMIN_CMD('REORG TABLE ${appSchema}.TLQBASE')
@
