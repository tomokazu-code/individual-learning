from pyspark import SparkConf,SparkContext

import os
os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd1=sc.parallelize(([('男',324),('女',43),('男',41)]))

rdd2=rdd1.reduceByKey(lambda a,b:a+b)
print(rdd2.collect())