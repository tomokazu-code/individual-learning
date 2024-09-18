from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5,6])

#filter
#对rdd逐个处理，得到true的保留下来
rdd2=rdd.filter(lambda num:num%2==0)
print(rdd2.collect())
