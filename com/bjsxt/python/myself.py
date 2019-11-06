from pyspark import SparkConf, SparkContext

def function():
    conf = SparkConf()
    conf.setAppName("tset")
    conf.setMaster("local")
    sc = SparkContext(conf=conf)
    lines = sc.textFile("./words")
    lines.foreach(print)

function()