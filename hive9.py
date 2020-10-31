import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('test').enableHiveSupport().getOrCreate()

in1="/public/retail_db/order_items/part*"

out="/user/shree624/problem1/"

inf="hive"
outf="parquet"

#df1=spark.read.format("csv").load(in1)
#df1.show(5)
#df1.createOrReplaceTempView('mt')
SQL= "select * from sree_retail_db.AvgCost"

df2=spark.sql(SQL)
df2.show()
df2.coalesce(1).write.format(outf).option("compression","uncompressed").mode("overwrite").save(out)
