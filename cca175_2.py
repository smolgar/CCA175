import pyspark
from pyspark.sql import SparkSession
import org.apache.spark.sql.avro
spark= SparkSession.builder.appName('c').enableHiveSupport().getOrCreate()

IN="/public/nyse/NYSE*.*"
OUT="/user/shree624/problem1/"
INF="csv"
OUTF="csv"

SQL="select Count(1) as CNT from mt"


df = spark.read.format(INF).load(IN)
df.show()
df.printSchema()
exit 
df1=df.createOrReplaceTempView('mt')

df2= spark.sql(SQL)
df2.show(4)
df2.printSchema()

df2.coalesce(1).write.mode("overwrite").format(OUTF).save(OUT)

