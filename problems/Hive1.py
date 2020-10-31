import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Testing').enableHiveSupport().getOrCreate()

IN="/public/orders/part-00000"
OUT="/user/shree624/Solutions/problem1"

SQL="select cast(_c1 as Date),count(1) from MyTable where _c3='COMPLETE' group by cast(_c1 as Date) order by cast(_c1 as Date)"
df=spark.read.format("csv").option("sep",",").option("header","false").load(IN)
df.show(5)
df1=df.createOrReplaceTempView("MyTable")
df2= spark.sql(SQL)
df2.write.format("csv").option("header","false").option("compression","uncompressed").mode("overwrite").save(OUT)
df2.show()
