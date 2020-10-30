SELECT
    department
FROM
    employees
WHERE
    "position" = 'Software Developer'
GROUP BY
    department
HAVING COUNT(*) < 5