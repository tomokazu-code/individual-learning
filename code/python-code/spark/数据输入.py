from pyspark import SparkConf,SparkContext
#数据输入
conf=SparkConf().setMaster("local[*]").setAppName("test_spark")
sc=SparkContext(conf=conf)

# #把对象加载到Spark内，成为RDD对象
# rdd1=sc.parallelize([1,2,3,4,5])
# rdd2=sc.parallelize((1,2,3,4,5))
#
# #查看rdd里面的东西，需要用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())

#将文件加载到Spark内，成为rdd对象

rdd=sc.textFile("E:/2011年1月销售数据.txt")
print(rdd.collect())

sc.stop()