# Design Youtube


1 ) Functionnal requirment:
- Upload videos from a user perspective
- Watch videos from a user perspective

Non Functional Requirments : 
Reliability 
Availability > over consistency  / Eventual consistent 
Minimize the latency ( video should start immediately )

2 ) Estimates :
1Billion DAU
Watching => 5 videos / day 
50 Million videos stored


3 ) High level design :

Key takeways:
- Google drive is built on object storage 
- S3, google storage they handle replication => Reliability covered 
- LRU cache ?
