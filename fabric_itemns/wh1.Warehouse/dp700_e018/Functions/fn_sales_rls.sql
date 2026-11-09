--Limiting access on column level (RLS)
CREATE FUNCTION dp700_e018.fn_sales_rls(@region VARCHAR(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS result
WHERE @region IN (
    SELECT region FROM dp700_e018.user_region
    WHERE user_email = USER_NAME()
);

GO