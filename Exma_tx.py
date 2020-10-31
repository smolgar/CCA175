import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").enableHiveSupport().getOrCreate()

IN="/public/retail_db/orders/part-00000"
IN1="/public/retail_db/customers/part-00000"
OUT="/user/shree624/problem2/"
INF="csv"
OUTF="csv"

df= spark.read.format(INF).load(IN)
df1= spark.read.format(INF).load(IN1)
df.createOrReplaceTempView('o')
df1.createOrReplaceTempView('c')
SQL="select *  from c where _c7='TX' "
df.show()
df2=spark.sql(SQL)
df2.show()
df2.printSchema()
df2.coalesce(1).write.mode("overwrite").option("compression","uncompressed").format(OUTF).save(OUT)


