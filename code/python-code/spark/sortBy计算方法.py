from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"

conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

rdd1=sc.textFile("E:/python/python资料/第15章资料/资料/hello.txt")
word_rdd=rdd1.flatMap(lambda x:x.split(" ")).map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)

#sortBy 指定位置排序，ascending=False降序

print(word_rdd.sortBy(lambda x:x[1],ascending=False).collect())
