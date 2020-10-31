import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('test').enableHiveSupport().getOrCreate()

in1="/public/retail_db/customers/part*"
out="/user/shree624/problem1/"

inf="csv"
outf="parquet"

df1=spark.read.format("csv").load(in1)
df1.show(5)
df1.createOrReplaceTempView('mt')
SQL= "select _c7,count(1) as Tot_cust from mt group by _c7 order by _c7"

df2=spark.sql(SQL)

df2.coalesce(1).write.format(outf).mode("overwrite").save(out)
