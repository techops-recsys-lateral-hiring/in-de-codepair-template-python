import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    # create Spark context with necessary configuration
    sc = SparkContext("local","PySpark Word Count Exmaple")

    # read data from text file and split each line into words
    words = sc.textFile("input.txt").flatMap(lambda line: line.split(" "))

    # count the occurrence of each word
    wordCounts = words.map(lambda word: word.replace(",","")).map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

    output = wordCounts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

