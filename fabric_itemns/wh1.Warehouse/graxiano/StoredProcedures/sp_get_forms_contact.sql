CREATE PROCEDURE graxiano.sp_get_forms_contact
    @tipoSolicitud VARCHAR(50) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT *
    FROM graxiano.fact_forms_contact
    WHERE (@tipoSolicitud IS NULL OR tipoSolicitud = @tipoSolicitud);
END;

GO