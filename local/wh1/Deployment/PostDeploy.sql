-- Environment-specific permissions; preserve object/column scope and grantor.
-- Fabric Warehouse creates Entra users implicitly through GRANT.
-- Repeated GRANT statements reapply permissions without adding broader access.

GRANT SELECT
    ON OBJECT::[dp700_e018].[finance] TO [test@graxiano.com]
    AS [dbo];
GO

GRANT SELECT
    ON [dp700_e018].[employees] ([department]) TO [test@graxiano.com]
    AS [dbo];
GO

GRANT SELECT
    ON [dp700_e018].[employees] ([employee_id]) TO [test@graxiano.com]
    AS [dbo];
GO

GRANT SELECT
    ON [dp700_e018].[employees] ([full_name]) TO [test@graxiano.com]
    AS [dbo];
GO

GRANT SELECT
    ON OBJECT::[dp700_e018].[user_region] TO [test@graxiano.com]
    AS [dbo];
GO

GRANT SELECT
    ON OBJECT::[dp700_e018].[sales] TO [test@graxiano.com]
    AS [dbo];
GO

GRANT SELECT
    ON OBJECT::[dp700_e019].[masking_demo] TO [test@graxiano.com]
    AS [dbo];
GO
