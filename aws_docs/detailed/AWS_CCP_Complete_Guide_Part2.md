# 🎓 AWS Certified Cloud Practitioner (CLF-C02) - Part 2

## DOMAIN 3: CLOUD TECHNOLOGY & SERVICES (34%)

---

## 📋 Quick Navigation

- **Part 1**: Exam Overview, Cloud Concepts, Security
- **Part 2**: Cloud Technology & Services (This file)
- **Part 3**: Networking, Additional Services, Billing & Support
- **Part 4**: Practice Questions, Exam Strategy, Resources

---

## 💻 COMPUTE SERVICES

### 3.1 Amazon EC2 (Elastic Compute Cloud)

**What is EC2?**

- Virtual servers in the cloud
- Complete control over computing resources
- Pay only for what you use
- Launch in minutes

**Instance Types (Know the Categories):**

**1. General Purpose (T, M series)**

- Balanced compute, memory, networking
- **T3/T3a**: Burstable, web servers, dev environments
- **M5/M6**: Steady workload, app servers
- **Use case**: Web apps, small databases

**2. Compute Optimized (C series)**

- High-performance processors
- **C5/C6**: Batch processing, gaming, HPC
- **Use case**: CPU-intensive workloads

**3. Memory Optimized (R, X series)**

- Fast performance for large datasets
- **R5/R6**: In-memory databases, big data
- **X1**: SAP HANA, high-memory needs
- **Use case**: Real-time processing, caching

**4. Storage Optimized (I, D series)**

- High sequential read/write
- **I3**: NoSQL databases, data warehousing
- **D2**: MapReduce, distributed file systems
- **Use case**: High IOPS, large datasets

**5. Accelerated Computing (P, G, F series)**

- Hardware accelerators (GPU, FPGA)
- **P3/P4**: Machine learning, HPC
- **G4**: Graphics-intensive, ML inference
- **Use case**: AI/ML, video rendering

**EC2 Pricing Models (CRITICAL!):**

**1. On-Demand**

- Pay by the second (Linux) or hour (Windows)
- No commitment
- **Use case**: Short-term, unpredictable workloads
- **Cost**: Highest
- **Example**: $0.10/hour

**2. Reserved Instances (RI)**

- 1 or 3-year commitment
- Up to 75% discount
- **Types**:
  - Standard RI: Most discount, can't change instance type
  - Convertible RI: Less discount, can change instance type
  - Scheduled RI: Specific time windows
- **Use case**: Steady-state, predictable workloads
- **Example**: $0.03/hour (70% savings)

**3. Savings Plans**

- Commit to $/hour for 1 or 3 years
- Up to 72% discount
- More flexible than RIs
- **Types**:
  - Compute Savings Plans: Most flexible
  - EC2 Instance Savings Plans: Specific instance family
- **Use case**: Flexible workloads

**4. Spot Instances**

- Bid on spare capacity
- Up to 90% discount
- Can be interrupted with 2-minute warning
- **Use case**: Fault-tolerant, flexible workloads
- **Example**: Batch jobs, data analysis, CI/CD
- **NOT for**: Databases, critical apps

**5. Dedicated Hosts**

- Physical server dedicated to you
- Most expensive
- **Use case**: Compliance, licensing (per-socket, per-core)
- Visibility into sockets, cores

**6. Dedicated Instances**

- Instances on hardware dedicated to you
- May share hardware with other instances in your account
- Less expensive than Dedicated Hosts

**Pricing Comparison:**

```
Spot (90% off) < Reserved (75% off) < Savings Plans (72% off) < On-Demand (0% off) < Dedicated
```

**EC2 Features:**

**Auto Scaling**

- Automatically adjust capacity
- Maintain application availability
- **Components**:
  - Launch Template: What to launch
  - Auto Scaling Group: Where and when
  - Scaling Policies: How to scale
