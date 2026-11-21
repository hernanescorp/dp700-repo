SELECT connections.connection_id
    , connections.connect_time
    , sessions.session_id
    , sessions.login_name
    , sessions.login_time
    , sessions.status
FROM sys.dm_exec_connections AS connections
INNER JOIN sys.dm_exec_sessions AS sessions
ON connections.session_id = sessions.session_id
ORDER BY connections.connect_time DESC;
-- This query retrieves information about active connections and their associated sessions in SQL Server. 
-- It joins the sys.dm_exec_connections and sys.dm_exec_sessions dynamic management views (DMVs) to provide details such as connection ID, connection time, session ID, login name, login time, and session status. 

--The results are ordered by connection time in descending order, allowing you to see the most recent connections first.


-- Find long running queries
SELECT request.session_id
    , request.status
    , request.start_time
    , request.command
    , request.cpu_time
    , request.total_elapsed_time
FROM sys.dm_exec_requests AS request
WHERE request.status = 'running'
ORDER BY request.total_elapsed_time DESC;

SELECT login_name
FROM sys.dm_exec_sessions
WHERE session_id = 52

KILL 52;
-- query insights:

-- Identify queries run by you in the last 30 minuts
SELECT * 
FROM queryinsights.exec_requests_history
WHERE start_time >= DATEADD(MINUTE, -30, GETDATE())
    AND login_name = USER_NAME()

-- iDENTIFY TOP CPU CONSUMING QUERIES
SELECT TOP 10
    distributed_statement_id,
    query_hash,
    allocated_cpu_time_ms,
    label,
    command
FROM queryinsights.exec_requests_history
ORDER BY allocated_cpu_time_ms DESC;

-- Identify long running queries 
SELECT * 
FROM queryinsights.long_running_queries
ORDER BY median_total_elapsed_time_ms DESC;