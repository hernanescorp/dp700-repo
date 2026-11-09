-- Apply masking when creating the table
CREATE TABLE dbo.table1 (
    name VARCHAR(100) MASKED WITH (FUNCTION = 'default()'),
    email VARCHAR(100) MASKED WITH (FUNCTION = 'email()'),
    number INT MASKED WITH (FUNCTION = 'random(1000, 9999)'),
    id VARCHAR(20) MASKED WITH (FUNCTION = 'partial(2,"-MASKED-",2)')
)

-- When the table already exists, you can apply masking using ALTER TABLE statement
ALTER TABLE dbo.table1
ALTER COLUMN name ADD MASKED WITH (FUNCTION = 'default()');

-- Use DROP MASKED to remove masking from a column
ALTER TABLE dbo.table1
ALTER COLUMN name DROP MASKED;

-- GRANT UNMASK permission to a user to allow them to see the unmasked data
GRANT UNMASK ON dbo.table1 TO [username];
REVOKE UNMASK ON dbo.table1 TO [username];
-- Dynamic Data Naskiing is not a security feature, it is a data protection feature. It is not meant to be used as a security measure to protect sensitive data from unauthorized access. It is meant to be used as a data protection feature to protect sensitive data from being exposed to users who do not have the necessary permissions to view it.
    -- For enhanced security, it is recommended to use Dynamic Data Masking in conjunction with other security features such as encryption, access control, and auditing.
    