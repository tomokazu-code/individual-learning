from pyspark import SparkConf,SparkContext

import os
os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"



conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5])

# def func(data):
#     return data*10

rdd2=rdd.map(lambda x:x*10).map(lambda x:x+5)



print(rdd2.collect())