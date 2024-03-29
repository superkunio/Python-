UPDATE T_C_CMD_TRANS_IN_GOODS_DIR SET CM_SYS_ROW_CREATETIME = LST_MODI_TIME WHERE T_C_CMD_TRANS_IN_GOODS_DIR.CM_SYS_ROW_CREATETIME is null;
--更新FIRST_IDENT_TIME
MERGE
INTO
    T_C_CMD_TRANS_IN_GOODS_DIR AS GD
USING
    (
        SELECT
            TRANS_IN_CASE_GOODS_DIR_UUID,
            FIRST_IDENT_TIME,
            FIRST_PROP_TYPE,
            FIRST_PROP_SUBTYPE,
            CASE
                WHEN CM_SYS_ROW_CREATETIME IS NULL
                THEN LST_MODI_TIME
				ELSE CM_SYS_ROW_CREATETIME
            END AS CM_SYS_ROW_CREATETIME ,
            PROP_TYPE,
            PROP_SUB_TYPE
        FROM
            DB2ADMIN.T_C_CMD_TRANS_IN_GOODS_DIR) AS T
ON
    GD.TRANS_IN_CASE_GOODS_DIR_UUID = T.TRANS_IN_CASE_GOODS_DIR_UUID
AND T.CM_SYS_ROW_CREATETIME IS NOT NULL
WHEN MATCHED
AND GD.FIRST_IDENT_TIME IS NULL THEN
UPDATE
SET
    GD.FIRST_IDENT_TIME=T.CM_SYS_ROW_CREATETIME ;
--更新FIRST_PROP_TYPE
MERGE
INTO
    T_C_CMD_TRANS_IN_GOODS_DIR AS GD
USING
    (
        SELECT
            TRANS_IN_CASE_GOODS_DIR_UUID,
            FIRST_IDENT_TIME,
            FIRST_PROP_TYPE,
            FIRST_PROP_SUBTYPE,
            CASE
                WHEN CM_SYS_ROW_CREATETIME IS NULL
                THEN LST_MODI_TIME
            END AS CM_SYS_ROW_CREATETIME ,
            PROP_TYPE,
            PROP_SUB_TYPE
        FROM
            DB2ADMIN.T_C_CMD_TRANS_IN_GOODS_DIR) AS T
ON
    GD.TRANS_IN_CASE_GOODS_DIR_UUID = T.TRANS_IN_CASE_GOODS_DIR_UUID
AND T.PROP_TYPE IS NOT NULL
AND trim(T.PROP_TYPE) !=''
WHEN MATCHED
AND GD.FIRST_PROP_TYPE IS NULL THEN
UPDATE
SET
    GD.FIRST_PROP_TYPE=T.PROP_TYPE ;
--更新FIRST_PROP_SUBTYPE
MERGE
INTO
    T_C_CMD_TRANS_IN_GOODS_DIR AS GD
USING
    (
        SELECT
            TRANS_IN_CASE_GOODS_DIR_UUID,
            FIRST_IDENT_TIME,
            FIRST_PROP_TYPE,
            FIRST_PROP_SUBTYPE,
            CASE
                WHEN CM_SYS_ROW_CREATETIME IS NULL
                THEN LST_MODI_TIME
            END AS CM_SYS_ROW_CREATETIME ,
            PROP_TYPE,
            PROP_SUB_TYPE
        FROM
            DB2ADMIN.T_C_CMD_TRANS_IN_GOODS_DIR) AS T
ON
    GD.TRANS_IN_CASE_GOODS_DIR_UUID = T.TRANS_IN_CASE_GOODS_DIR_UUID
AND T.PROP_SUB_TYPE IS NOT NULL
AND trim(T.PROP_SUB_TYPE) !=''
WHEN MATCHED
AND GD.FIRST_PROP_SUBTYPE IS NULL THEN
UPDATE
SET
    GD.FIRST_PROP_SUBTYPE= INT(T.PROP_SUB_TYPE)






