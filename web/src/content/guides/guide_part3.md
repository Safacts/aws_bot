# 🎓 AWS Certified Cloud Practitioner (CLF-C02) - Part 3

## NETWORKING & ADDITIONAL SERVICES + DOMAIN 4: BILLING & SUPPORT

---

## 📋 Quick Navigation

- **Part 1**: Exam Overview, Cloud Concepts, Security
- **Part 2**: Cloud Technology & Services (Compute, Storage, Database)
- **Part 3**: Networking, Additional Services, Billing & Support (This file)
- **Part 4**: Practice Questions, Exam Strategy, Resources

---

## 🌐 NETWORKING SERVICES

### 4.1 Amazon VPC (Virtual Private Cloud)

**What is VPC?**

- Your own private network in AWS
- Logically isolated section of AWS Cloud
- Complete control over networking
- Default VPC created automatically

**Key Components:**

**Subnets**

- Subdivision of VPC
- Tied to specific AZ
- **Public Subnet**: Has route to Internet Gateway
- **Private Subnet**: No direct internet access
- CIDR block (e.g., 10.0.1.0/24)

**Internet Gateway (IGW)**

- Allows communication between VPC and internet
- Horizontally scaled, redundant, highly available
- One IGW per VPC
- Attached to VPC

**NAT Gateway/Instance**

- Allows private subnet instances to access internet
- Outbound only (not inbound)
- **NAT Gateway**: Managed by AWS, highly available
- **NAT Instance**: EC2 instance, you manage
- Located in public subnet

**Route Tables**

- Control traffic routing
- Each subnet associated with route table
- **Example routes**:
  - 10.0.0.0/16 → local (within VPC)
  - 0.0.0.0/0 → IGW (to internet)

**Security Groups** (Covered in Part 1)

- Virtual firewall for instances
- Stateful
- Allow rules only

**Network ACLs** (Covered in Part 1)

- Firewall for subnets
- Stateless
- Allow and deny rules

**VPC Peering**

