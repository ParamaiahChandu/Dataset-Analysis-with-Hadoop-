# Dataset-Analysis-with-Hadoop
Utilizing Hadoop for Dataset Analysis  
  
After cloning the repository into CSCloud, to run my analysis, following command must be executed:  
hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -file /home/chanduph/asgn4/mapper.py -mapper /home/chanduph/asgn4/mapper.py -file /home/chanduph/asgn4/reducer.py -reducer /home/chanduph/asgn4/reducer.py -input /data/nyc/nyc-traffic.csv -output HadoopOutput  
  
This command will create a directory with the name 'HadoopOutput', that contains two files '_SUCCESS' and 'part-00000'. 'part-00000' file contains statistics output we need. If we again run the above command we will get an error because 'HadoopOutput' already exist. To avoid this error, we have to change the above command at the end, replace 'HadoopOutput' with any other name.  
  
Run the following command to get statistics output:  
hadoop fs -cat HadoopOutput/part-00000  
