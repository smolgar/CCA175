import pyspark 
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
conf=SparkConf()
conf.set("spark.jar.packages","com.databricks:spark-avro_2.3:4.0.0")
spark = SparkSession.builder.appName("tset").enableHiveSupport().config(conf=conf).getOrCreate()

inn="/public/orders/part-00000"
out="/user/shree624/Solutions/problem4/"
out1="/user/shree624/Solutions/problem4/part*"
inf="csv"
outf="parquet"
df=spark.read.format(inf).option("sep",",").load(inn)
df.show(5)



df.write.format('com.databricks.spark.avro').save(out)


df=spark.read.format('com.databricks.spark.avro').load(out1)

