import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('test').enableHiveSupport().getOrCreate()

in1="/public/retail_db/customers/part*"
out="/user/shree624/problem1/"

inf="csv"
outf="csv"

df1=spark.read.format("csv").load(in1)
df1.show(5)
df1.createOrReplaceTempView('mt')
SQL= "select _c1,_c2, substring(_c1,1,2) || _c2 as CocatCustname  from mt where _c7='TX'"

df2=spark.sql(SQL)
df2.show()
df2.coalesce(1).write.format(outf).mode("overwrite").save(out)