- Connect two VPCs privately
- Same or different accounts/regions
- Non-transitive (A-B, B-C doesn't mean A-C)
- No overlapping CIDR blocks

**VPC Endpoints**

- Private connection to AWS services
- No internet gateway needed
- **Types**:
  - **Interface Endpoint**: ENI with private IP (most services)
  - **Gateway Endpoint**: Route table entry (S3, DynamoDB)
- **Use case**: Access S3 from private subnet without NAT

**AWS PrivateLink**

- Expose services to other VPCs
- Private connectivity
- No VPC peering needed

**VPN (Virtual Private Network)**

- Encrypted connection over internet
- Connect on-premises to VPC
- **Components**:
  - Virtual Private Gateway (VGW): VPC side
  - Customer Gateway: On-premises side
- **Use case**: Hybrid cloud, secure connection

**AWS Direct Connect**

- Dedicated network connection
- Bypass internet
- More reliable, consistent performance
- Lower latency than VPN
- More expensive
- **Use case**: High throughput, consistent performance

**Transit Gateway**

- Connect multiple VPCs and on-premises networks
- Hub-and-spoke model
- Simplifies network architecture
- **Use case**: Complex multi-VPC environments

### 4.2 Amazon Route 53

**What is Route 53?**

- Managed DNS service
- Domain registration
- Health checking
- Traffic routing

**Routing Policies:**

**1. Simple Routing**

- Single resource
- No health checks
- **Use case**: Single web server

**2. Weighted Routing**

- Distribute traffic by percentage
- **Example**: 70% to new version, 30% to old
- **Use case**: A/B testing, gradual migration

**3. Latency Routing**

- Route to lowest latency region
- **Use case**: Global applications

**4. Failover Routing**

- Active-passive setup
- Health checks required
- **Use case**: Disaster recovery

**5. Geolocation Routing**

- Route based on user location
- **Use case**: Content localization, compliance

**6. Geoproximity Routing**

- Route based on geographic location with bias
- **Use case**: Shift traffic between regions

**7. Multi-Value Answer Routing**

- Return multiple IP addresses
- Health checks
- **Use case**: Simple load balancing

**Features:**

- Domain registration ($12/year)
- Health checks and monitoring
- Traffic flow (visual editor)
- DNSSEC support

### 4.3 Amazon CloudFront

**What is CloudFront?**

- Content Delivery Network (CDN)
- Distribute content globally
- Cache at edge locations (400+)
- Low latency, high transfer speeds

**Key Concepts:**

**Origin**

- Source of content
- **Types**: S3, EC2, ELB, HTTP server

**Distribution**

- Configuration for content delivery
- **Types**:
  - Web Distribution: Websites, APIs
  - RTMP Distribution: Media streaming (deprecated)

**Edge Locations**

- Cache content
- More than regions + AZs
- Can write (PUT) objects

**Regional Edge Caches**

- Between origin and edge locations
- Larger cache
- Less frequently accessed content

**Features:**

- SSL/TLS support
- Custom domain names (CNAME)
- Geo-restriction
- Signed URLs/Cookies (restrict access)
- Lambda@Edge (run code at edge)
- Real-time logs

**Use Cases:**

- Static website hosting
- Video streaming
- API acceleration
- Software distribution

**CloudFront vs S3 Transfer Acceleration:**

- CloudFront: Global distribution, caching
- S3 Transfer Acceleration: Fast uploads to S3

### 4.4 AWS Global Accelerator

**What is Global Accelerator?**

- Improve application availability and performance
- Uses AWS global network
- Static IP addresses (2 Anycast IPs)
- Automatic failover

**Features:**

- Health checks
- Traffic dials (control traffic percentage)
- Endpoint weights

**Use Cases:**

- Gaming applications
- IoT
- VoIP
- Non-HTTP protocols

**Global Accelerator vs CloudFront:**

- Global Accelerator: TCP/UDP, static IPs, non-cacheable
- CloudFront: HTTP/HTTPS, caching, dynamic content

### 4.5 Amazon API Gateway

**What is API Gateway?**

- Create, publish, maintain APIs
- RESTful and WebSocket APIs
- Serverless
- Integrates with Lambda

**Features:**

- Authentication (IAM, Cognito, Lambda authorizers)
- Rate limiting (throttling)
- Caching
- API versioning
- Request/response transformation
- CORS support

**Use Cases:**

- Serverless backends
- Microservices
- Mobile/web app backends

---

## 🔧 ADDITIONAL AWS SERVICES

### 5.1 Application Integration Services

**Amazon SQS (Simple Queue Service)**

- Fully managed message queue
- Decouple applications
- **Types**:
  - **Standard Queue**: Unlimited throughput, at-least-once delivery, best-effort ordering
  - **FIFO Queue**: Exactly-once processing, ordered, 300 TPS
- **Features**:
  - Message retention: 1 min to 14 days (default 4 days)
  - Visibility timeout
  - Dead-letter queue
  - Long polling
- **Use case**: Asynchronous processing, job queues

**Amazon SNS (Simple Notification Service)**

- Pub/sub messaging
- Push notifications
- **Subscribers**: Email, SMS, HTTP, Lambda, SQS
- **Topics**: Logical access point
- **Use case**: Alerts, notifications, fan-out pattern

**Amazon EventBridge (CloudWatch Events)**

- Serverless event bus
- Connect applications using events
- **Sources**: AWS services, custom apps, SaaS
- **Targets**: Lambda, SQS, SNS, Step Functions
- **Use case**: Event-driven architectures

**AWS Step Functions**

- Orchestrate workflows
- Visual workflow designer
- Coordinate Lambda functions and services
- **Use case**: Complex workflows, ETL pipelines

**Amazon MQ**

- Managed message broker
- Supports: Apache ActiveMQ, RabbitMQ
- **Use case**: Migrate existing message brokers

### 5.2 Analytics Services

**Amazon Athena**

- Query S3 data using SQL
- Serverless
- Pay per query (data scanned)
- **Use case**: Ad-hoc queries, log analysis

**Amazon EMR (Elastic MapReduce)**

- Big data processing
- Hadoop, Spark, HBase, Presto
- Managed clusters
- **Use case**: Data processing, machine learning

**Amazon Kinesis**

- Real-time data streaming
- **Services**:
  - **Kinesis Data Streams**: Real-time data ingestion
  - **Kinesis Data Firehose**: Load data to S3, Redshift, Elasticsearch
  - **Kinesis Data Analytics**: SQL queries on streaming data
  - **Kinesis Video Streams**: Video streaming
- **Use case**: Real-time analytics, IoT

**AWS Glue**

- ETL (Extract, Transform, Load) service
- Serverless
- Data catalog
- **Use case**: Data preparation, data lakes

**Amazon QuickSight**

- Business intelligence service
- Interactive dashboards
- ML-powered insights
- **Use case**: Data visualization, reporting

**Amazon OpenSearch Service (Elasticsearch)**

- Search and analytics
- Log analytics
- Full-text search
- **Use case**: Application monitoring, security analytics

### 5.3 Machine Learning & AI Services

**Amazon SageMaker**

- Build, train, deploy ML models
- Fully managed
- Jupyter notebooks
- **Use case**: Custom ML models

**Amazon Rekognition**

- Image and video analysis
- **Features**: Face detection, object detection, text in images
- **Use case**: Content moderation, security

**Amazon Comprehend**

- Natural language processing (NLP)
- Sentiment analysis, entity recognition
- **Use case**: Customer feedback analysis

**Amazon Lex**

- Build conversational interfaces (chatbots)
- Same technology as Alexa
- **Use case**: Customer service bots

**Amazon Polly**

- Text-to-speech
- Lifelike voices
- **Use case**: Accessibility, content creation

**Amazon Transcribe**

- Speech-to-text
- Automatic speech recognition
- **Use case**: Transcription, subtitles

**Amazon Translate**

- Language translation
- Neural machine translation
- **Use case**: Localization

**Amazon Textract**

- Extract text from documents
- Forms, tables, handwriting
- **Use case**: Document processing

**Amazon Forecast**

- Time-series forecasting
- ML-based predictions
- **Use case**: Demand planning, inventory

**Amazon Personalize**

- Personalized recommendations
- Same technology as Amazon.com
- **Use case**: Product recommendations

### 5.4 Developer Tools

**AWS CodeCommit**

- Git repository hosting
- Private repositories
- **Use case**: Source control

**AWS CodeBuild**

- Build and test code
- Continuous integration
- Pay per build minute
- **Use case**: Compile code, run tests

**AWS CodeDeploy**

- Automated deployments
- EC2, Lambda, on-premises
- **Use case**: Application deployment

**AWS CodePipeline**

- Continuous delivery
- Orchestrate build, test, deploy
- **Use case**: CI/CD pipelines

**AWS CodeStar**

- Unified interface for development
- Project templates
- **Use case**: Quick project setup

**AWS Cloud9**

- Cloud-based IDE
- Code editor in browser
- **Use case**: Development environment

**AWS X-Ray**

- Distributed tracing
- Debug and analyze applications
- **Use case**: Performance optimization, troubleshooting

### 5.5 Management & Governance

**AWS CloudFormation**

- Infrastructure as Code (IaC)
- JSON or YAML templates
- Create, update, delete stacks
- **Features**:
  - Version control
  - Rollback on failure
  - Change sets (preview changes)
- **Use case**: Automate infrastructure, consistency

**AWS CloudWatch** (Covered in Part 1)

- Monitoring and observability
- Metrics, logs, alarms, dashboards

**AWS CloudTrail** (Covered in Part 1)

- API logging and auditing

**AWS Config** (Covered in Part 1)

- Resource configuration tracking

**AWS Systems Manager**

- Operational insights
- **Features**:
  - Parameter Store: Store configuration data
  - Session Manager: Secure shell access (no SSH keys)
  - Patch Manager: Automate patching
  - Run Command: Execute commands on instances
- **Use case**: Operations management

**AWS OpsWorks**

- Configuration management
- Chef and Puppet
- **Use case**: Automate server configuration

**AWS Service Catalog**

- Create and manage catalogs of IT services
- Approved products
- **Use case**: Governance, standardization

**AWS Trusted Advisor**

- Best practice recommendations
- **Categories**:
  1. Cost Optimization
  2. Performance
  3. Security
  4. Fault Tolerance
  5. Service Limits
- **Tiers**:
  - Basic/Developer: 7 core checks (free)
  - Business/Enterprise: All checks
- **Use case**: Optimize AWS environment

**AWS Personal Health Dashboard**

- Personalized view of AWS service health
- Alerts for events affecting your resources
- **Use case**: Proactive notifications

**AWS Service Health Dashboard**

- General AWS service status
- Public view
- **Use case**: Check AWS service availability

### 5.6 Migration & Transfer

**AWS Migration Hub**

- Track migrations
- Central location
- **Use case**: Migration planning

**AWS Application Discovery Service**

- Discover on-premises applications
- Plan migrations
- **Use case**: Migration assessment

**AWS Database Migration Service (DMS)**

- Migrate databases to AWS
- Homogeneous (Oracle to Oracle) or heterogeneous (Oracle to Aurora)
- Minimal downtime
- **Use case**: Database migration

**AWS Server Migration Service (SMS)**

- Migrate on-premises servers to AWS
- Incremental replication
- **Use case**: Server migration

**AWS DataSync**

- Transfer data to/from AWS
- Up to 10x faster than open-source tools
- **Use case**: Data migration, data replication

**AWS Transfer Family**

- SFTP, FTPS, FTP to S3 or EFS
- Managed file transfer
- **Use case**: File transfers

### 5.7 End User Computing

**Amazon WorkSpaces**

- Virtual desktops (DaaS)
- Windows or Linux
- Pay monthly or hourly
- **Use case**: Remote work, contractors

**Amazon AppStream 2.0**

- Application streaming
- Desktop applications in browser
- **Use case**: Software delivery

**Amazon WorkDocs**

- Document storage and collaboration
- Like Dropbox/Google Drive
- **Use case**: File sharing

**Amazon WorkLink**

- Secure mobile access to internal websites
- No VPN needed
- **Use case**: Mobile workforce

### 5.8 IoT Services

**AWS IoT Core**

- Connect IoT devices to cloud
- Device management
- **Use case**: IoT applications

**AWS IoT Greengrass**

- Run local compute on IoT devices
- Offline operation
- **Use case**: Edge computing

### 5.9 Other Important Services

**Amazon Elastic Transcoder**

- Media transcoding
- Convert video formats
- **Use case**: Video processing

**AWS Amplify**

- Build mobile and web apps
- Frontend and backend
- **Use case**: Full-stack development

**AWS Device Farm**

- Test mobile apps on real devices
- **Use case**: Mobile app testing

**AWS Backup**

- Centralized backup
- Automate backups across services
- **Use case**: Backup management

**AWS Elastic Disaster Recovery (DRS)**

- Disaster recovery
- Replicate on-premises to AWS
- **Use case**: Business continuity

---

## 💰 DOMAIN 4: BILLING, PRICING & SUPPORT (12%)

### 6.1 AWS Pricing Models

**Pay-as-you-go**

- No upfront costs
- Pay only for what you use
- Stop paying when you stop using

**Save when you reserve**

- Reserved Instances (EC2, RDS, etc.)
- Savings Plans
- Up to 75% discount

**Pay less by using more**

- Volume discounts
- Tiered pricing (S3, data transfer)

**Pay less as AWS grows**

- AWS passes savings to customers
- 75+ price reductions since launch

### 6.2 Free Tier

**Types:**

**1. Always Free**

- Never expires
- **Examples**:
  - Lambda: 1M requests/month
  - DynamoDB: 25 GB storage
  - SNS: 1M publishes
  - CloudWatch: 10 metrics

**2. 12 Months Free**

- From account creation
- **Examples**:
  - EC2: 750 hours/month (t2.micro or t3.micro)
  - S3: 5 GB storage
  - RDS: 750 hours/month (db.t2.micro)
  - CloudFront: 50 GB data transfer

**3. Trials**

- Short-term free trials
- **Examples**:
  - SageMaker: 2 months
  - Inspector: 90 days
  - Lightsail: 1 month

### 6.3 Pricing for Key Services

**EC2 Pricing Factors:**

- Instance type
- Region
- Operating system
- Pricing model (On-Demand, Reserved, Spot)
- Data transfer

**S3 Pricing Factors:**

- Storage class
- Storage amount
- Number of requests
- Data transfer out
- Management features

**RDS Pricing Factors:**

- Instance type
- Database engine
- Storage type and amount
- Backup storage
- Data transfer
- Multi-AZ deployment

**Lambda Pricing:**

- Number of requests
- Duration (GB-seconds)
- Free tier: 1M requests, 400,000 GB-seconds

**Data Transfer Pricing:**

- **Inbound**: Free (to AWS)
- **Outbound**: Charged (from AWS to internet)
- **Between regions**: Charged
- **Within region**: Free (same AZ) or small charge (different AZ)
- **CloudFront to internet**: Lower cost than direct

### 6.4 Billing & Cost Management Tools

**AWS Budgets**

- Set custom budgets
- Alerts when exceeded
- **Types**:
  - Cost budgets
  - Usage budgets
  - Reservation budgets
  - Savings Plans budgets
- **Free tier**: 2 budgets
- **Use case**: Cost control, alerts

**AWS Cost Explorer**

- Visualize and analyze costs
- Historical data (up to 12 months)
- Forecast future costs (up to 12 months)
- Filter by service, region, tag, etc.
- **Features**:
  - Cost and usage reports
  - Savings Plans recommendations
  - Reserved Instance recommendations
- **Use case**: Cost analysis, optimization

**AWS Cost and Usage Report (CUR)**

- Most detailed billing report
- Hourly, daily, or monthly
- Delivered to S3
- Integrate with Athena, QuickSight
- **Use case**: Detailed cost analysis

**AWS Price List API**

- Query AWS service prices
- Programmatic access
- **Use case**: Automation, cost estimation

**AWS Pricing Calculator**

- Estimate AWS costs
- Create cost estimates
- Share estimates
- **Use case**: Planning, budgeting

**Cost Allocation Tags**

- Organize resources
- Track costs by project, department, etc.
- **Types**:
  - AWS-generated tags
  - User-defined tags
- Must activate in Billing console
- **Use case**: Cost tracking, chargeback

**AWS Compute Optimizer**

- ML-based recommendations
- Right-size EC2, Lambda, EBS, Auto Scaling
- Reduce costs, improve performance
- **Use case**: Resource optimization

### 6.5 AWS Organizations - Billing Features

**Consolidated Billing**

- One bill for all accounts
- Combined usage for volume discounts
- **Benefits**:
  - Volume pricing tiers
  - Reserved Instance sharing
  - Savings Plans sharing
  - Free tier applies per organization (not per account)

**Example:**

- Account A: 8 TB S3 storage
- Account B: 4 TB S3 storage
- Combined: 12 TB → Lower per-GB price

### 6.6 AWS Support Plans (MEMORIZE!)

**Basic Support (Free)**

- 24/7 customer service
- Documentation, whitepapers, forums
- AWS Trusted Advisor: 7 core checks
- AWS Personal Health Dashboard
- **No technical support**

**Developer Support ($29/month or 3% of monthly usage)**

- Basic +
- Business hours email support
- 1 primary contact
- **Response times**:
  - General guidance: 24 hours
  - System impaired: 12 hours
- **Use case**: Testing, development

**Business Support ($100/month or 3-10% of monthly usage)**

- Developer +
- 24/7 phone, email, chat support
- Unlimited contacts
- Full Trusted Advisor checks
- Infrastructure Event Management (additional fee)
- **Response times**:
  - General guidance: 24 hours
  - System impaired: 12 hours
  - Production system impaired: 4 hours
  - Production system down: 1 hour
- **Use case**: Production workloads

**Enterprise On-Ramp Support ($5,500/month or 10% of monthly usage)**

- Business +
- Pool of Technical Account Managers (TAMs)
- Concierge Support Team
- Infrastructure Event Management (included)
- **Response times**:
  - Business-critical system down: 30 minutes
- **Use case**: Business-critical workloads

**Enterprise Support ($15,000/month or 3-10% of monthly usage)**

- Enterprise On-Ramp +
- Designated Technical Account Manager (TAM)
- White-glove case routing
- Management business reviews
- **Response times**:
  - Business-critical system down: 15 minutes
- **Use case**: Mission-critical workloads

**Support Plan Comparison:**
| Feature | Basic | Developer | Business | Enterprise On-Ramp | Enterprise |
|---------|-------|-----------|----------|-------------------|------------|
| Price | Free | $29+ | $100+ | $5,500+ | $15,000+ |
| Technical Support | No | Email | 24/7 Phone/Chat | 24/7 Phone/Chat | 24/7 Phone/Chat |
| Response Time (Critical) | N/A | N/A | 1 hour | 30 min | 15 min |
| TAM | No | No | No | Pool | Dedicated |
| Trusted Advisor | 7 checks | 7 checks | All checks | All checks | All checks |
| Use Case | Learning | Development | Production | Business-critical | Mission-critical |

**Key Response Times to Memorize:**

- Business (Production down): 1 hour
- Enterprise On-Ramp (Business-critical): 30 minutes
- Enterprise (Business-critical): 15 minutes

### 6.7 AWS Marketplace

**What is AWS Marketplace?**

- Digital catalog of software
- Third-party software
- AMIs, SaaS, containers
- Pay-as-you-go or annual
- Consolidated billing

**Categories:**

- Infrastructure software
- DevOps
- Business applications
- Machine learning
- IoT

**Use Cases:**

- Find and deploy software
- Try before you buy
- Simplified procurement

### 6.8 AWS Partner Network (APN)

**Consulting Partners**

- Help design, build, migrate
- Professional services
- **Tiers**: Select, Advanced, Premier

**Technology Partners**

- Software solutions on AWS
- ISVs (Independent Software Vendors)

**AWS Competency Program**

- Validated expertise
- Specific areas (e.g., Migration, Security)

### 6.9 Cost Optimization Best Practices

**1. Right-sizing**

- Match instance types to workload
- Use Compute Optimizer

**2. Reserved Capacity**

- Reserved Instances
- Savings Plans
- Up to 75% savings

**3. Spot Instances**

- Up to 90% savings
- Fault-tolerant workloads

**4. Auto Scaling**

- Scale based on demand
- Avoid over-provisioning

**5. Storage Optimization**

- Use appropriate storage class
- Lifecycle policies
- Delete unused resources

**6. Data Transfer**

- Use CloudFront
- Keep data in same region
- Use VPC endpoints

**7. Monitoring**

- CloudWatch alarms
- Cost Explorer
- Budgets

**8. Tagging**

- Track costs by project
- Identify waste

**9. Serverless**

- Lambda, Fargate
- Pay only for use

**10. Managed Services**

- Reduce operational overhead
- RDS vs EC2 database

---

## 📝 KEY EXAM TIPS - PART 3

### Must Memorize:

✅ VPC components (subnets, IGW, NAT, route tables)  
✅ VPN vs Direct Connect  
✅ Route 53 routing policies  
✅ CloudFront use cases  
✅ SQS vs SNS  
✅ AWS Support Plans (pricing, response times)  
✅ Cost management tools (Budgets, Cost Explorer)  
✅ Consolidated billing benefits  
✅ Free tier offerings  
✅ Trusted Advisor categories

### Common Exam Scenarios:

**Scenario 1**: "Connect on-premises to AWS with consistent performance?"

- **Answer**: AWS Direct Connect

**Scenario 2**: "Decouple application components?"

- **Answer**: Amazon SQS

**Scenario 3**: "Send notifications to multiple subscribers?"

- **Answer**: Amazon SNS

**Scenario 4**: "Get recommendations to reduce costs?"

- **Answer**: AWS Trusted Advisor

**Scenario 5**: "Track costs by department?"

- **Answer**: Cost Allocation Tags

**Scenario 6**: "15-minute response time for critical issues?"

- **Answer**: Enterprise Support

**Scenario 7**: "Distribute content globally with low latency?"

- **Answer**: Amazon CloudFront

**Scenario 8**: "Query S3 data using SQL?"

- **Answer**: Amazon Athena

**Scenario 9**: "Automate infrastructure deployment?"

- **Answer**: AWS CloudFormation

**Scenario 10**: "Combine usage across accounts for discounts?"

- **Answer**: AWS Organizations with Consolidated Billing

---

## 🎯 STUDY CHECKLIST - PART 3

- [ ] Understand VPC components and architecture
- [ ] Know VPN vs Direct Connect differences
- [ ] Memorized Route 53 routing policies
- [ ] Understand CloudFront and CDN concepts
- [ ] Know SQS vs SNS differences
- [ ] Can explain all AWS Support Plans
- [ ] Memorized support response times
- [ ] Understand cost management tools
- [ ] Know consolidated billing benefits
- [ ] Understand Trusted Advisor categories
- [ ] Know free tier offerings
- [ ] Understand cost optimization strategies
- [ ] Can differentiate analytics services
- [ ] Know ML/AI service purposes

---

**Continue to Part 4 for Practice Questions, Exam Strategy, and Final Resources**

**Study Time for Part 3**: 10-12 hours  
**Practice Questions**: Complete 100+ questions on networking, billing, and support
