import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

spark = SparkSession.builder.appName("test").enableHiveSupport().getOrCreate()
spark.conf.set("spark.shuffel.partition.sql","1")
in1="/public/retail_db/orders/part*"
out="/user/shree624/cca175_practice_test1/problem6/data/orders_pending_payment"
inf="csv"
outf="orc"

df1=spark.read.format(inf).load(in1)
df1.show()

df1.createOrReplaceTempView("o")

SQL= "select _c0 , _c1 , _c2 , _c3  from o where _c3='PENDING_PAYMENT' order by _c0"

df4=spark.sql(SQL)
df4.show(40)
df4.coalesce(4).write.format(outf).mode("overwrite").option("compression","uncompressed").save(out)