- **Scaling Types**:
  - Target Tracking: Maintain metric (e.g., 50% CPU)
  - Step Scaling: Scale based on CloudWatch alarms
  - Scheduled Scaling: Predictable patterns
  - Predictive Scaling: ML-based forecasting

**Elastic Load Balancing (ELB)**

- Distribute traffic across instances
- **Types**:
  - **Application Load Balancer (ALB)**: HTTP/HTTPS, Layer 7
  - **Network Load Balancer (NLB)**: TCP/UDP, Layer 4, ultra-low latency
  - **Gateway Load Balancer**: Layer 3, third-party appliances
  - **Classic Load Balancer**: Legacy, Layer 4/7
- **Features**:
  - Health checks
  - SSL termination
  - Sticky sessions
  - Cross-zone load balancing

**EC2 User Data**

- Bootstrap script
- Runs at instance launch
- Install software, configure settings
- Runs as root user

**EC2 Metadata**

- Information about instance
- Access from within instance
- URL: http://169.254.169.254/latest/meta-data/
- **Examples**: instance-id, public-ip, security-groups

**Placement Groups**

- Control instance placement
- **Types**:
  - **Cluster**: Low latency, high throughput (same AZ-)
  - **Spread**: Reduce correlated failures (different hardware)
  - **Partition**: Large distributed workloads (Hadoop, Cassandra)

### 3.2 AWS Lambda

**What is Lambda?**

- Serverless compute service
- Run code without managing servers
- Pay only for compute time
- Automatic scaling

**Key Features:**

- **Languages**: Python, Node.js, Java, Go, C#, Ruby, PowerShell
- **Timeout**: Max 15 minutes
- **Memory**: 128 MB to 10 GB
- **Pricing**: Per request + compute time (GB-seconds)
- **Free Tier**: 1M requests/month, 400,000 GB-seconds

**Use Cases:**

- Real-time file processing
- Data transformation
- Backends for web/mobile apps
- IoT backends
- Scheduled tasks (cron jobs)

**Lambda vs EC2:**
| Feature | Lambda | EC2 |
|---------|--------|-----|
| Management | Serverless | You manage |
| Scaling | Automatic | Manual/Auto Scaling |
| Pricing | Per request | Per hour |
| Duration | Max 15 min | Unlimited |
| Use case | Event-driven | Long-running |

**Event Sources:**

- S3 (file upload)
- DynamoDB (table changes)
- API Gateway (HTTP requests)
- CloudWatch Events (scheduled)
- SNS, SQS, Kinesis

### 3.3 AWS Elastic Beanstalk

**What is Elastic Beanstalk?**

- PaaS for deploying applications
- Handles infrastructure automatically
- You focus on code

**Supported Platforms:**

- Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker

**Features:**

- Automatic capacity provisioning
- Load balancing
- Auto Scaling
- Health monitoring
- Platform updates

**Components:**

- **Application**: Container for environments
- **Environment**: Collection of AWS resources
- **Environment Tier**: Web server or worker
- **Platform**: OS, language, web server

**Use Cases:**

- Quick deployment
- Developers who don't want to manage infrastructure
- Standard web applications

**Pricing:**

- No additional charge
- Pay for underlying resources (EC2, ELB, etc.)

### 3.4 Amazon Lightsail

**What is Lightsail?**

- Simplified compute service
- Fixed monthly price
- Includes everything: compute, storage, networking
- For simple workloads

**Features:**

- Pre-configured applications (WordPress, LAMP, etc.)
- Virtual private servers
- Managed databases
- Load balancers
- Static IPs
- DNS management

**Pricing:**

- Fixed monthly plans ($3.50 - $160/month)
- Predictable costs

**Use Cases:**

- Simple web applications
- Websites
- Dev/test environments
- Small businesses

**Lightsail vs EC2:**

- Lightsail: Simple, fixed price, limited options
- EC2: Complex, flexible, pay-as-you-go

### 3.5 AWS Batch

**What is AWS Batch?**

