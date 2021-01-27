# Copy files
hdfs dfs -mkdir books-input
#hdfs dfs -put books-input/*.txt books-input
hadoop fs -D fs.local.block.size=1000000000 -put books-input/*.txt books-input

# Run MR
real_cmd=\'
mapper_args=\'"mapper.py "$1\'
mapper_cmd=$mapper_args
real_cmd+=$mapper_cmd\'
#hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files mapper.py,reducer.py -mapper $mapper_cmd -reducer reducer.py -input books-input -output books-output
real_real_cmd='hadoop jar /usr/lib/hadoop/hadoop-streaming.jar -files mapper.py,reducer.py -mapper '
real_real_cmd+=$mapper_cmd
real_real_cmd+=' -reducer reducer.py -input books-input -output books-output'
eval $real_real_cmd

# Merge and get output
hadoop fs -cat books-output/part* > combined.txt
hdfs dfs -getmerge books-output/ output
