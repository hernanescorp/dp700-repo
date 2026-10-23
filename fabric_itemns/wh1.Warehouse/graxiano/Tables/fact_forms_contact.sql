CREATE TABLE [graxiano].[fact_forms_contact] (
    [id_contact]    BIGINT        IDENTITY NOT NULL,
    [RowKey]        VARCHAR (100) NOT NULL,
    [Timestamp]     DATETIME2 (6) NULL,
    [tipoSolicitud] VARCHAR (50)  NULL,
    [nombre]        VARCHAR (200) NULL,
    [email]         VARCHAR (200) NULL,
    [rol]           VARCHAR (100) NULL
);


GO