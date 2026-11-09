    -- Examples
    GRANT SELECT ON SCHEMA::my_schema TO [my_user@example.com]; -- Grant SELECT permission on a specific schema

    GRANT SELECT ON my_schema.my_table TO [my_user@example.com]; -- Grant SELECT permission on a specific table

    DENY SELECT ON my_schema.my_table TO [my_user@example.com]; -- Deny SELECT permission on a specific table

    REVOKE SELECT ON my_schema.my_table TO [my_user@example.com];  -- Revoke SELECT permission on a specific table

    -- Column-level permissions
    GRANT SELECT (column1, column2) ON my_schema.my_table TO [my_user@example.com]; -- Grant SELECT permission on specific columns of a table
    DENY SELECT (column3) ON my_schema.my_table TO [my_user@example.com]; -- Deny SELECT permission on a specific column of a table
    REVOKE SELECT (column2) ON my_schema.my_table TO [my_user@example.com]; -- Revoke SELECT permission on a specific column of a table

    --ROW LWEVEL SECURITY (RLS)
    -- Create schema for managing RLS 
    CREATE SCHEMA sec;

    -- CREATE function that defines RLS logic for filtering rows
    CREATE FUNCTION sec.fn_region_sales_rls(@region VARCHAR(50))
    RETURNS TABLE -- This function returns a table that can be used to filter rows based on the region parameter.
    WITH SCHEMABINDING -- This option ensures that the function is bound to the schema and cannot be dropped or altered without first dropping the function.

    AS
    RETURN SELECT 1 AS result -- 
    WHERE @region IN (
        SELECT region FROM sales.user_region
        WHERE user_email = USER_NAME() 
    );

    -- Create a security policy that applies the RLS function to the sales.sales_data table
    CREATE SECURITY POLICY sec.region_sales_policy
    ADD FILTER PREDICATE sec.fn_region_sales_rls(region) ON sales.sales_region
        WITH (STATE = ON); -- This policy will filter rows in the sales.sales_data table based on the region of the current user.
-- WHENEVER a user queries the sales.sales_data table, the RLS function will be invoked to determine which rows are visible to that user based on their assigned region in the sales.user_region table.