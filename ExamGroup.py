import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").enableHiveSupport().getOrCreate()

IN="/public/retail_db/orders/part-00000"
IN1="/public/retail_db/customers/part-00000"
OUT="/user/shree624/problem2/"
INF="csv"
OUTF="json"

df= spark.read.format(INF).load(IN)
df1= spark.read.format(INF).load(IN1)
df.createOrReplaceTempView('o')
df1.createOrReplaceTempView('c')
SQL="select customer_id,customer_fname,CNT from (Select c._c0 as customer_id,c._c1 as customer_fname,cast(count(o._c0) as int)  as CNT from o join c on o._c0=c._c0 where o._c3='COMPLETE' group by c._c0,c._c1) where CNT > 4 order by CNT asc"
df.show()
df2=spark.sql(SQL)
df2.show()
df2.printSchema()
df2.coalesce(1).write.mode("overwrite").option("compression","gzip").format(OUTF).save(OUT)


