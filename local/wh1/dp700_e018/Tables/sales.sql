CREATE TABLE [dp700_e018].[sales] (
    [sale_id]      INT             NULL,
    [region]       VARCHAR (50)    NULL,
    [sales_person] VARCHAR (100)   NULL,
    [amount]       DECIMAL (18, 2) NULL
);
GO


GRANT SELECT
    ON OBJECT::[dp700_e018].[sales] TO [test@graxiano.com]
    AS [dbo];
GO

