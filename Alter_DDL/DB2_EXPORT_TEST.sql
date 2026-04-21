-- liquibase formatted sql
-- changeset firoz:test_db2_export_v1 endDelimiter:@

-- ========================
-- SET CURRENT PATH
-- ========================
SET CURRENT PATH = "SYSIBM","SYSFUN","SYSPROC","SYSIBMADM"
@

-- ========================
-- DB2 EXPORT TEST
-- PURPOSE:
--  - Demonstrate that DB2 EXPORT
--    does NOT work via Liquibase
--  - EXPORT is a DB2 CLP utility
--    and not executable SQL
-- ========================
EXPORT TO /tmp/liquibase_export_test.del OF DEL
SELECT 1 FROM SYSIBM.SYSDUMMY1
@

-- ========================
-- EXPECTED BEHAVIOR
-- ========================
-- This changeSet will FAIL with:
-- SQLCODE=-104, SQLSTATE=42601
-- because EXPORT is not valid SQL
-- when executed via JDBC/Liquibase

