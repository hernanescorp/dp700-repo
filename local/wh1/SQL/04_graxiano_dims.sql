-- SCD1 - Dimensión de recursos de Azure

CREATE TABLE graxiano.dim_az_res_scd1 (
    resource_id BIGINT IDENTITY NOT NULL,
    NOMBRE VARCHAR(100) NOT NULL,
    TIPO VARCHAR(100),
    UBICACION VARCHAR(100),
    GRUPO_RECURSOS  VARCHAR(100),
    SUSCRIPCION VARCHAR(100)
);
GO

COPY INTO graxiano.dim_az_res_scd1 (
    NOMBRE,
    TIPO,
    UBICACION,
    GRUPO_RECURSOS,
    SUSCRIPCION
)
FROM 'https://graxianodatalake.blob.core.windows.net/raw/graxiano/manual_exports/Azure.csv'
WITH (
    FILE_TYPE = 'CSV',
    FIRSTROW = 2,
    IDENTITY_INSERT = 'OFF'
);

UPDATE [graxiano].[dim_az_res_scd1]
SET  UBICACION = 'UBICACION TEST'
WHERE resource_id = 8394709705418604545

-- SCD2 - Dimensión de recursos de Azure
CREATE TABLE graxiano.dim_az_res_scd2 (
    resource_id BIGINT IDENTITY NOT NULL,
    NOMBRE VARCHAR(100) NOT NULL,
    TIPO VARCHAR(100),
    UBICACION VARCHAR(100),
    GRUPO_RECURSOS  VARCHAR(100),
    SUSCRIPCION VARCHAR(100),
    record_start_date DATE NOT NULL,
    record_end_date DATE NULL,
    is_current BIT NOT NULL
);
GO

ALTER TABLE graxiano.dim_az_res_scd2
ALTER COLUMN record_start_date DATE NULL;

ALTER TABLE graxiano.dim_az_res_scd2
ALTER COLUMN is_current BIT NULL;

COPY INTO graxiano.dim_az_res_scd2 (
    NOMBRE,
    TIPO,
    UBICACION,
    GRUPO_RECURSOS,
    SUSCRIPCION
)
FROM 'https://graxianodatalake.blob.core.windows.net/raw/graxiano/manual_exports/Azure.csv'
WITH (
    FILE_TYPE = 'CSV',
    FIRSTROW = 2,
    IDENTITY_INSERT = 'OFF'
);

UPDATE [graxiano].[dim_az_res_scd2]
SET [record_start_date] = GETDATE(), [is_current] = 1

UPDATE [graxiano].[dim_az_res_scd2]
SET record_end_date = '2999-12-31'