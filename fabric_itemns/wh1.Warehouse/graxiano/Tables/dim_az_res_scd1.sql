CREATE TABLE [graxiano].[dim_az_res_scd1] (
    [resource_id]    BIGINT        IDENTITY NOT NULL,
    [NOMBRE]         VARCHAR (100) NOT NULL,
    [TIPO]           VARCHAR (100) NULL,
    [UBICACION]      VARCHAR (100) NULL,
    [GRUPO_RECURSOS] VARCHAR (100) NULL,
    [SUSCRIPCION]    VARCHAR (100) NULL
);


GO