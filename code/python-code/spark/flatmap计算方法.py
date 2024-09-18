from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"


conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd=sc.parallelize(["asfasdf fasf sadfs","afsdaffsf hgsdf","ghehewrth sdf"])

rdd2=rdd.flatMap(lambda x : x.split(" "))


print(rdd2.collect())