recommendation engine

1 - Build a system that recommends entites on our site to a yser based on their prior activity ( or other factors )

2 - Do not recommend entities that have already been seen 

Non functional requirments :
- fetch recommendations as fast as possible : use cache, repopulate the cache quickly
- Frontend optimizations 

Use embedding : vector representation of our entity ( document, videos )
we can update our embedding model offline 

Process / approach : 
1 - Retrieval

- Fetch the last entities that a user interacted with 
- For each of these entities, fetch most k element entities for each of those
    => Using embeddings

2 - Ranking 
- Assign a score to all these embeddings
- Filter out all entities the user has seen 
- Sort and return to user

--------------------------------------------------------------------------------------------------------------
In hash based sharding, you apply a hash function to an entity's unique ID. 
The hash function produces a numerical value that is typically reduced modulo Number of nodes to determine which shard the record belongs to 

=> Uniform data distribution ( removing hotspots )
=> Parallelism 
=> Fault Isolation 
=> Deterministic way to decide where each record belongs to ( no need for a complex mapping of keys to shards )

Indexing 
The practice of creating a DS that allow for fast retrieval of records. In a database, we should index colums that are frequently accessed and used in queries 

=> Speeding up queries 
=> Efficient lookup 
=> Joins and range queries 



Sharding indexing and replication 


----------------------------------------------------------------------------------------------------------------

Queue vs Kafka 


Kafka
- Event Streaming & Log aggregation
- High Throughput 
- Durability and Fault tolerance : data can be re-read if need not lost 


Qeueue ( RabbitMQ, Amazon SQS )

- Task Distribution and Decoupling 