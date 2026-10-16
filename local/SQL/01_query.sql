CREATE SCHEMA dp700;
GO

CREATE TABLE dp700.employees (
    employee_id INT NOT NULL,
    name VARCHAR(50),
    department_id INT,
    hire_date DATE,
    salary DECIMAL(10,2)
);
GO