# Seguridad y despliegue de wh1

## Separacion del modelo y las identidades

El proyecto conserva Microsoft.Build.Sql 2.2.0 y el destino Fabric Warehouse
`SqlDwUnifiedDatabaseSchemaProvider`. Tablas, vistas, procedimientos, esquemas,
la funcion `dp700_e018.fn_sales_rls`, su politica activa y las mascaras DDM
permanecen en el modelo declarativo.

`PostDeploy.sql` contiene exactamente los siete bloques GRANT originales,
incluido `AS [dbo]` en todos ellos. Se ejecutan despues del esquema:

| Objeto | Ambito SELECT | Numero de bloques |
| --- | --- | --- |
| dp700_e018.finance | OBJECT (tabla) | 1 |
| dp700_e018.employees | department, employee_id, full_name (uno por columna) | 3 |
| dp700_e018.user_region | OBJECT (tabla) | 1 |
| dp700_e018.sales | OBJECT (tabla) | 1 |
| dp700_e019.masking_demo | OBJECT (tabla) | 1 |

Todos tienen como destinatario `test@graxiano.com`. No se concede SELECT sobre
employees.salary, UNMASK, permisos de escritura ni roles amplios. Repetir los
GRANT reaplica los permisos; no reconcilia ni elimina permisos ajenos.

`Security/test@graxiano.com.sql` conserva la definicion extraida y el SID como
referencia historica. Esta excluido de Build, incluido como None y no tiene
referencias desde PostDeploy. No debe ejecutarse: Warehouse no permite CREATE
USER explicito; GRANT/DENY materializan el usuario implicitamente.

## Soporte de publicacion: investigacion documental (2026-11-11)

La compilacion local incluye el script en el DACPAC; no ejecuta sus sentencias.
Los scripts PostDeploy no reciben validacion semantica del modelo DacFx.

1. **DACPAC con SqlPackage/DacFx o Publish de SQL Database Projects:** es la via
   propuesta para un futuro pipeline que consuma `local/wh1/wh1.sqlproj`.
   Microsoft documenta publicacion de DACPAC a Warehouse y ejecucion de
   PostDeploy despues del plan de esquema. No se ha probado la ejecucion remota
   ni seleccionado una version de SqlPackage/perfil en este trabajo. El pipeline
   debe publicar el DACPAC completo y no omitir el PostDeploy (por ejemplo, no
   habilitar `IgnorePostDeployScript`).
2. **Integracion Git nativa de Fabric:** el workspace de este repositorio sigue
   `fabric_itemns/`, no `local/wh1/`. Por tanto estos cambios locales NO participan
   automaticamente en esa sincronizacion. Microsoft documenta scripts de
   despliegue para Warehouse en preview: PostDeploy se ejecuta tras el esquema,
   pero Git requiere la experiencia de source control actualizada. En workspaces
   sin actualizar los metadatos no se sincronizan y los scripts no participan en
   ese flujo. No se ha inspeccionado ni cambiado el estado del workspace.
3. **Deployment pipelines de Fabric:** ejecutan los scripts designados del item
   de origen al promoverlo. No consumen este proyecto local automaticamente.
   El requisito de actualizacion de source control anterior es especifico de Git.

Para una futura adopcion nativa, usar una consulta compartida en `.sharedqueries`
y la designacion PostDeploy del item sincronizado, siguiendo la documentacion.
No se ha realizado esa migracion. Warehouse admite un solo archivo por fase y
no admite composicion con SQLCMD `:r` en su flujo nativo. Por ello se ajusto el
plan inicial: los siete GRANT estan directamente en un unico PostDeploy.sql,
sin un archivo Grants.sql auxiliar. El SDK local si permite componer scripts,
pero esa capacidad no demuestra compatibilidad con la integracion nativa.

Fuentes oficiales:

- [Scripts de despliegue de Warehouse (preview)](https://learn.microsoft.com/en-us/fabric/data-warehouse/deployment-scripts)
- [Desarrollo y publicacion de proyectos Warehouse](https://learn.microsoft.com/en-us/fabric/data-warehouse/develop-warehouse-project)
- [Flujos de desarrollo y despliegue](https://learn.microsoft.com/en-us/fabric/data-warehouse/development-deployment)
- [Empaquetado y ejecucion de Pre/PostDeploy](https://learn.microsoft.com/en-us/sql/tools/sql-database-projects/concepts/pre-post-deployment-scripts?view=sql-server-ver17)
- [Permisos granulares y limitacion CREATE USER](https://learn.microsoft.com/en-us/fabric/data-warehouse/sql-granular-permissions)
- [Opciones de SqlPackage Publish](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-publish)

## Riesgos y preparacion del futuro CI/CD

- Validar en un Warehouse de pruebas autorizado el principal Entra, su resolucion
  y los privilegios del publicador para ejecutar los GRANT con `AS [dbo]`.
  No se ha verificado remotamente este grantor ni se han cambiado privilegios.
- Dar al consumidor solo el acceso Fabric necesario para conectar (Read del
  elemento); revisar que roles de workspace, ReadData u otros permisos heredados
  no amplien el acceso previsto por OLS/CLS/DDM.
- RLS depende de USER_NAME() y de las filas de user_region. El DACPAC conserva la
  tabla y el filtro, pero no carga las asignaciones de usuarios a regiones.
  El SELECT existente sobre user_region se conserva sin endurecerlo ni ampliarlo.
- Un fallo de PostDeploy puede dejar el esquema ya actualizado y permisos
  aplicados parcialmente. El pipeline debe fallar, impedir promociones y permitir
  reintentar tras corregir la causa; no asumir rollback integral del despliegue.
- Generar y revisar el plan antes de publicar; mantener DropObjectsNotInSource
  y DropPermissionsNotInSource desactivados y proteger Users/Permissions externos
  en el perfil definitivo. Comprobar las opciones contra la version elegida de
  SqlPackage. No hay perfil ni pipeline de publicacion creado en este cambio.
- Fijar versiones de .NET, Microsoft.Build.Sql y SqlPackage; conservar el DACPAC
  como artefacto. Actualizar 2.2.0 en un cambio separado con validacion equivalente.
- Si aparecen dependencias de sys en el modelo, revisar la referencia oficial
  Microsoft.SqlServer.Dacpacs.FabricDw con DatabaseVariableLiteralValue=master.
  No se ha agregado una dependencia innecesaria para la compilacion actual.
- Separar identidades por entorno y evolucionar hacia roles funcionales con
  permisos declarativos y pertenencias externas. Mantener pruebas de acceso
  permitido y denegado, filas RLS y mascaras DDM con un usuario sin privilegios.
- Evitar versionar bin/obj en una futura politica de Git. Se conservan el
  BeforeBuild y la advertencia de SDK originales; no se suprimen validaciones.

## Validacion local

Ejecutar desde la raiz: `dotnet build .\local\wh1\wh1.sqlproj`.
Resultado esperado: `local/wh1/bin/Debug/wh1.dacpac`.
Inspeccionar el ZIP del DACPAC: model.xml debe contener RLS y DDM; postdeploy.sql
debe contener los siete GRANT y ningun CREATE USER ejecutable.
Comparar los bloques contra Git y comprobar `git diff -- fabric_itemns/`.
Compilar e inspeccionar el paquete no acredita ejecucion ni seguridad efectiva
en el servicio. No se han ejecutado publicaciones, despliegues, commits ni pushes.

Resultado comprobado el 2026-11-11: compilacion correcta, codigo de salida 0,
0 errores y 1 advertencia de actualizacion disponible a Microsoft.Build.Sql 2.3.0.
Salida completa en `Build.log` (evidencia local, no entrada del proyecto).
Inspeccion del DACPAC: 12 tablas, funcion y politica RLS, 10 MaskingFunction
coincidentes con el DDL, y 7 bloques GRANT identicos caracter por caracter a los
originales, incluidos los siete `AS [dbo]`. Se verificaron los elementos evaluados
por MSBuild: el usuario historico no es Build, figura como None, y solo existe un
PostDeploy. Ningun CREATE USER ejecutable ni :r aparece en postdeploy.sql.
Las definiciones originales de tablas y los otros archivos SQL declarativos
se compararon con una instantanea anterior a la edicion y permanecen intactos.
`git diff --exit-code -- fabric_itemns/` termino con codigo 0 sin diferencias.
