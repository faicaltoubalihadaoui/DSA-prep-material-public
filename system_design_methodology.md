# Requirement Clarifications
*Functionnal Requirments*
- Users should be able to create accounts
- Users should be able to update profile
- Users should be able to post answers/questions
.

*Non functionnal requirments*

<span style="color: #26B260">**Availability** : 

It means that any request to the system should receive a response, even if the response is outdated

<span style="color: #26B260">**Consistency** : 

Means all the nodes of the system are on the same page, have the same data at the same time

<span style="color: #26B260">**Eventual Consistency**:

In a distributed system, Availability and Consistency can't be achieved simultaneously.  Consequently, we may to favor Availability over Consistency.
This means that the system becomes highly available but can produce inconsistent states ( reads and writes ).
In a eventually consistent system, multiple copies of the same data are stored on different nodes and those nodes may not be in perfect sync with one another at all times.
This means that it's possible for different nodes to have slightly different versions of the same data, but the system will eventually converge on a single consistent state.

<span style="color: #26B260">**Latency**:

It is the amount of time it takes for a request to be processed and a response to be returned.
In a distributed system, requests and responses can be handlel by many nodes which are connected over a network.
Consequently, it is very important to measure the latency of the system because of the network lag involved. 

Low latency => Requests fulfilled quickly, it improves the performance of the system.

# Estimations

*Storage Estimates*

Memorize the table of storage estimations ( char, image, doc, video .)

*QPS Estimates*

Calculates the nbr of queries + responses received per second


You should have rough estimates for both Storage and QPS

# API Design

Give an example of REST API with HTTP protocol for some functionnal requirments above.


# Database Design

Expect to design/draw schema-like tables/columns and relationships with other tables ( SQL ) .

# System's Detailed Design 

* Read-Heavy system => Use Cache

* Low latency => Cache & CDN

* Write Heavy system => Message Queue for async processing 

