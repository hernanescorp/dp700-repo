CREATE TABLE [dp700_e018].[finance] (
    [finance_id] INT             NULL,
    [department] VARCHAR (50)    NULL,
    [budget]     DECIMAL (18, 2) NULL
);
GO

GRANT SELECT
    ON OBJECT::[dp700_e018].[finance] TO [test@graxiano.com]
    AS [dbo];
GO

