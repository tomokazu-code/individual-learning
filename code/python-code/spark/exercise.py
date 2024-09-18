

from pyspark import SparkConf,SparkContext
import os
import json
os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

file_rdd=sc.textFile("E:\python\python资料\第15章资料\资料\orders.txt")

rdd1=file_rdd.flatMap(lambda x:x.split("|"))
rdd_dict=rdd1.map(lambda x:json.loads(x))
rdd2=rdd_dict.map(lambda x:(x["areaName"],int(x["money"])))
rdd3=rdd2.reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1] ,ascending=False)


# print(rdd3.collect())

rdd4=rdd_dict.map(lambda x:x["category"]).distinct()
# print(rdd4.collect())

beijing_data_rdd=rdd_dict.filter(lambda x:x["areaName"]=='北京').map(lambda x:x["category"]).distinct()

print(beijing_data_rdd.collect())
