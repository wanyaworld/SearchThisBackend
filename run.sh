# Copy files
hdfs dfs -mkdir books-input
hdfs dfs -put books-input/*.txt books-input

# Run MR
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input books-input -output books-output

# Merge and get output
hadoop fs -cat books-output/part* > combined.txt
hdfs dfs -getmerge books-output/ output
