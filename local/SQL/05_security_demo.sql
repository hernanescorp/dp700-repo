-- Create schema
CREATE SCHEMA dp700_e018;
GO

-- Create employees table
CREATE TABLE dp700_e018.employees (
    employee_id INT,
    full_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(18, 2)
);

INSERT INTO dp700_e018.employees
VALUES 
(1, 'Alice Johnson', 'HR', 70000),
(2, 'Bob Smith', 'IT', 85000),
(3, 'Carol Lee', 'Sales', 65000);

-- Create sales table
CREATE TABLE dp700_e018.sales (
    sale_id INT,
    region VARCHAR(50),
    sales_person VARCHAR(100),
    amount DECIMAL(18, 2)
);

INSERT INTO dp700_e018.sales
VALUES 
(101, 'north', 'Alice Johnson', 10000),
(102, 'south', 'Bob Smith', 12000),
(103, 'north', 'Carol Lee', 8000),
(104, 'west', 'David Lee', 15000);

-- Create finance table
CREATE TABLE dp700_e018.finance (
    finance_id INT,
    department VARCHAR(50),
    budget DECIMAL(18, 2)
);

INSERT INTO dp700_e018.finance
VALUES 
(1, 'HR', 300000),
(2, 'IT', 500000),
(3, 'Sales', 250000);

-- Create user-region mapping (for RLS)
CREATE TABLE dp700_e018.user_region (
    user_email VARCHAR(100),
    region VARCHAR(50)
);

INSERT INTO dp700_e018.user_region
VALUES
('test@graxiano.com', 'north');