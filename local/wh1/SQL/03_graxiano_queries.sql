CREATE SCHEMA graxiano;
GO 

CREATE TABLE graxiano.fact_forms_contact (
    id_contact BIGINT IDENTITY,
    RowKey VARCHAR(100) NOT NULL,
    [Timestamp] DATETIME2(6),
    tipoSolicitud VARCHAR(50),
    nombre VARCHAR(200),
    email VARCHAR(200),
    rol VARCHAR(100)
);
GO

INSERT INTO graxiano.fact_forms_contact (RowKey, [Timestamp], tipoSolicitud, nombre, email, rol)
VALUES

('1', '2024-01-01 10:00:00', 'test', 'Juan test', 'juan.perez@example.com', 'test');

CREATE OR ALTER VIEW graxiano.vw_fact_forms_contact AS
SELECT 
   [id_contact]
   , [Timestamp]
   , [tipoSolicitud]
   ,DATEDIFF(DAY, [Timestamp], GETDATE()) AS dias_transcurridos
   , CASE 
        WHEN DATEDIFF(DAY, [Timestamp], GETDATE()) >= 30 THEN 'mas de 30 dias'
        WHEN DATEDIFF(DAY, [Timestamp], GETDATE()) <30 THEN 'menos de 30 dias'
        ELSE 'sin datos'
    END AS dias_transcurridos_categoria
FROM graxiano.fact_forms_contact; 

CREATE PROCEDURE graxiano.sp_get_forms_contact
    @tipoSolicitud VARCHAR(50) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT *
    FROM graxiano.fact_forms_contact
    WHERE (@tipoSolicitud IS NULL OR tipoSolicitud = @tipoSolicitud);
END;

EXEC graxiano.sp_get_forms_contact @tipoSolicitud = 'test';

-----------------------------------------------------------
COPY INTO graxiano.fact_forms_contact (
    RowKey,
    [Timestamp],
    tipoSolicitud,
    nombre,
    email,
    rol
)
FROM 'https://graxianodatalake.blob.core.windows.net/raw/graxiano/forms/2026/10/22/forms.parquet'
WITH (
    FILE_TYPE = 'PARQUET',
    IDENTITY_INSERT = 'OFF'
);
 ------------------------------------

SELECT *
FROM graxiano.fact_forms_contact
OPTION (FOR TIMESTAMP AS OF '2026-10-23 12:15:00');

SELECT *
FROM graxiano.fact_forms_contact
OPTION (FOR TIMESTAMP AS OF '2026-10-23 12:29:00');



