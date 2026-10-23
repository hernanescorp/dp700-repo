CREATE TABLE [graxiano].[dim_az_res_scd2] (
    [resource_id]       BIGINT        IDENTITY NOT NULL,
    [NOMBRE]            VARCHAR (100) NOT NULL,
    [TIPO]              VARCHAR (100) NULL,
    [UBICACION]         VARCHAR (100) NULL,
    [GRUPO_RECURSOS]    VARCHAR (100) NULL,
    [SUSCRIPCION]       VARCHAR (100) NULL,
    [record_start_date] DATE          NULL,
    [record_end_date]   DATE          NULL,
    [is_current]        BIT           NULL
);


GO