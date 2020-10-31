import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

conf = SparkConf()
conf.set("spark.jars.packages", "com.databricks:spark-avro_2.11:2.4.0")
spark = SparkSession.builder.appName("AVRO-Excersices"). \
config(conf= conf). \
getOrCreate()

spark.conf.set("spark.sql.legacy.replaceDatabricksSparkAvro.enabled","true")
inn="/public/orders/part-00000"
out="/user/shree624/Solutions/problem1"

#SQL="select sum(cast(_c2 as Bigint)) as Total_Value from mytable "

df=spark.read.format("csv").option('sep',',').option("header","false").load(inn)
df.printSchema()
df.show()

df.write.mode("overwrite").option("compression","snappy").format("avro").save(out)


