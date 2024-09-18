from pyspark import SparkConf,SparkContext
import os
import json
os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism","1")
sc=SparkContext(conf=conf)


file_rdd=sc.textFile("E:\python\python资料\第15章资料\资料\search_log.txt")
rdd1=file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:(x[0][:2],1)).\
    reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)
print(rdd1)

rdd2=file_rdd.map(lambda x:x.split("\t")).map(lambda x:(x[2],1)).reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending=False).take(3)
print(rdd2)

rdd3=file_rdd.map(lambda x:x.split("\t")).filter(lambda x:x[2]=="黑马程序员").\
    map(lambda x:(x[0][:2],1)).reduceByKey(lambda a,b:a+b).sortBy(lambda x:x[1],ascending=False).\
    take(1)
print(rdd3)

file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:{"time":x[0],"user_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]}).\
    saveAsTextFile("e:/output_json")