SELECT * 
FROM [dp700].[assignments];

SELECT * 
FROM [dp700].[departments];

SELECT * 
FROM [dp700].[employees];

SELECT * 
FROM [dp700].[projects];

SELECT 
name
, salary 
, CONCAT('$', [salary]) AS salary_formatted
FROM [dp700].[employees]
WHERE salary > 50000;

SELECT
e.name
, d.[department_name]
FROM [dp700].[employees] e
JOIN [dp700].[departments] d
ON e.department_id = d.department_id

SELECT
a.department_name
, COUNT(*) AS numer_of_employees
    FROM (
        SELECT
        e.name
        , d.[department_name]
        FROM [dp700].[employees] e
    JOIN [dp700].[departments] d
    ON e.department_id = d.department_id

    ) AS a
GROUP BY a.department_name