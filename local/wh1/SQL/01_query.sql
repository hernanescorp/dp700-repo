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

INSERT INTO dp700.employees 
(employee_id, [name], [department_id], [hire_date], [salary])
VALUES
(1, 'Hernan EScriba', 101, '2015-01-01', 75000.00),
    (2, 'Jane Smith', 102, '2018-09-15', 85000.00),
    (3, 'Alex Johnson', 103, '2020-01-10', 68000.00),
    (4, 'Sara Lee', 101, '2017-03-12', 72000.00),
    (5, 'Michael Brown', 102, '2019-11-20', 95000.00),
    (6, 'Emma Davis', 103, '2021-07-18', 62000.00);
GO

CREATE TABLE dp700.departments (
    department_id INT NOT NULL,
    department_name VARCHAR(50),
    manager VARCHAR(50),
    location VARCHAR(50)
);
GO

INSERT INTO dp700.departments
([department_id], [department_name], [manager], [location])
VALUES 
    (101, 'Sales', 'Alice Green', 'New York'),
    (102, 'Management', 'Robert White', 'San Francisco'),
    (103, 'IT', 'Sophia Black', 'Seattle'),
    (104, 'Marketing', 'David Blue', 'Chicago');
GO

-- Create the projects table
CREATE TABLE dp700.projects (
    project_id INT,
    project_name VARCHAR(50),
    department_id INT,
    budget DECIMAL(12, 2),
    start_date DATE
);
GO

-- Insert data into projects table
INSERT INTO dp700.projects (project_id, project_name, department_id, budget, start_date)
VALUES
    (201, 'Product Launch', 101, 150000.00, '2023-01-01'),
    (202, 'System Upgrade', 103, 200000.00, '2022-05-15'),
    (203, 'New Branch Setup', 102, 250000.00, '2023-03-01'),
    (204, 'Digital Marketing Campaign', 104, 120000.00, '2022-08-01');
GO

-- Create the assignments table to track employee-project relationships
CREATE TABLE dp700.assignments (
    assignment_id INT,
    employee_id INT,
    project_id INT,
    assigned_date DATE,
    role VARCHAR(50)
);
GO

-- Insert data into assignments table
INSERT INTO dp700.assignments (assignment_id, employee_id, project_id, assigned_date, role)
VALUES
    (1, 1, 201, '2023-02-01', 'Team Lead'),
    (2, 3, 202, '2022-06-01', 'Developer'),
    (3, 2, 203, '2023-04-01', 'Project Manager'),
    (4, 5, 203, '2023-04-15', 'Analyst'),
    (5, 4, 201, '2023-02-10', 'Sales Rep'),
    (6, 6, 202, '2022-07-01', 'Support Engineer');
GO
