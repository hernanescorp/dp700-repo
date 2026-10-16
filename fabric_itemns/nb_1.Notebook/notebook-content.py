# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "dba0f676-0c05-4c16-8229-401e855faa24",
# META       "default_lakehouse_name": "lk_1",
# META       "default_lakehouse_workspace_id": "b609f989-9bba-4dfe-ac3f-e28288cbe234",
# META       "known_lakehouses": [
# META         {
# META           "id": "dba0f676-0c05-4c16-8229-401e855faa24"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # NOTEBOOK GLOBAL

# MARKDOWN ********************

# ## Creation of a delta table with Spark

# CELL ********************

df = spark.createDataFrame(
    [
        ("Hernan", 41, "Ingeniero"),
        ("Maria", 20, "Analista"),
        ("Juan", 31, "Cientifico")
    ],
    "name STRING, age INT, role STRING"
)

df.write.format("delta").saveAsTable("person")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Sintax Differences Example 1

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT name, age
# MAGIC FROM person

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **KQL QUERY**
# 
# ```
# person
# | project name, age
# ```

# CELL ********************

display(spark.table("dbo.person").select("name", "age"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Sintax difference Example 2

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT count(*) AS count
# MAGIC FROM person

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# **KQL**
# 
# ```
# person 
# | count
# ```


# CELL ********************

display(spark.table("person") \
.agg({"*":"count"}) \
.withColumnRenamed("count(1)", "count"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Sintax Difference Example 3

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT name, age 
# MAGIC FROM person
# MAGIC WHERE name = 'Hernan'

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ```
# person 
# | where name == "Hernan"
# | project name, age
# ```

# CELL ********************

from pyspark.sql.functions import col
display (
    spark.table("dbo.person") \
    .filter(col("name") == "Hernan") \
    .select("name", "Age")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Syntax Difference Example 4

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT
# MAGIC     name,
# MAGIC     age
# MAGIC FROM person
# MAGIC WHERE age >= 30
# MAGIC ORDER BY age ASC

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ```
# person
# | where age >= 30
# | project  name, age
# | order by age asc
# ```

# CELL ********************

display(
    spark.table("person") \
    .filter(col("age")>= 30) \
    .select("name", "age") \
    .orderBy(col("age"), asceding = True)
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Syntax Difference Example 5

# MARKDOWN ********************

# ## Create a new Table

# CELL ********************

df = spark.createDataFrame(
    [
        ("Hernan","IT"),
        ("Maria","finance"),
        ("Juan", "sales")
    ],
    "name STRING, info STRING"
)

df.write.format("delta").saveAsTable("person_info")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT p.name, p.age, pi.info
# MAGIC FROM person AS p
# MAGIC JOIN person_info AS pi
# MAGIC ON p.name = pi.name

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ```
# person
# |join person_info on name
# |project name, age, info
# ```

# CELL ********************

display(
    spark.table("person")
    .join(spark.table("person_info"), on="name", how="inner")
    .select("name", "age", "info")
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
