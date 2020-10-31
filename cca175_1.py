import pyspark
from pyspark.sql import SparkSession

s = SparkSession.builder \
     .master("local") \
    .appName("Word Count") \
 .getOrCreate()


O="/user/shree624/problem1"
I="/public/nyse/NYSE*.*"
inf="csv"
outf="csv"
m="overwrite"
part=1
table="table"
opt1="compression"
optv="snappy"

SQL="select count(1) from table"

df=s \
	.read \
	.format(inf) \
	.load(I)

df1= df.createOrReplaceTempView(table)

df2=s.sql(SQL)

df2.coalesce(part).write.mode(m).format(outf).save(O)
