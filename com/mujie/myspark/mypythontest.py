from pyspark import SparkContext, SparkConf

if __name__ == '__main__':
    conf = SparkConf()
    conf.setAppName("tset")
    conf.setMaster("local")
    sc = SparkContext(conf=conf)
    lines = sc.textFile("./words")
    lines.foreach(print)


