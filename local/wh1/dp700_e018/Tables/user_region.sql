CREATE TABLE [dp700_e018].[user_region] (
    [user_email] VARCHAR (100) NULL,
    [region]     VARCHAR (50)  NULL
);
GO

GRANT SELECT
    ON OBJECT::[dp700_e018].[user_region] TO [test@graxiano.com]
    AS [dbo];
GO

