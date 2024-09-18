from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON']="E:\python\python310\python.exe"
os.environ['HADOOP_HOME']="E:\python\hadoop\hadoop-3.0.0"
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set("spark.default.parallelism","1")
sc=SparkContext(conf=conf)

rdd1=sc.parallelize([1,2,3,4,5,6],numSlices=1)

rdd1.saveAsTextFile("E:/output")
