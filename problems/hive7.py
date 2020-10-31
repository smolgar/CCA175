import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

spark = SparkSession.builder.appName("test").enableHiveSupport().getOrCreate()
spark.conf.set("spark.shuffel.partitions.sql","2")
in1="/public/h1b/h1b_kaggle/h1b*"
out="/user/shree624/cca175_practice_test1/problem7/data/h1b_data_noheader"
inf="csv"
outf="csv"

df1=spark.read.format(inf).option("header","true").load(in1)
df1.show()


df1.coalesce(4).write.format(outf).mode("overwrite").option("compression","uncompressed").save(out)
