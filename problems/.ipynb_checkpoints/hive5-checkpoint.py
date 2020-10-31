import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

spark = SparkSession.builder.appName("test").enableHiveSupport().getOrCreate()

df1=spark.read.format("json").load("/public/retail_db_json/orders/part*")
df2=spark.read.format("json").load("/public/retail_db_json/order_items/part*")
df3=spark.read.format("json").load("/public/retail_db_json/products/part*")

df1.createOrReplaceTempView("o")
df2.createOrReplaceTempView("ot")
df3.createOrReplaceTempView("p")

df1.show()
df2.show()
df2.show()
df4=spark.sql(" select product_name|| ',' || round(rev,2) from (select \
	p.product_name ,  \
	sum(order_item_subtotal) as rev \
	, rank() over ( \
	 order by sum(order_item_subtotal) desc ) as RANK1 \
	from o join ot on o.order_id=ot.order_item_order_id Join p on p.product_id=ot.order_item_order_id \
	where to_date(o.order_date)= '2013-07-26' and o.order_status in ('COMPLETE','CLOSED') \
	group by p.product_name ) where RANK1 <=5 order by rev desc")
df4.show(40)
df4.write.format("text").mode("overwrite").option("compression","uncompressed").save("/user/shree624/cca175_practice_test1/problem5/data/top5_products")
