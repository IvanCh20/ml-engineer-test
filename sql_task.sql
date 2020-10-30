SELECT
    department
FROM
    employees
WHERE
    "position" = 'Software Developer'
GROUP BY
    department
HAVING COUNT(*) < 5
-- Ещё необходимо учесть отделы вообще без разработчиков
UNION
SELECT 
    department
FROM 
    employees
GROUP BY department, position
NOT HAVING position = 'Software Developer'
