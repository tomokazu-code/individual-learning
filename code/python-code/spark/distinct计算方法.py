from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,1,2,3,3,3,6,5,5,4,4,5,5,6,5])

#rdd去重操作
rdd2=rdd.distinct()
print(rdd2.collect())

