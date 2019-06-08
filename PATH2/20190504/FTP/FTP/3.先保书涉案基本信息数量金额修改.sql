---1.更新先保书总金额
UPDATE T_C_DOC_GOODS_REG t SET t.AMT = (select sum(d.AMT) FROM T_C_DOC_GOODS_REG_DTL d WHERE d.GOODS_REG_UUID = t.GOODS_REG_UUID GROUP BY t.GOODS_REG_UUID)
WHERE (t.AMT is NULL or t.AMT = '' or t.AMT = '0');
---2.更新先保书总数量
UPDATE T_C_DOC_GOODS_REG t SET t.QTY = (select sum(d.QTY) FROM T_C_DOC_GOODS_REG_DTL d WHERE d.GOODS_REG_UUID = t.GOODS_REG_UUID GROUP BY t.GOODS_REG_UUID)
WHERE (t.QTY is NULL or t.QTY = '' or t.QTY = '0');
---3.更新案件基本信息案值和货值
UPDATE T_C_CASEINFO t SET (TOTAL_VALUE,GOODS_VALUE) = (select sum(amt),sum(amt) from T_C_CASE_GOODS_DTL d WHERE d.CASE_UUID = t.CASE_UUID)
WHERE t.TOTAL_VALUE = 0 OR t.GOODS_VALUE =0;