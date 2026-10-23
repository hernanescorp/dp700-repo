CREATE   VIEW graxiano.vw_fact_forms_contact AS
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

GO