- Run batch computing workloads
- Automatically provisions resources
- Manages job scheduling

**Use Cases:**

- Data processing
- Image/video rendering
- Financial modeling
- Genomics research

**Components:**

- **Jobs**: Units of work
- **Job Definitions**: How to run jobs
- **Job Queues**: Where jobs wait
- **Compute Environments**: Where jobs run

### 3.6 Amazon ECS & EKS (Container Services)

**Amazon ECS (Elastic Container Service)**

- Run Docker containers
- Fully managed
- Integrates with AWS services
- **Launch Types**:
  - EC2: You manage instances
  - Fargate: Serverless, AWS manages

**Amazon EKS (Elastic Kubernetes Service)**

- Managed Kubernetes
- Run Kubernetes on AWS
- Compatible with standard Kubernetes tools

**AWS Fargate**

- Serverless compute for containers
- No EC2 instances to manage
- Pay for resources used

**Use Cases:**

- Microservices
- Batch processing
- Machine learning

---

## 💾 STORAGE SERVICES

### 3.7 Amazon S3 (Simple Storage Service)

**What is S3?**

- Object storage service
- Store and retrieve any amount of data
- 99.999999999% (11 9's) durability
- Unlimited storage

**Key Concepts:**

**Buckets**

- Containers for objects
- Globally unique names
- Region-specific
- Flat structure (no folders, just prefixes)

**Objects**

- Files stored in buckets
- Key (name) + Value (data)
- Max size: 5 TB
- Metadata, version ID, access control

**S3 Storage Classes (MEMORIZE!):**

**1. S3 Standard**

- Frequently accessed data
- Low latency, high throughput
- 99.99% availability
- **Use case**: Active data, websites, content distribution
- **Cost**: Highest storage, lowest retrieval

**2. S3 Intelligent-Tiering**

- Automatic cost optimization
- Moves data between tiers based on access patterns
- No retrieval fees
- **Use case**: Unknown or changing access patterns
- **Tiers**: Frequent, Infrequent, Archive, Deep Archive

**3. S3 Standard-IA (Infrequent Access)**

- Less frequently accessed
- Lower storage cost, retrieval fee
- 99.9% availability
- **Use case**: Backups, disaster recovery
- **Minimum**: 30 days, 128 KB

**4. S3 One Zone-IA**

- Single AZ (vs 3 AZs)
- 20% cheaper than Standard-IA
- 99.5% availability
- **Use case**: Secondary backups, recreatable data
- **Risk**: Data lost if AZ fails

**5. S3 Glacier Instant Retrieval**

- Archive data with instant access
- 68% cheaper than Standard-IA
- Millisecond retrieval
- **Use case**: Medical images, news archives
- **Minimum**: 90 days

**6. S3 Glacier Flexible Retrieval**

- Archive data
- Retrieval: Minutes to hours
- **Retrieval options**:
  - Expedited: 1-5 minutes
  - Standard: 3-5 hours
  - Bulk: 5-12 hours
- **Use case**: Long-term backups
- **Minimum**: 90 days

**7. S3 Glacier Deep Archive**

- Lowest cost storage
- Retrieval: 12-48 hours
- **Use case**: Compliance, regulatory archives
- **Minimum**: 180 days
- **Example**: 7-10 year retention

**Storage Class Comparison:**

```
Cost (Storage): Standard > IA > One Zone-IA > Glacier IR > Glacier > Deep Archive
Cost (Retrieval): Deep Archive > Glacier > IA > Standard
Speed: Standard = IA = Glacier IR > Glacier > Deep Archive
```

**S3 Features:**

**Versioning**

- Keep multiple versions of objects
- Protect against accidental deletion
- Can be suspended (not disabled)
- **Use case**: Backup, rollback

**Replication**

- **Cross-Region Replication (CRR)**: Different regions
- **Same-Region Replication (SRR)**: Same region
- Requires versioning
- **Use cases**: Compliance, lower latency, disaster recovery

**Lifecycle Policies**

- Automate transitions between storage classes
- Delete old versions
- **Example**:
  - 30 days → Standard-IA
  - 90 days → Glacier
  - 365 days → Delete

**S3 Transfer Acceleration**

- Fast uploads using CloudFront edge locations
- 50-500% faster
- **Use case**: Large files, global users

**S3 Event Notifications**

- Trigger actions on object events
- **Targets**: Lambda, SQS, SNS
- **Events**: Object created, deleted, restored

**S3 Security:**

**Encryption at Rest**

- **SSE-S3**: AWS-managed keys (default)
- **SSE-KMS**: KMS-managed keys (audit trail)
- **SSE-C**: Customer-provided keys
- **Client-side**: Encrypt before upload

**Encryption in Transit**

- HTTPS/SSL

**Access Control**

- **Bucket Policies**: JSON, resource-based
- **IAM Policies**: User/role-based
- **ACLs**: Legacy, object-level
- **Block Public Access**: Account/bucket level

**S3 Pricing:**

- Storage (per GB)
- Requests (GET, PUT, etc.)
- Data transfer out
- Management features

**S3 Use Cases:**

- Backup and restore
- Disaster recovery
- Archive
- Data lakes
- Static website hosting
- Content distribution
- Application hosting

### 3.8 Amazon EBS (Elastic Block Store)

**What is EBS?**

- Block storage for EC2
- Network-attached storage
- Persistent (survives instance termination)
- Single AZ (attach to instances in same AZ)

**EBS Volume Types (KNOW THE DIFFERENCES!):**

**1. General Purpose SSD (gp3, gp2)**

- Balanced price/performance
- **gp3**:
  - 3,000 IOPS baseline
  - 125 MB/s throughput
  - Can provision up to 16,000 IOPS
  - Cheaper than gp2
- **gp2**:
  - 3 IOPS per GB (min 100, max 16,000)
  - Burst to 3,000 IOPS
- **Use case**: Boot volumes, dev/test, low-latency apps
- **Size**: 1 GB - 16 TB

**2. Provisioned IOPS SSD (io2, io1)**

- Highest performance SSD
- **io2 Block Express**: Up to 256,000 IOPS
- **io2**: Up to 64,000 IOPS, 99.999% durability
- **io1**: Up to 64,000 IOPS
- **Use case**: Databases (MongoDB, Cassandra, SQL Server)
- **Size**: 4 GB - 16 TB

**3. Throughput Optimized HDD (st1)**

- Low-cost HDD
- Throughput-intensive workloads
- 500 IOPS max
- 500 MB/s throughput
- **Use case**: Big data, data warehouses, log processing
- **Size**: 125 GB - 16 TB
- **Cannot** be boot volume

**4. Cold HDD (sc1)**

- Lowest cost HDD
- Infrequently accessed data
- 250 IOPS max
- 250 MB/s throughput
- **Use case**: Archival, infrequent access
- **Size**: 125 GB - 16 TB
- **Cannot** be boot volume

**Volume Type Selection:**

```
Database (high IOPS) → io2
Boot volume → gp3
Big data (throughput) → st1
Archive (cost) → sc1
```

**EBS Features:**

**Snapshots**

- Backup of EBS volume
- Stored in S3 (managed by AWS)
- Incremental (only changed blocks)
- Can copy across regions
- Can create volume from snapshot
- **Use case**: Backup, disaster recovery, migration

**Encryption**

- Encrypt volumes and snapshots
- Uses KMS
- Minimal performance impact
- Encrypted snapshots from encrypted volumes

**Multi-Attach (io1/io2 only)**

- Attach volume to multiple instances
- Same AZ only
- Up to 16 instances
- **Use case**: Clustered applications

**EBS vs Instance Store:**
| Feature | EBS | Instance Store |
|---------|-----|----------------|
| Persistence | Yes | No (ephemeral) |
| Backup | Snapshots | Manual |
| Performance | Network | Physical |
| Use case | Data retention | Temporary, cache |

### 3.9 Amazon EFS (Elastic File System)

**What is EFS?**

- Managed NFS (Network File System)
- Shared file storage
- Multiple EC2 instances can access
- Elastic (grows/shrinks automatically)
- Linux only

**Features:**

- Petabyte-scale
- Multi-AZ (regional service)
- Pay for what you use
- No capacity planning
- POSIX-compliant

**Storage Classes:**

- **Standard**: Frequently accessed
- **Infrequent Access (IA)**: Lower cost, retrieval fee
- **Lifecycle management**: Auto-move to IA

**Performance Modes:**

- **General Purpose**: Low latency (default)
- **Max I/O**: Higher latency, higher throughput

**Throughput Modes:**

- **Bursting**: Scales with size
- **Provisioned**: Fixed throughput

**Use Cases:**

- Content management
- Web serving
- Home directories
- Shared development environments

**EFS vs EBS vs S3:**
| Feature | EFS | EBS | S3 |
|---------|-----|-----|-----|
| Type | File | Block | Object |
| Access | Multiple instances | Single instance | Internet |
| Scope | Regional | AZ | Global |
| Use case | Shared files | Instance storage | Static content |

### 3.10 AWS Storage Gateway

**What is Storage Gateway?**

- Hybrid cloud storage
- Connect on-premises to AWS
- Seamless integration

**Types:**

**1. File Gateway**

- NFS/SMB interface
- Store files as objects in S3
- Local cache for low latency
- **Use case**: File shares, backups

**2. Volume Gateway**

- iSCSI block storage
- **Stored Volumes**: Full copy on-premises, async backup to S3
- **Cached Volumes**: Frequently accessed data on-premises, full copy in S3
- **Use case**: Backup, disaster recovery

**3. Tape Gateway**

- Virtual tape library (VTL)
- Replace physical tapes
- Store in S3 and Glacier
- **Use case**: Backup applications using tape

### 3.11 AWS Snow Family

**Purpose**: Physical devices to move large amounts of data

**AWS Snowcone**

- Smallest device
- 8 TB storage
- 4 GB memory, 2 vCPUs
- Rugged, portable
- **Use case**: Edge computing, IoT

**AWS Snowball Edge**

- **Storage Optimized**: 80 TB, 40 vCPUs
- **Compute Optimized**: 42 TB, 52 vCPUs, GPU
- Local compute and storage
- **Use case**: Large migrations, edge computing

**AWS Snowmobile**

- Shipping container on truck
- 100 PB capacity
- For exabyte-scale transfers
- **Use case**: Data center migration

**When to Use:**

- Over 10 TB of data
- Limited bandwidth
- High network costs
- **Rule of thumb**: If transfer takes more than a week, use Snow

---

## 🗄️ DATABASE SERVICES

### 3.12 Amazon RDS (Relational Database Service)

**What is RDS?**

- Managed relational database
- AWS handles: provisioning, patching, backups, recovery
- You manage: schema, queries, optimization

**Supported Engines:**

- **Amazon Aurora**: AWS proprietary, MySQL/PostgreSQL compatible
- **MySQL**
- **PostgreSQL**
- **MariaDB**
- **Oracle**
- **SQL Server**

**Key Features:**

**Automated Backups**

- Daily full backup
- Transaction logs every 5 minutes
- Retention: 0-35 days
- Point-in-time recovery

**DB Snapshots**

- Manual backups
- Retained until you delete
- Can copy across regions

**Multi-AZ Deployment**

- High availability
- Synchronous replication to standby
- Automatic failover (60-120 seconds)
- Same region, different AZ
- **Use case**: Production databases
- **NOT for**: Read scaling (use Read Replicas)

**Read Replicas**

- Asynchronous replication
- Up to 15 replicas (Aurora)
- Can be in different regions
- **Use case**: Read-heavy workloads, reporting
- Can be promoted to standalone DB

**RDS Proxy**

- Connection pooling
- Reduce database load
- Improve failover time
- **Use case**: Lambda functions, connection-heavy apps

**RDS Pricing:**

- Instance hours
- Storage (GB/month)
- Backup storage
- Data transfer

**RDS vs EC2 Database:**
| Feature | RDS | EC2 |
|---------|-----|-----|
| Management | AWS | You |
| Patching | Automatic | Manual |
| Backups | Automatic | Manual |
| Scaling | Easy | Complex |
| Cost | Higher | Lower |
| Control | Less | Full |

### 3.13 Amazon Aurora

**What is Aurora?**

- AWS proprietary database
- MySQL and PostgreSQL compatible
- 5x faster than MySQL, 3x faster than PostgreSQL
- Cloud-optimized

**Key Features:**

- **Storage**: Auto-scaling (10 GB to 128 TB)
- **Replication**: 6 copies across 3 AZs
- **Read Replicas**: Up to 15
- **Backtrack**: Rewind database to any point in time
- **Global Database**: Cross-region replication (<1 second)
- **Aurora Serverless**: Auto-scaling, pay per second

**Aurora Serverless**

- On-demand, auto-scaling
- No capacity planning
- Pay per second
- **Use case**: Infrequent, intermittent, unpredictable workloads

**Aurora vs RDS:**

- Aurora: Faster, more expensive, AWS proprietary
- RDS: Standard engines, less expensive

### 3.14 Amazon DynamoDB

**What is DynamoDB?**

- Fully managed NoSQL database
- Key-value and document database
- Serverless
- Single-digit millisecond latency
- Automatic scaling

**Key Concepts:**

**Tables**

- Collection of items
- No schema required

**Items**

- Collection of attributes
- Similar to rows

**Attributes**

- Key-value pairs
- Similar to columns

**Primary Key**

- **Partition Key**: Single attribute
- **Composite Key**: Partition key + Sort key

**Capacity Modes:**

**1. On-Demand**

- Pay per request
- No capacity planning
- Automatic scaling
- **Use case**: Unpredictable workloads

**2. Provisioned**

- Specify read/write capacity units
- Auto Scaling available
- More cost-effective for predictable workloads
- **Use case**: Steady, predictable traffic

**Features:**

**DynamoDB Streams**

- Capture table changes
- Trigger Lambda functions
- **Use case**: Real-time processing, replication

**Global Tables**

- Multi-region, multi-active
- Automatic replication
- **Use case**: Global applications, disaster recovery

**DynamoDB Accelerator (DAX)**

- In-memory cache
- Microsecond latency
- No code changes
- **Use case**: Read-heavy workloads

**Point-in-Time Recovery (PITR)**

- Continuous backups
- Restore to any point in last 35 days

**DynamoDB vs RDS:**
| Feature | DynamoDB | RDS |
|---------|----------|-----|
| Type | NoSQL | SQL |
| Schema | Flexible | Fixed |
| Scaling | Automatic | Manual |
| Queries | Key-based | SQL |
| Use case | High-scale, simple queries | Complex queries, transactions |

### 3.15 Amazon ElastiCache

**What is ElastiCache?**

- Managed in-memory cache
- Reduce database load
- Microsecond latency

**Engines:**

**1. Redis**

- Advanced data structures
- Persistence
- Replication
- Backup/restore
- Multi-AZ
- **Use case**: Complex caching, session store, leaderboards

**2. Memcached**

- Simple key-value
- Multi-threaded
- No persistence
- **Use case**: Simple caching, object caching

**Use Cases:**

- Database query caching
- Session storage
- Real-time analytics
- Gaming leaderboards

### 3.16 Amazon Redshift

**What is Redshift?**

- Data warehouse
- Petabyte-scale
- Columnar storage
- Massively parallel processing (MPP)
- SQL-based

**Features:**

- 10x faster than traditional data warehouses
- Compression
- Parallel queries
- **Redshift Spectrum**: Query S3 data directly

**Use Cases:**

- Business intelligence
- Analytics
- Reporting
- Data warehousing

**Redshift vs RDS:**

- Redshift: Analytics, OLAP, read-heavy
- RDS: Transactional, OLTP, read-write

### 3.17 Amazon Neptune

**What is Neptune?**

- Graph database
- Highly connected data
- Supports: Gremlin, SPARQL

**Use Cases:**

- Social networks
- Recommendation engines
- Fraud detection
- Knowledge graphs

### 3.18 Amazon DocumentDB

**What is DocumentDB?**

- MongoDB-compatible
- Document database
- Fully managed
- JSON documents

**Use Cases:**

- Content management
- Catalogs
- User profiles

### 3.19 Amazon Keyspaces

**What is Keyspaces?**

- Apache Cassandra-compatible
- Serverless
- Scalable

**Use Cases:**

- IoT
- Time-series data
- High-throughput applications

### 3.20 Amazon QLDB (Quantum Ledger Database)

**What is QLDB?**

- Immutable ledger
- Cryptographically verifiable
- Centralized (not blockchain)

**Use Cases:**

- Financial transactions
- Supply chain
- Audit trails

---

## 📝 KEY EXAM TIPS - DOMAIN 3 (PART 2)

### Must Memorize:

✅ EC2 instance types and use cases  
✅ EC2 pricing models (On-Demand, Reserved, Spot, etc.)  
✅ Lambda characteristics (serverless, 15-min timeout)  
✅ S3 storage classes and use cases  
✅ EBS volume types (gp3, io2, st1, sc1)  
✅ RDS features (Multi-AZ, Read Replicas)  
✅ DynamoDB characteristics (NoSQL, serverless)  
✅ Database service selection (RDS vs DynamoDB vs Redshift)

### Common Exam Scenarios:

**Scenario 1**: "Cost-effective storage for infrequently accessed data?"

- **Answer**: S3 Standard-IA or S3 One Zone-IA

**Scenario 2**: "Run code without managing servers?"

- **Answer**: AWS Lambda

**Scenario 3**: "High-performance database for OLTP?"

- **Answer**: RDS with Provisioned IOPS (io2)

**Scenario 4**: "Lowest cost EC2 for fault-tolerant workload?"

- **Answer**: Spot Instances

**Scenario 5**: "Share files between multiple EC2 instances?"

- **Answer**: Amazon EFS

**Scenario 6**: "Archive data for 10 years, rarely accessed?"

- **Answer**: S3 Glacier Deep Archive

**Scenario 7**: "High availability for production database?"

- **Answer**: RDS Multi-AZ

**Scenario 8**: "NoSQL database with automatic scaling?"

- **Answer**: DynamoDB

**Scenario 9**: "Data warehouse for analytics?"

- **Answer**: Amazon Redshift

**Scenario 10**: "In-memory cache to reduce database load?"

- **Answer**: ElastiCache

---

## 🎯 STUDY CHECKLIST - PART 2

- [ ] Understand EC2 instance types and categories
- [ ] Memorized EC2 pricing models and use cases
- [ ] Know Lambda characteristics and limitations
- [ ] Can explain all S3 storage classes
- [ ] Understand EBS volume types and selection
- [ ] Know EFS vs EBS vs S3 differences
- [ ] Understand RDS features (Multi-AZ, Read Replicas)
- [ ] Know Aurora benefits and Serverless option
- [ ] Understand DynamoDB characteristics
- [ ] Can differentiate database services
- [ ] Know ElastiCache engines (Redis vs Memcached)
- [ ] Understand Redshift for data warehousing

---

**Continue to Part 3 for Networking, Additional Services, Billing & Support**

**Study Time for Part 2**: 15-18 hours  
**Practice Questions**: Complete 150+ questions on compute, storage, and database services
