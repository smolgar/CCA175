import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

spark = SparkSession.builder.appName("test").enableHiveSupport().getOrCreate()

df1=spark.read.format("csv").load("/public/retail_db/orders/part-00000")
df2=spark.read.format("csv").load("/public/retail_db/customers/part-00000")

df1.createOrReplaceTempView("Orders")
df2.createOrReplaceTempView("customer")

df1.show()
df2.show()
df3=spark.sql("select a._c1 as customer_fname,a._c2 as customer_lname, count(b._c0) as order_count from Orders b join customer a on a._c0=b._c0 where month(to_date(b._c1))='07' and year(to_date(b._c1))='2013' group by a._c1,a._c2 order by count(b._c0) desc, a._c1, a._c2")

df3.write.format("json").mode("overwrite").option("compression","uncompressed").save("/user/shree624/cca175_practice_test1/problem3/data/order_count_by_customer")
