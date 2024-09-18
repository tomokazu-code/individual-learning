from pyspark import SparkConf,SparkContext
# 创建SparkConf对象
conf=SparkConf().setMaster("local[*]").setAppName("tset_spark_app")

# 基于SparkConf对象创建SparkContsxt对象

sc=SparkContext(conf=conf)


#打印PySpark运行版本
print(sc.version)

sc.stop()