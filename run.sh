hdfs dfs -mkdir books-input
hdfs dfs -put books-input/*.txt books-input
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input books-input -output books-output
hdfs dfs -get books-output
