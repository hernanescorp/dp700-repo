CREATE SECURITY POLICY [dp700_e018].[sales_rls_policy]
    ADD FILTER PREDICATE [dp700_e018].[fn_sales_rls]([region]) ON [dp700_e018].[sales]
    WITH (STATE = ON);
GO