* ACID compliant system => use SQL Database / RDBMS
    * Atomicity : A transaction is treated as a single indivisible unit 
    * Consistency : the system must be at every moment on a valid state, Integrity constraints should be maintained before and after the transaction ( enforcing constraints over data like PK and FK)
    * Isolation : Intermediate states of a transaction are not visible to other concurrent transactions ( concurrent transacations won't interfere with each other )
    * Durability : Once a transaction is committed, the changes are permanent, even in the event of a system crash ( the data is stored in disk, even if the server restarts or craches the data will still be there )

    #### Why SQL for ACID ?
    * ACID Compliant
    * Strongly Defined Schema : rigidity and enforcing data consistency
    * Concurrency Control : using locks and transactions to prevent conflicts between concurrent  calls
    * Data persistance when the system crash 
    * Ideal for complex queries
    * Use cases: any application where data integrity is critical : Financial systems, inventory management, bookings 

* NO ACID properties / unstructured data => NoSQL Database
    #### Why NoSQL for Non ACID ?
    * Flexbility and scalability : 
        * Schema-less, allowing dynamic and unstructured data by dropping consistency 
        * Designed for Horizontal scaling, handling large amount of data accross distributed systems

    * Eventual Consistency :In many cases, strong consistency is less critical, and eventual consistency is sufficient (e.g., social media updates, product catalogs).

    * High Performance : NoSQL databases prioritize read/write speed and low latency over strict consistency
    
    * Indexing

        Indexing in MongoDB improves the speed of query operations on a database. Without an index, MongoDB must scan every document in a collection to find matching result.

        an Index allosw mongoDB to efficiently locate documents that match the query.

        -> Benefits of Indexing

        - Faster query execution.
        - Reduces the load on the database for frequent or complex queries.

        -> Caution

        - Indexes consume additional memory and storage.
        - Too many indexes can slow down write operations like inserts and updates.

        -> Key Features of Indexing in MongoDB

        -> Default _id Index:

        - Every MongoDB collection has an index on the _id field by default.
        - This ensures that operations like finding a document by its ID are very efficient.

        -> Custom Indexes:
        - You can create indexes on other fields, such as name, email, or tags, to speed up queries.

    * Data Normalization 

    Data Normalization is the process of organizing data to reduce redundancy and improve data integrity.
    In MongoDB, normalization is intended to minimize duplication by splitting data into multiple collections.

    In a normalized schema, related data is stored in separate collections and referenced using unique identifiers.
    Example:

    - Users Collection: Contains user information.
    - Orders Collection: Contains orders with a reference to the user who placed them.

    ```Javascript
        // Users Collection
    {
    "_id": "userId1",
    "name": "John Doe",
    "email": "john@example.com"
    }

    // Orders Collection
    {
    "_id": "orderId1",
    "userId": "userId1",
    "product": "Laptop",
    "quantity": 1
    }
    ```

    Advantages of Normalization

        Reduces data redundancy.
        Easier to maintain consistency.
        Smaller document sizes.

    Advantages of Denormalization

        Fewer joins or lookups are required.
        Faster read operations.

# Sharding and Scalability :
Sharding and scalability are critical when choosing a database for large scale applications.
# MongoDB
Sharding is a mongoDB's built in mechanismù for horizontal scaling, allowing data to be distributed accross multiple servers ( shards )

- The data is partitioned based on a shard key
- each shard contains a subset of data, and queries are routed to the relevant shards.
- a config server proxy keeps track of the meta data and shard key ranges

Pros :

- Horizontal scaling : easily adding more servers to handle growing data volumes and traffic
- High availability : Data replication with shards ensures redundancy 
- Elasticity : automatic balancing redistributes data as shards are added

Scalability of MongoDB

    Designed for horizontal scalability, making it suitable for large, distributed systems.
    Ideal for handling massive volumes of unstructured, semi-structured, or rapidly changing data.
    Can handle large numbers of concurrent read/write operations effectively.

# SQL
MySQL were originally designed for vertical scaling ( adding more resources to a single server )
If you want horizontal scaling, you need a config or a third party tool

Horizontal Scaling is not native. you need to use vitess developed by youtube for example 
more challenging because you need to maintain data integrity 

Scalability of SQL

    Primarily designed for vertical scaling:
        Upgrading the hardware (CPU, RAM, disk) of the primary server.
    Scaling out (horizontal) is complex:
        Requires manual sharding and replication.
        Distributed SQL databases (e.g., CockroachDB, Google Spanner) address some of these challenges.


# Comparison: MongoDB vs. SQL

| **Aspect**              | **MongoDB (NoSQL)**                             | **SQL Databases**                              |
|--------------------------|------------------------------------------------|-----------------------------------------------|
| **Sharding**             | Native, automatic, and easy to set up          | Requires manual setup or third-party tools    |
| **Horizontal Scaling**   | Built-in, highly efficient                     | Complex, not natively supported in most cases |
| **Vertical Scaling**     | Less effective; MongoDB focuses on horizontal  | Primarily designed for vertical scaling       |
| **Consistency**          | Eventual consistency (can be tuned to strong)  | Strong consistency by default                 |
| **Schema Flexibility**   | Schema-less; supports dynamic schema changes   | Fixed schema; requires predefined structure   |
| **Joins and Relationships** | Limited support; favors embedding or manual joins | Excellent support for relational data         |
| **ACID Compliance**      | Partial (with tunable consistency)             | Full ACID compliance                          |
| **Use Cases**            | High-volume, unstructured, write-heavy data    | Structured, relational, transactional data    |
| **Ease of Setup for Scalability** | Simplified for distributed systems             | Complex for distributed environments          |
| **Best For**             | Social media, IoT, video platforms, analytics  | E-commerce, financial systems, ERP            |

Which is Better?

    MongoDB:
        Best for applications requiring high scalability, such as social media, IoT, or video platforms.
        Handles dynamic schemas and write-heavy workloads efficiently.
        Horizontal scaling makes it ideal for distributed systems.
        No Single points of failure 

    SQL:
        Better for applications requiring strong consistency, complex queries, and transactional support (e.g., e-commerce, financial systems).
        Vertical scaling works well for smaller datasets and simpler scalability needs.

## Hybrid Approach

Many modern systems use a **polyglot persistence strategy**, combining MongoDB for high-scale, unstructured data (e.g., user-generated content) and SQL databases for transactional, structured data. This approach leverages the strengths of both technologies.


![db1.png](/_resources/db1.png)  

![db2.png](/_resources/db2.png)  

![db3.png](/_resources/db3.png)  

![db4.png](/_resources/db4.png)  

![db5.png](/_resources/db5.png)  

![db6.png](/_resources/db6.png)  

![db7.png](/_resources/db7.png)  

![db8.png](/_resources/db8.png)  

![db9.png](/_resources/db9.png)  

![db10.png](/_resources/db10.png)  
![db11.png](/_resources/db11.jpg)  

# Types of Databases 
DynamoDB ( K-V data )
neo4j ( Graph database )
MongoDB ( document data)



# System Design details 

* Store complex data : videos /images => Blob/Object Storage


 
* Vertical scaling
refers to increasing resources ( such as CPU, memory or storage ) of a single machine to improve its performance or handle higher traffic / loads
+ Very Limited, machines have limited capacity

* Horizontal scaling 
adding more servers, machines to a system to distribute the workload and increase the overall capacity and performance
+ More powerful, scales infinteley 
+ Adding replicas => redundancy & Fault tolerance, elimitating single point failure
- complex and needs more configurations 

* Load Balancer ( Server - Reverse Proxy )
+ Directs incomming requests to the appropriate servers
+ It uses an algorithm : example : Round Robin algorithm but its not efficient / another one like hashing the request id in order to balance the workload
Balance the amount of traffic each server is getting => optimize performance and Availability


* CDN ( Content Delivery Network )
network of server located geographically closer to end users, designed to deliver web content efficiently by caching and serving it from nearby locations ( reducing latency )
+ It servers greatly static content like images, videos 
It is a technique of caching 

* Caching
The technique of storing frequently accessed data or content in a temporary storage lcoation ( cache ) to improve retrieval speed and 
limit network requests to the server
It can be using In memory cache, Local cache, or CPU built-in cache 

* IP ( Internet Protocol Address) An IP is an address that is unique numerical label assigned to each device connected to a computer network
* TCP ( Transmission control protocol ) is a communication protocol that ensures reliable, connection oriented transmission of data 
by partitionning it intro multiple packets, numbering them, and reassembling them at the end
TCP ensures all the data is sent, if a packet is lost it resends it

* DNS ( Domain Name system ) decentralized system that translates the domain name into an ip address
DNS register service, you map your domain that you bought from it to the IP address ( DNSA ) of the server on which the application is deployed
a record mapping, the OS cache it to not do a network connection each it 

* HTTP is a protocol that governs the communication between web browsers and servers, allowing sending requests and receiving responses
with multiple info such as the headers, the body, it allows sharing resources and retrieval of info over the Internet

* REST API paradigm/pattern standard around http apis : stateless and following consistent guidelines 
* GraphQL API paradigm/pattern that using a query language and that is flexible compared to REST, it uses a single request ( query ) and you can fetch 
multiple resources with a single request

* gRPC is also an API paradigm designed mained for comms between web servers 

* Web Sockets : communication protocol that provides real time, instanteanous bi directionnal communication between a client and a server 
using a single long lived connection. It used used when instant and continuous, exhcnage of data is required

* Sharding : is a technique in database management where data is horizontally divided and distributed accorss multiple servers or nodes
to improve performance, scalability and load balancing 

* Replication : is the process of creating and maintaining identical copies of data accross multiple servers or nodes, providing redundancy,
fault tolerance, and improved Availability in distributed systems.


################################################################### Scalability 
https://blog.algomaster.io/p/scalability


As System grows, the performance starts to degrade unless we adapt it to deal with that growth

Scalability is the property of a system to handle a growing amount of load by adding resources to the system

In order words, a system that can continuously evolve to support a growing amount of work is scalable 

How to scale ? More Users, More features, more data, more complexity, more geographies

How to scale a system ?
- Vertical Scaling 
- Horizontal Scaling 
- Load Balancing 
- Caching  : Sotre frequently accessed data in memory
- CDN ( Content Delivery Network )
It distributes static assets ( images, videos, etc)

- CDN :
![cdn.png](/_resources/cdn.png)  
- Sharding / partitionning
- Async communication : means deferring long running or non critical tasks to background queues or message brokers,
this ensures your main application remains responsive to users. 

Example: Slack uses asynchronous communication for messaging. When a message is sent, the sender's interface doesn't freeze; it continues to be responsive while the message is processed and delivered in the background.

- Microservices Architecture 
Example: Uber has evolved its architecture into microservices to handle different functions like billing, notifications, and ride matching independently, allowing for efficient scaling and rapid development.

- Auto Scaling : automatically adjusting the number of active servers based on the current load
This ensures that the system can handle spikes in traffice without manual intervention
Example : AWS auto scaling 

- Multi Region Deployment 
Deploy the application in multuple data centers or cloud regions to reduce latency and improve redundancy


################################################################## Latency Vs ThroughPut
https://aws.amazon.com/compare/the-difference-between-throughput-and-latency/?nc1=h_ls

Latency :  the delay that a user experiences when they send or receive data from the network 

Throughput : determines the number of users that can access the network at the same time

high performing networks direcly impact revenue generation and operational efficiency 

One of the most important factors is the location of where data originates and its intended destination. If your servers are in a different geographical region from your device, the data has to travel further, which increases latency. This factor is called propagation.

Latency and throughput work together to deliver high network connectivity and performance

################################################################## CAP Theorem
https://www.bmc.com/blogs/cap-theorem/

CAP theorem maintains that when a distributed database experiences a network failure, you can provide either consistency or availability but not both

It s a tradeoff. All other times, all three can be provided. But, in the event of a network failure, a choice must be made.

To some, the choice between consistency and availability is really a matter of philosophical discussion that s rarely made in practice.


The challenge of the CAP theorem is that you ideally want to achieve all three goals at the same time, but you can only choose two. Making the right choice makes all the difference. The trade-off between consistency, availability and getting the balance right depends on the application and what the user values


Examples of a consistent database include:

    Bank account balances
    Text messages
    Inventory
    Airline reservation systems
    Payrolls
    Student records
    Health records
    Energy management systems

Database options for prioritizing the consistency component of the CAP theorem:
    
    SQL
    MongoDB
    Redis
    HBase



Database options for prioritizing the availability component of the CAP theorem:

    Cassandra
    DynamoDB
    Cosmos DB



################################################################## ACID Transactions
https://redis.io/glossary/acid-transactions/
Atomicity : 

Atomicity in ACID transactions guarantees that a transaction is treated a single indivisible unit of work.
If any part of the transaction fails, the entire transactions must be rolled back, meaning that any changes made during the transaction are undone.
This ensures tgat the database remains in a consistent state, regardless of any failures that may occue during the transaction

Consistency : 

The database schema must satisfy all constraints and rules are satisfied at every moment, and any transaction taht violates these constraints must be rolled back to maintain the consistency of the database.
This ensures that the database maintains its integrity and the data remains accurate and reliable.

Isolation : 

This property ensures that each transaction operates independently of other transactions, which means that a transaction’s effects should only become visible to other transactions after it has been committed. This property prevents interference and conflicts between concurrent transactions, and helps maintain the integrity and consistency of the database.

Durability : 

This characteristic makes sure that, even in a system failure, the changes made to the database during a transaction are irreversible. Any changes made after a transaction is committed must persist, even if the system is destroyed or loses power.

Consider a banking app where a user wishes to transfer funds from one account to another, where the operation’s transaction might look like this:

    BEGIN TRANSACTION – An example of withdrawing money from the bank using a cheque, pay order, or through an ATM.
    Deduct the transfer amount from the source account.
    Add the transfer amount to the destination account.
    COMMIT – Updating the record of the transaction carried out by the customer.

The transaction is rolled back, and the database is restored to its initial state if any of its operations fail, such as if the source account does not have enough funds.

################################################################## Rate Limiting 
https://www.imperva.com/learn/application-security/rate-limiting/

What Is Rate Limiting?

Rate limiting is a technique to limit network traffic to prevent users from exhausting system resources. Rate limiting makes it harder for malicious actors to overburden the system and cause attacks like Denial of Service (DoS). This involves attackers flooding a target system with requests and consuming too much network capacity, storage, and memory.

APIs that use rate limiting can throttle or temporarily block any client that tries to make too many API calls. It might slow down a throttled user’s requests for a specified time or deny them altogether. Rate limiting ensures that legitimate requests can reach the system and access information without impacting the overall application’s performance.

################################################################## API Design 


################################################################# Strong Vs Eventual Consistency



################################################################# Distributed Tracing 



################################################################ Sync vs Async 


############################################################### Batch Processing vs Stream Processing 




############################################################### Fault Tolerance 




1 Byte (B) = 8 bits

    1 Byte = 8 bits

Kilobyte (KB)

    1 KB = 1,000 bytes (in the context of storage, typically used in file systems)
    1 KB = 103103 bytes

Megabyte (MB)

    1 MB = 1,000 KB = 106106 bytes
    1 MB = 1,000,000 bytes

Gigabyte (GB)

    1 GB = 1,000 MB = 109109 bytes
    1 GB = 1,000,000,000 bytes

Terabyte (TB)

    1 TB = 1,000 GB = 10121012 bytes
    1 TB = 1,000,000,000,000 bytes

Petabyte (PB)

    1 PB = 1,000 TB = 10151015 bytes
    1 PB = 1,000,000,000,000,000 bytes




#########################################  Design Spotify 


1 - Clarifying questions:
Brainstorming
- Songs / Music
- Playlists
- User 
- Artists
- Podcasts

Then ask the question : What should we focus on during this interview ?

Use cases Functional Requirments: 
- Finding and Playing Music

Constrain the problem to make it solvable within the hour

2 - High level metrics ( estimates )
Ask the question about how many users/ songs to the interviewer

Users : 1 billion user
Songs : 100 million
MP3 audio ~5 MB  ( make that assumation and ask the interview if he s okay with it)
Total audio storage : 500 TB
3x replication -> 1.5 PB  
1 KB by user -> 10^(12) B  => 1TB


3 - High level design 

App 
FE 
LB
Multiple instances of webserver
database

4 - Database design

For the audio, we can use AWS S3, because songs are immutable => Blobs of data
S3 is used for blob storage
it scales linearly great



important materials : 

replication vs sharding : https://www.youtube.com/watch?v=jLEp1XI_L6Q