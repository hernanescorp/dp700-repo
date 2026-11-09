CREATE TABLE [dp700_e018].[employees] (
    [employee_id] INT             NULL,
    [full_name]   VARCHAR (100)   NULL,
    [department]  VARCHAR (50)    NULL,
    [salary]      DECIMAL (18, 2) NULL
);
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

