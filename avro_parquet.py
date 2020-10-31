import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").enableHiveSupport().getOrCreate()

IN="/public/retail_db/orders/part-00000"
OUT="/user/shree624/problem1/"
INF="csv"
OUTF="parquet"

df= spark.read.format(INF).load(IN)
df1 = df.createOrReplaceTempView('o')
SQL="Select _c0,_c3 from o order by _c0"
df.show()
df1=spark.sql(SQL)
df1.show()
df1.printSchema()
df1.coalesce(1).write.mode("overwrite").option("compression","gzip").format(OUTF).save(OUT)


