start transaction;
CREATE TABLE g AS SELECT NULL AS j UNION ALL SELECT NULL AS j UNION ALL SELECT 'asdf' AS j WITH DATA;
rollback;
