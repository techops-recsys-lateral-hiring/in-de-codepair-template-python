import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    # create Spark context with necessary configuration
    sc = SparkContext("local","PySpark Sum Exmaple")

    
    rdd = sc.parallelize([4,9,7])

    sum = rdd.reduce(lambda a,b: a +b)

    print("sum=%i" %sum)

