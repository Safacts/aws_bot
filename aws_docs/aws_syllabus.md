AWS Certified Cloud Practitioner (CLF-C02) Comprehensive Study Guide

Domain 1: Cloud Concepts
The Six Advantages of Cloud Computing

Trade Capital Expense (CapEx) for Variable Expense (OpEx)
AWS allows organizations to pay only for compute resources consumed rather than investing heavily in data centers and servers before knowing how to use them. Variable expense means no upfront hardware purchases.

Benefit from Massive Economies of Scale
AWS aggregates usage from hundreds of thousands of customers, achieving higher economies of scale than any single organization could alone. AWS economies of scale translate into lower pay-as-you-go prices for customers.

Stop Guessing Capacity
AWS eliminates the need to guess infrastructure capacity requirements months in advance. AWS Auto Scaling and on-demand provisioning allow resources to scale up or down within minutes.

Increase Speed and Agility
AWS reduces the time to provision IT resources from weeks to minutes. AWS CloudFormation enables infrastructure deployment in seconds, accelerating organizational agility.

Stop Spending Money Running and Maintaining Data Centers
AWS handles undifferentiated heavy lifting of racking, stacking, and powering servers. Organizations can focus on business-differentiating projects instead of infrastructure management.

Go Global in Minutes
AWS operates Regions and Availability Zones worldwide, enabling global application deployment with low latency. AWS CloudFront and Route 53 enable global reach with minimal configuration effort.

CapEx vs. OpEx

Capital Expenditure (CapEx)
CapEx refers to upfront investments in physical infrastructure such as servers, data centers, and networking equipment. CapEx requires large initial outlays and depreciates over time.

Operational Expenditure (OpEx)
OpEx refers to paying for services or products on a consumption basis. AWS cloud computing follows the OpEx model, where customers pay only for what they use without upfront commitments.

AWS Cloud Financial Model
AWS converts fixed infrastructure costs into variable costs aligned with actual usage. AWS OpEx model reduces financial risk by eliminating capacity overprovisioning.

Types of Cloud Computing Service Models

Infrastructure as a Service (IaaS)
IaaS provides virtualized computing resources over the internet, including virtual machines, storage, and networking. Amazon EC2, Amazon VPC, and Amazon EBS are AWS IaaS offerings. Customers manage operating systems, middleware, runtime, data, and applications.

Platform as a Service (PaaS)
PaaS provides a platform allowing customers to develop, run, and manage applications without managing underlying infrastructure. AWS Elastic Beanstalk and AWS Lambda are AWS PaaS offerings. Customers focus on application code while AWS manages servers, operating systems, and runtime environments.

Software as a Service (SaaS)
SaaS delivers fully functional software applications over the internet on a subscription basis. Amazon WorkSpaces, Amazon Chime, and Amazon Connect are AWS SaaS offerings. Customers use the application without managing any infrastructure or platform components.

Cloud Deployment Models

Public Cloud (Cloud-Native)
Public cloud deployment runs entirely on AWS infrastructure, with no on-premises components. AWS public cloud provides maximum scalability, global reach, and full benefit of AWS economies of scale.

Private Cloud (On-Premises)
Private cloud deployment uses virtualization and resource management tools in a dedicated on-premises data center. AWS Outposts extends AWS infrastructure and services to on-premises environments.

Hybrid Cloud
Hybrid cloud deployment connects on-premises infrastructure with AWS cloud resources. AWS Direct Connect, AWS VPN, and AWS Storage Gateway enable hybrid architectures. Hybrid cloud is common for organizations with regulatory requirements or legacy system dependencies.

AWS Global Infrastructure

AWS Regions
AWS Regions are geographically isolated areas containing multiple Availability Zones. Each AWS Region operates independently with its own set of AWS services. Organizations select AWS Regions based on compliance, latency, service availability, and pricing requirements.

AWS Availability Zones (AZs)
AWS Availability Zones are physically separate data centers within an AWS Region, each with independent power, cooling, and networking. AWS Availability Zones connect through low-latency, high-bandwidth links. Deploying across multiple AWS Availability Zones provides fault tolerance and high availability.

AWS Edge Locations
AWS Edge Locations are data centers used by Amazon CloudFront to cache content closer to end users. AWS Edge Locations number over 400 globally, outnumbering AWS Regions and Availability Zones. AWS Edge Locations reduce latency for content delivery and DNS resolution.

AWS Local Zones
AWS Local Zones place compute, storage, and database services closer to large population centers. AWS Local Zones extend an AWS Region to additional geographic locations. AWS Local Zones support latency-sensitive applications such as real-time gaming and video streaming.

AWS Wavelength Zones
AWS Wavelength Zones embed AWS compute and storage within telecommunications providers' 5G networks. AWS Wavelength Zones enable ultra-low latency for mobile edge computing applications.

AWS Well-Architected Framework

Operational Excellence Pillar
Operational Excellence focuses on running and monitoring systems to deliver business value and continually improving processes. AWS CloudWatch, AWS Config, and AWS Systems Manager support Operational Excellence.

Security Pillar
Security Pillar focuses on protecting information, systems, and assets through risk assessment and mitigation strategies. AWS IAM, AWS KMS, and AWS Shield support the Security Pillar.

Reliability Pillar
Reliability Pillar focuses on ensuring workloads perform intended functions and recover quickly from failures. AWS Auto Scaling, Amazon Route 53 health checks, and multi-AZ deployments support the Reliability Pillar.

Performance Efficiency Pillar
Performance Efficiency focuses on using computing resources efficiently to meet system requirements. AWS Lambda, Amazon CloudFront, and Amazon ElastiCache support Performance Efficiency.

Cost Optimization Pillar
Cost Optimization focuses on avoiding unnecessary costs and maximizing value from AWS investments. AWS Cost Explorer, AWS Budgets, and AWS Reserved Instances support Cost Optimization.

Sustainability Pillar
Sustainability Pillar focuses on minimizing environmental impacts of cloud workloads. AWS graviton processors, efficient instance selection, and AWS customer carbon footprint tool support the Sustainability Pillar.

Domain 2: Security and Compliance
AWS Shared Responsibility Model

AWS Responsibility: Security OF the Cloud
AWS is responsible for protecting the infrastructure that runs all AWS services. AWS manages physical security of data centers, including access controls, surveillance, and environmental protections. AWS secures the hardware, software, networking, and facilities running AWS Cloud services. AWS manages the hypervisor layer and below for compute services.

AWS Infrastructure Responsibilities
• AWS manages physical data center security, including biometric access controls and 24/7 surveillance
• AWS maintains and patches the underlying host operating systems and virtualization software
• AWS secures networking infrastructure, including routers, switches, and load balancers
• AWS ensures physical media destruction and secure decommissioning of storage devices

Customer Responsibility: Security IN the Cloud
Customers are responsible for security configurations and management tasks within AWS services. Customer responsibilities vary depending on the AWS service used.

Customer Responsibilities for IaaS (Amazon EC2)
• Customers manage guest operating system patching and updates
• Customers configure security group firewall rules
• Customers implement IAM policies and access controls
• Customers encrypt data at rest and in transit
• Customers manage application-level security

Customer Responsibilities for Managed Services (Amazon RDS)
• Customers manage database user accounts and permissions
• Customers configure security groups for database access
• Customers enable encryption options
• AWS handles operating system patching and database engine updates

Customer Responsibilities for Serverless Services (AWS Lambda)
• Customers manage function code security
• Customers configure IAM execution roles
• Customers manage data encryption
• AWS handles all infrastructure management

AWS Identity and Access Management (IAM)

IAM Overview
AWS IAM enables secure control of access to AWS services and resources. AWS IAM is a global service, not Region-specific. AWS IAM is offered at no additional charge.

IAM Users
IAM Users represent individual people or services requiring AWS access. Each IAM User has unique credentials (username/password and access keys). IAM Users should follow the principle of least privilege, receiving only permissions necessary for their tasks.

IAM Groups
IAM Groups are collections of IAM Users sharing common permissions. IAM Groups simplify permission management by allowing policy attachment to multiple users simultaneously. IAM Users can belong to multiple IAM Groups. IAM Groups cannot contain other IAM Groups (no nesting).

IAM Roles
IAM Roles provide temporary security credentials for trusted entities. IAM Roles eliminate the need to share long-term credentials. AWS services (like Amazon EC2) assume IAM Roles to access other AWS resources. IAM Roles enable cross-account access and federation with external identity providers.

IAM Policies
IAM Policies are JSON documents defining permissions (Allow or Deny). IAM Policies specify actions, resources, and conditions. AWS Managed Policies are created and managed by AWS for common use cases. Customer Managed Policies are created by customers for specific organizational requirements. Inline Policies are embedded directly in a single IAM User, Group, or Role.

IAM Policy Structure
IAM Policies contain Version, Statement, Effect (Allow/Deny), Action, Resource, and optional Condition elements. IAM Policy evaluation follows explicit deny > explicit allow > implicit deny logic.

IAM Best Practices
• Enable AWS Multi-Factor Authentication (MFA) for the root account and IAM Users
• Create individual IAM Users instead of sharing credentials
• Use IAM Groups to assign permissions
• Grant least privilege access
• Use IAM Roles for applications running on Amazon EC2
• Rotate credentials regularly
• Use AWS IAM Access Analyzer to identify unused permissions

Root Account
AWS root account has complete, unrestricted access to all AWS resources. AWS root account should be secured with MFA and not used for daily tasks. AWS root account credentials should be stored securely and rarely accessed.

AWS Security Services

AWS WAF (Web Application Firewall)
AWS WAF protects web applications from common web exploits at Layer 7 (application layer). AWS WAF filters HTTP/HTTPS traffic based on customizable rules. AWS WAF blocks SQL injection, cross-site scripting (XSS), and other OWASP Top 10 vulnerabilities. AWS WAF integrates with Amazon CloudFront, Application Load Balancer, and Amazon API Gateway.

AWS Shield
AWS Shield provides managed DDoS (Distributed Denial of Service) protection. AWS Shield Standard is automatically enabled at no additional cost for all AWS customers. AWS Shield Advanced provides enhanced DDoS protection, 24/7 access to AWS DDoS Response Team, and cost protection for scaling.

AWS Shield Standard vs. AWS Shield Advanced
• AWS Shield Standard: Automatic protection against common network and transport layer DDoS attacks
• AWS Shield Advanced: Enhanced detection, near real-time attack visibility, 24/7 DDoS Response Team access, cost protection

Amazon GuardDuty
Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity. Amazon GuardDuty analyzes AWS CloudTrail logs, VPC Flow Logs, and DNS logs. Amazon GuardDuty uses machine learning to identify anomalies and threats.

AWS Inspector
AWS Inspector automatically assesses applications for vulnerabilities and deviations from best practices. AWS Inspector scans Amazon EC2 instances and container images for software vulnerabilities. AWS Inspector provides detailed findings with prioritized recommendations.

AWS Macie
AWS Macie uses machine learning to discover, classify, and protect sensitive data stored in Amazon S3. AWS Macie identifies personally identifiable information (PII) and intellectual property. AWS Macie generates alerts for unauthorized access or inadvertent data leaks.

AWS Key Management Service (KMS)
AWS KMS creates and manages cryptographic keys for data encryption. AWS KMS integrates with most AWS services for seamless encryption. AWS KMS provides centralized key management with full audit capabilities via AWS CloudTrail.

AWS CloudHSM
AWS CloudHSM provides dedicated Hardware Security Modules for cryptographic key storage. AWS CloudHSM offers single-tenant HSM clusters for regulatory compliance requirements. AWS CloudHSM supports asymmetric keys and custom key stores.

AWS Secrets Manager
AWS Secrets Manager stores and automatically rotates database credentials, API keys, and other secrets. AWS Secrets Manager integrates with Amazon RDS for automatic credential rotation. AWS Secrets Manager eliminates hardcoded credentials in application code.

AWS Certificate Manager (ACM)
AWS Certificate Manager provisions, manages, and deploys SSL/TLS certificates. AWS Certificate Manager provides free public certificates for AWS-integrated services. AWS Certificate Manager handles certificate renewal automatically.

Network Security

Security Groups
Security Groups act as virtual firewalls for Amazon EC2 instances at the instance level. Security Groups control inbound and outbound traffic using allow rules only (no deny rules). Security Groups are stateful—return traffic is automatically allowed. Security Groups evaluate all rules before deciding to allow traffic.

Network Access Control Lists (Network ACLs)
Network ACLs operate at the subnet level within an Amazon VPC. Network ACLs support both allow and deny rules. Network ACLs are stateless—return traffic must be explicitly allowed. Network ACLs evaluate rules in numbered order, stopping at the first match.

Security Groups vs. Network ACLs Comparison
| Feature | Security Groups | Network ACLs |
|---------|-----------------|--------------|
| Scope | Instance level | Subnet level |
| Rule Type | Allow rules only | Allow and Deny rules |
| State | Stateful | Stateless |
| Rule Evaluation | All rules evaluated | Rules evaluated in order |
| Default Behavior | Denies all inbound, allows all outbound | Allows all inbound and outbound |

AWS VPN
AWS VPN establishes encrypted connections between on-premises networks and AWS VPCs. AWS Site-to-Site VPN creates IPsec tunnels over the public internet. AWS Client VPN enables remote user access to AWS and on-premises resources.

AWS Direct Connect
AWS Direct Connect establishes dedicated private network connections from on-premises to AWS. AWS Direct Connect bypasses the public internet for consistent network performance. AWS Direct Connect supports 1 Gbps and 10 Gbps dedicated connections.

Compliance and Governance

AWS Artifact
AWS Artifact is a self-service portal for on-demand access to AWS compliance reports. AWS Artifact provides access to AWS SOC reports, PCI-DSS attestations, ISO certifications, and other compliance documents. AWS Artifact Agreements enable customers to review and accept AWS agreements such as BAA (HIPAA).

AWS Compliance Programs
AWS maintains compliance certifications including SOC 1/2/3, PCI-DSS, HIPAA, FedRAMP, GDPR, and ISO 27001. AWS Compliance Programs are validated by independent third-party auditors. Customers inherit AWS compliance controls for infrastructure-level requirements.

AWS Config
AWS Config tracks and records AWS resource configurations and changes over time. AWS Config evaluates resource configurations against desired settings using Config Rules. AWS Config provides configuration history for troubleshooting and compliance auditing.

AWS CloudTrail
AWS CloudTrail records AWS API calls and account activity across AWS infrastructure. AWS CloudTrail provides event history for governance, compliance, and operational auditing. AWS CloudTrail logs include caller identity, timestamp, source IP, and request/response details.

AWS Security Hub
AWS Security Hub provides a comprehensive view of security alerts across AWS accounts. AWS Security Hub aggregates findings from Amazon GuardDuty, AWS Inspector, and AWS Macie. AWS Security Hub automates security checks against AWS best practices and compliance standards.

AWS Trusted Advisor
AWS Trusted Advisor provides real-time guidance for optimizing AWS resources. AWS Trusted Advisor checks five categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits. AWS Trusted Advisor security checks include exposed access keys and open security groups.

Domain 3: Cloud Technology and Services
Compute Services

Amazon EC2 (Elastic Compute Cloud)
Amazon EC2 provides resizable virtual servers (instances) in the cloud. Amazon EC2 is the foundation of AWS IaaS compute offerings. Amazon EC2 provides complete control over the operating system, networking, and storage.

Amazon EC2 Instance Types

General Purpose Instances (M, T Series)
General Purpose instances provide balanced compute, memory, and networking resources. Amazon EC2 T instances offer burstable performance for variable workloads. Amazon EC2 M instances are ideal for web servers, development environments, and small databases.

Compute Optimized Instances (C Series)
Compute Optimized instances provide high-performance processors for compute-intensive tasks. Amazon EC2 C instances are ideal for batch processing, gaming servers, scientific modeling, and high-performance computing.

Memory Optimized Instances (R, X, Z Series)
Memory Optimized instances provide fast performance for workloads processing large datasets in memory. Amazon EC2 R instances are ideal for high-performance databases, distributed caches, and in-memory analytics. Amazon EC2 X instances support in-memory databases like SAP HANA.

Storage Optimized Instances (I, D, H Series)
Storage Optimized instances provide high sequential read/write access to large datasets on local storage. Amazon EC2 I instances are ideal for NoSQL databases and data warehousing. Amazon EC2 D instances are ideal for distributed file systems and data processing applications.

Accelerated Computing Instances (P, G, F Series)
Accelerated Computing instances use hardware accelerators (GPUs, FPGAs) for floating-point calculations. Amazon EC2 P instances are ideal for machine learning training and high-performance computing. Amazon EC2 G instances are ideal for graphics-intensive applications and video encoding.

Amazon EC2 Auto Scaling
Amazon EC2 Auto Scaling automatically adjusts the number of Amazon EC2 instances based on demand. Amazon EC2 Auto Scaling maintains application availability and reduces costs by scaling down during low demand. Amazon EC2 Auto Scaling uses launch templates and scaling policies to manage instance fleet size.

Elastic Load Balancing (ELB)
Elastic Load Balancing distributes incoming application traffic across multiple targets. Application Load Balancer (ALB) operates at Layer 7 (HTTP/HTTPS) with path-based and host-based routing. Network Load Balancer (NLB) operates at Layer 4 (TCP/UDP) for ultra-high performance and static IP support. Gateway Load Balancer (GWLB) operates at Layer 3 for deploying third-party virtual appliances.

AWS Lambda
AWS Lambda runs code without provisioning or managing servers. AWS Lambda executes code in response to events and automatically scales based on request volume. AWS Lambda charges only for compute time consumed, measured in milliseconds. AWS Lambda supports Python, Node.js, Java, Go, Ruby, .NET, and custom runtimes.

Amazon ECS (Elastic Container Service)
Amazon ECS is a fully managed container orchestration service supporting Docker containers. Amazon ECS integrates with AWS Fargate for serverless container deployment. Amazon ECS provides native integration with AWS services including Amazon ECR, IAM, and CloudWatch.

Amazon EKS (Elastic Kubernetes Service)
Amazon EKS is a managed Kubernetes service for running Kubernetes on AWS without installing clusters. Amazon EKS automatically manages Kubernetes control plane availability and scalability. Amazon EKS integrates with AWS services for security, networking, and observability.

AWS Fargate
AWS Fargate provides serverless compute for containers, eliminating the need to manage servers. AWS Fargate works with both Amazon ECS and Amazon EKS. AWS Fargate automatically provisions compute resources based on container resource requirements.

AWS Elastic Beanstalk
AWS Elastic Beanstalk deploys and scales web applications automatically without infrastructure management. AWS Elastic Beanstalk supports Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker. AWS Elastic Beanstalk handles capacity provisioning, load balancing, auto-scaling, and application health monitoring.

Amazon Lightsail
Amazon Lightsail provides simple virtual private servers with predictable pricing. Amazon Lightsail is ideal for simple web applications, blogs, and development environments. Amazon Lightsail bundles compute, storage, and networking at a fixed monthly price.

AWS Batch
AWS Batch enables batch computing workloads to run on AWS at any scale. AWS Batch dynamically provisions the optimal quantity and type of compute resources. AWS Batch is ideal for financial modeling, drug discovery simulations, and rendering.

AWS Outposts
AWS Outposts extends AWS infrastructure and services to on-premises data centers. AWS Outposts provides the same APIs, tools, and hardware as AWS Regions. AWS Outposts supports hybrid architectures with consistent operations across on-premises and cloud environments.

Storage Services

Amazon S3 (Simple Storage Service)
Amazon S3 provides object storage with industry-leading scalability, availability, and durability. Amazon S3 stores data as objects within buckets. Amazon S3 delivers 99.999999999% (11 nines) durability across multiple Availability Zones.

Amazon S3 Storage Classes

S3 Standard
S3 Standard is designed for frequently accessed data with low latency and high throughput. S3 Standard stores data across a minimum of three Availability Zones. S3 Standard is ideal for dynamic websites, content distribution, and big data analytics.

S3 Intelligent-Tiering
S3 Intelligent-Tiering automatically moves data between access tiers based on changing access patterns. S3 Intelligent-Tiering has no retrieval fees and minimal monitoring charges. S3 Intelligent-Tiering is ideal for data with unknown or changing access patterns.

S3 Standard-Infrequent Access (S3 Standard-IA)
S3 Standard-IA is designed for data accessed less frequently but requiring rapid access when needed. S3 Standard-IA offers lower storage cost than S3 Standard with per-GB retrieval fees. S3 Standard-IA is ideal for backups, disaster recovery files, and long-term storage.

S3 One Zone-Infrequent Access (S3 One Zone-IA)
S3 One Zone-IA stores data in a single Availability Zone at 20% lower cost than S3 Standard-IA. S3 One Zone-IA is ideal for secondary backups or easily reproducible data. S3 One Zone-IA does not provide the same resilience as multi-AZ storage classes.

S3 Glacier Instant Retrieval
S3 Glacier Instant Retrieval provides lowest-cost storage for rarely accessed data requiring millisecond retrieval. S3 Glacier Instant Retrieval is ideal for medical images, news media archives, and user-generated content.

S3 Glacier Flexible Retrieval
S3 Glacier Flexible Retrieval provides low-cost archive storage with retrieval times from minutes to hours. S3 Glacier Flexible Retrieval supports three retrieval options: Expedited (1-5 minutes), Standard (3-5 hours), and Bulk (5-12 hours). S3 Glacier Flexible Retrieval is ideal for backup and disaster recovery.

S3 Glacier Deep Archive
S3 Glacier Deep Archive provides the lowest-cost storage for data accessed once or twice per year. S3 Glacier Deep Archive retrieval time is within 12 hours (Standard) or 48 hours (Bulk). S3 Glacier Deep Archive is ideal for long-term compliance archives and magnetic tape replacement.

Amazon S3 Features
• S3 Versioning maintains multiple versions of objects for data protection
• S3 Lifecycle Policies automatically transition objects between storage classes
• S3 Transfer Acceleration uses CloudFront edge locations for fast data uploads
• S3 Replication copies objects across S3 buckets in different Regions (Cross-Region Replication)

Amazon EBS (Elastic Block Store)
Amazon EBS provides persistent block storage volumes for Amazon EC2 instances. Amazon EBS volumes persist independently from the running instance. Amazon EBS volumes are automatically replicated within their Availability Zone.

Amazon EBS Volume Types
• General Purpose SSD (gp2/gp3): Balanced price and performance for most workloads
• Provisioned IOPS SSD (io1/io2): High-performance for latency-sensitive transactional workloads
• Throughput Optimized HDD (st1): Low-cost HDD for frequently accessed, throughput-intensive workloads
• Cold HDD (sc1): Lowest-cost HDD for less frequently accessed workloads

Amazon EBS Snapshots
Amazon EBS Snapshots are point-in-time backups of Amazon EBS volumes stored in Amazon S3. Amazon EBS Snapshots are incremental, storing only changed blocks since the last snapshot. Amazon EBS Snapshots can be copied across Regions for disaster recovery.

Amazon EFS (Elastic File System)
Amazon EFS provides scalable, elastic file storage for Linux-based workloads. Amazon EFS automatically grows and shrinks as files are added and removed. Amazon EFS supports thousands of concurrent Amazon EC2 connections across multiple Availability Zones.

Amazon FSx
Amazon FSx provides fully managed third-party file systems. Amazon FSx for Windows File Server supports Windows-native file system features and SMB protocol. Amazon FSx for Lustre provides high-performance file storage for compute-intensive workloads.

AWS Storage Gateway
AWS Storage Gateway connects on-premises environments with AWS cloud storage. AWS Storage Gateway File Gateway presents S3 objects as files via NFS/SMB. AWS Storage Gateway Volume Gateway provides iSCSI block storage backed by Amazon S3. AWS Storage Gateway Tape Gateway provides virtual tape library backed by Amazon S3 and Glacier.

AWS Snow Family

AWS Snowcone
AWS Snowcone is the smallest AWS Snow device with 8 TB of usable storage. AWS Snowcone is portable and ruggedized for edge computing and data transfer in disconnected environments.

AWS Snowball
AWS Snowball provides petabyte-scale data transport with 80 TB or 210 TB storage options. AWS Snowball Edge Compute Optimized includes EC2 compute capabilities for local processing. AWS Snowball accelerates large data migrations that would take weeks or months over network.

AWS Snowmobile
AWS Snowmobile is an exabyte-scale data transfer service using a 45-foot shipping container. AWS Snowmobile transfers up to 100 PB per Snowmobile. AWS Snowmobile is ideal for data center shutdowns and massive data migrations.

Database Services

Amazon RDS (Relational Database Service)
Amazon RDS is a managed relational database service supporting multiple database engines. Amazon RDS automates database administration tasks including patching, backups, and recovery. Amazon RDS supports MySQL, PostgreSQL, MariaDB, Oracle, Microsoft SQL Server, and Amazon Aurora.

Amazon RDS Features
• Multi-AZ deployment provides high availability with automatic failover
• Read Replicas improve read performance and enable geographic distribution
• Automated backups with point-in-time recovery up to 35 days
• Amazon RDS handles database patching with minimal downtime

Amazon Aurora
Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud. Amazon Aurora provides up to 5x performance of standard MySQL and 3x performance of standard PostgreSQL. Amazon Aurora automatically scales storage up to 128 TB. Amazon Aurora Serverless automatically adjusts capacity based on application demand.

Amazon DynamoDB
Amazon DynamoDB is a fully managed NoSQL key-value and document database. Amazon DynamoDB delivers single-digit millisecond performance at any scale. Amazon DynamoDB automatically scales throughput capacity and replicates data across multiple Availability Zones. Amazon DynamoDB Global Tables enable multi-Region, active-active replication.

Amazon ElastiCache
Amazon ElastiCache provides fully managed in-memory caching using Redis or Memcached. Amazon ElastiCache improves application performance by caching frequently accessed data. Amazon ElastiCache reduces database load and decreases latency for read-heavy workloads.

Amazon Redshift
Amazon Redshift is a fully managed petabyte-scale data warehouse for analytics. Amazon Redshift uses columnar storage and parallel query execution for fast complex queries. Amazon Redshift Serverless automatically provisions and scales data warehouse capacity. Amazon Redshift Spectrum enables querying data directly in Amazon S3.

Amazon Neptune
Amazon Neptune is a fully managed graph database for applications with highly connected data. Amazon Neptune supports graph query languages Apache TinkerPop Gremlin and W3C SPARQL. Amazon Neptune is ideal for social networking, recommendation engines, and fraud detection.

Amazon DocumentDB
Amazon DocumentDB is a MongoDB-compatible document database with scalability and durability. Amazon DocumentDB is ideal for content management, catalogs, and user profiles.

Amazon Keyspaces
Amazon Keyspaces is a scalable, managed Apache Cassandra-compatible database service. Amazon Keyspaces is ideal for high-volume applications requiring single-digit-millisecond latency.

Amazon QLDB (Quantum Ledger Database)
Amazon QLDB provides an immutable, cryptographically verifiable transaction log. Amazon QLDB is ideal for systems of record, supply chain, and regulatory compliance.

Amazon Timestream
Amazon Timestream is a fast, scalable time-series database for IoT and operational applications. Amazon Timestream automatically scales and manages data lifecycle.

AWS Database Migration Service (DMS)
AWS DMS migrates databases to AWS with minimal downtime. AWS DMS supports homogeneous migrations (Oracle to Oracle) and heterogeneous migrations (Oracle to Aurora). AWS DMS keeps source database operational during migration.

Networking Services

Amazon VPC (Virtual Private Cloud)
Amazon VPC enables launching AWS resources in a logically isolated virtual network. Amazon VPC provides complete control over IP address ranges, subnets, routing, and security. Amazon VPC supports both IPv4 and IPv6 addressing.

Amazon VPC Components

Subnets
Subnets are segments of Amazon VPC IP address ranges where AWS resources are placed. Public subnets have routes to an Internet Gateway for internet access. Private subnets do not have direct internet access and require NAT Gateway for outbound connectivity.

Internet Gateway
Internet Gateway enables communication between Amazon VPC resources and the internet. Internet Gateway supports both inbound and outbound internet traffic. Only one Internet Gateway can attach to an Amazon VPC.

NAT Gateway
NAT Gateway enables instances in private subnets to connect to the internet while preventing inbound connections. NAT Gateway is a managed service with automatic scaling and high availability. NAT Gateway is placed in a public subnet and referenced in private subnet route tables.

Route Tables
Route Tables contain rules determining where network traffic is directed. Each subnet associates with one Route Table. Route Tables can include routes to Internet Gateways, NAT Gateways, VPC Peering connections, and VPN connections.

VPC Peering
VPC Peering enables private connectivity between two Amazon VPCs using private IP addresses. VPC Peering supports connections between VPCs in the same or different AWS accounts and Regions. VPC Peering connections are not transitive (A-B and B-C does not connect A-C).

VPC Endpoints
VPC Endpoints enable private connections to AWS services without traversing the internet. Interface Endpoints use AWS PrivateLink to access services through private IP addresses. Gateway Endpoints provide access to Amazon S3 and Amazon DynamoDB via route table entries.

AWS Transit Gateway
AWS Transit Gateway connects Amazon VPCs and on-premises networks through a central hub. AWS Transit Gateway simplifies network architecture by eliminating complex VPC Peering meshes. AWS Transit Gateway supports thousands of VPC connections per gateway.

Amazon Route 53
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. Amazon Route 53 routes end users to applications by translating domain names to IP addresses. Amazon Route 53 provides domain registration, DNS routing, and health checking.

Amazon Route 53 Routing Policies
• Simple Routing: Returns a single resource for a domain
• Weighted Routing: Distributes traffic based on assigned weights
• Latency-based Routing: Routes to the Region with lowest latency
• Failover Routing: Routes to standby resource when primary fails health checks
• Geolocation Routing: Routes based on user geographic location
• Geoproximity Routing: Routes based on resource location and optional bias
• Multivalue Answer Routing: Returns multiple healthy resources randomly

Amazon CloudFront
Amazon CloudFront is a content delivery network (CDN) that accelerates delivery of websites, APIs, and content. Amazon CloudFront caches content at Edge Locations worldwide for low-latency access. Amazon CloudFront integrates with AWS Shield for DDoS protection and AWS WAF for application security.

AWS Global Accelerator
AWS Global Accelerator improves global application availability and performance using AWS global network. AWS Global Accelerator provides static IP addresses that route to optimal endpoints. AWS Global Accelerator reduces latency by routing traffic through AWS backbone network.

Amazon API Gateway
Amazon API Gateway enables creating, publishing, and managing REST, HTTP, and WebSocket APIs. Amazon API Gateway handles API traffic management, authorization, and monitoring. Amazon API Gateway integrates with AWS Lambda for serverless API backends.

Application Integration Services

Amazon SQS (Simple Queue Service)
Amazon SQS is a fully managed message queuing service for decoupling distributed systems. Amazon SQS Standard queues provide maximum throughput with best-effort ordering. Amazon SQS FIFO queues guarantee exactly-once processing and strict message ordering.

Amazon SNS (Simple Notification Service)
Amazon SNS is a fully managed publish/subscribe messaging service. Amazon SNS sends messages to subscribers including Amazon SQS, AWS Lambda, HTTP endpoints, and email. Amazon SNS enables fan-out messaging patterns to multiple subscribers.

Amazon EventBridge
Amazon EventBridge is a serverless event bus connecting applications using events. Amazon EventBridge routes events from AWS services, SaaS applications, and custom sources. Amazon EventBridge enables event-driven architectures with filtering and transformation.

AWS Step Functions
AWS Step Functions orchestrates serverless workflows using visual state machines. AWS Step Functions coordinates AWS Lambda functions and other AWS services. AWS Step Functions provides built-in error handling and retry logic.

Management and Monitoring Services

Amazon CloudWatch
Amazon CloudWatch monitors AWS resources and applications in real time. Amazon CloudWatch collects metrics, logs, and events from AWS services. Amazon CloudWatch Alarms trigger automated actions based on metric thresholds.

AWS CloudFormation
AWS CloudFormation provisions and manages AWS infrastructure using code templates. AWS CloudFormation templates use YAML or JSON to define AWS resources. AWS CloudFormation enables infrastructure as code, version control, and repeatable deployments.

AWS Systems Manager
AWS Systems Manager provides operational visibility and control of AWS infrastructure. AWS Systems Manager Session Manager enables secure shell access without SSH keys or bastion hosts. AWS Systems Manager Patch Manager automates operating system and software patching.

AWS CloudTrail
AWS CloudTrail logs, monitors, and retains account activity across AWS infrastructure. AWS CloudTrail records API calls for auditing, compliance, and operational troubleshooting. AWS CloudTrail creates event history for the past 90 days by default.

AWS X-Ray
AWS X-Ray analyzes and debugs distributed applications with end-to-end tracing. AWS X-Ray visualizes request paths and identifies performance bottlenecks. AWS X-Ray integrates with Amazon EC2, AWS Lambda, and container services.

AWS Health Dashboard
AWS Health Dashboard displays AWS service health and personal account events. AWS Personal Health Dashboard provides proactive notifications about AWS events affecting your resources. AWS Service Health Dashboard shows current status of all AWS services across Regions.

Machine Learning and AI Services

Amazon SageMaker
Amazon SageMaker is a fully managed service for building, training, and deploying machine learning models. Amazon SageMaker provides built-in algorithms and Jupyter notebooks for development.

Amazon Rekognition
Amazon Rekognition adds image and video analysis to applications. Amazon Rekognition identifies objects, people, text, and activities in images and videos.

Amazon Comprehend
Amazon Comprehend uses natural language processing to extract insights from text. Amazon Comprehend identifies sentiment, entities, key phrases, and language.

Amazon Lex
Amazon Lex builds conversational interfaces using voice and text. Amazon Lex powers Amazon Alexa and provides automatic speech recognition.

Amazon Polly
Amazon Polly converts text into lifelike speech. Amazon Polly supports multiple languages and voices.

Amazon Transcribe
Amazon Transcribe converts speech to text automatically. Amazon Transcribe supports real-time and batch transcription.

Amazon Translate
Amazon Translate provides neural machine translation between languages. Amazon Translate supports real-time and batch translation.

Amazon Textract
Amazon Textract extracts text and data from scanned documents. Amazon Textract identifies forms, tables, and handwritten text.

Amazon Kendra
Amazon Kendra provides intelligent enterprise search using machine learning. Amazon Kendra delivers accurate answers from unstructured data sources.

Developer Tools

AWS CodeCommit
AWS CodeCommit is a managed source control service hosting Git repositories. AWS CodeCommit provides secure, scalable repository hosting.

AWS CodeBuild
AWS CodeBuild is a fully managed build service compiling source code and running tests. AWS CodeBuild scales automatically and charges only for build time used.

AWS CodeDeploy
AWS CodeDeploy automates code deployments to Amazon EC2, AWS Lambda, and on-premises servers. AWS CodeDeploy supports rolling, blue/green, and canary deployment strategies.

AWS CodePipeline
AWS CodePipeline is a continuous integration and continuous delivery (CI/CD) service. AWS CodePipeline automates build, test, and deploy phases of release processes.

AWS Cloud9
AWS Cloud9 is a cloud-based integrated development environment (IDE). AWS Cloud9 enables code writing, running, and debugging directly from a browser.

Domain 4: Billing, Pricing, and Support
AWS Pricing Models

AWS Free Tier
AWS Free Tier provides limited free usage of AWS services for new accounts for 12 months. AWS Free Tier includes 750 hours per month of Amazon EC2 t2.micro or t3.micro. AWS Free Tier includes 5 GB of Amazon S3 Standard storage. Some AWS services offer Always Free tiers beyond the 12-month period.

Amazon EC2 Pricing Models

On-Demand Instances
On-Demand Instances charge by the second (minimum 60 seconds) with no upfront commitment. On-Demand pricing is ideal for unpredictable workloads, short-term applications, and testing. On-Demand Instances provide the highest flexibility but highest cost per compute hour.

Reserved Instances
Reserved Instances provide up to 72% discount compared to On-Demand pricing. Reserved Instances require a 1-year or 3-year commitment. Standard Reserved Instances provide the largest discount but cannot change instance family. Convertible Reserved Instances provide smaller discount but allow changing instance type, operating system, and tenancy.

Reserved Instance Payment Options
• All Upfront: Largest discount, pay entire term upfront
• Partial Upfront: Middle discount, pay part upfront and remainder monthly
• No Upfront: Smallest discount, pay monthly with no upfront payment

Savings Plans
Savings Plans provide up to 72% discount in exchange for consistent usage commitment ($/hour) for 1 or 3 years. Compute Savings Plans apply to any EC2 instance regardless of Region, instance family, or size. EC2 Instance Savings Plans provide larger discounts but apply to specific instance families in specific Regions.

Spot Instances
Spot Instances provide up to 90% discount compared to On-Demand pricing. Spot Instances use spare Amazon EC2 capacity with variable pricing based on supply and demand. Spot Instances can be interrupted with 2-minute notification when AWS needs capacity. Spot Instances are ideal for fault-tolerant, flexible applications such as batch processing, data analysis, and containerized workloads.

Dedicated Hosts
Dedicated Hosts provide physical servers dedicated to a single customer account. Dedicated Hosts enable using existing server-bound software licenses. Dedicated Hosts meet compliance requirements requiring single-tenant infrastructure.

Dedicated Instances
Dedicated Instances run on hardware dedicated to a single customer but do not provide socket/core visibility. Dedicated Instances provide hardware isolation without Dedicated Host licensing benefits.

AWS Pricing Calculators and Tools

AWS Pricing Calculator
AWS Pricing Calculator estimates monthly AWS costs for specific architectures. AWS Pricing Calculator enables modeling solutions before building and exploring price points.

AWS Cost Explorer
AWS Cost Explorer visualizes and analyzes AWS costs and usage over time. AWS Cost Explorer provides 12 months of historical data and 12 months of forecast. AWS Cost Explorer identifies cost trends, anomalies, and optimization opportunities.

AWS Budgets
AWS Budgets sets custom cost and usage budgets with alerts when thresholds are exceeded. AWS Budgets supports cost budgets, usage budgets, reservation utilization, and coverage budgets. AWS Budgets can trigger automated actions such as stopping EC2 instances when budgets are exceeded.

AWS Cost and Usage Reports
AWS Cost and Usage Reports provide the most detailed billing data available. AWS Cost and Usage Reports include line items for every service, operation, and resource. AWS Cost and Usage Reports can be delivered to Amazon S3 for analysis.

AWS Cost Allocation Tags
AWS Cost Allocation Tags enable tracking AWS costs by project, department, or custom categories. AWS-generated tags identify resources automatically. User-defined tags require customer activation in the billing console.

AWS Organizations

AWS Organizations Overview
AWS Organizations centrally manages multiple AWS accounts under a single organization. AWS Organizations enables consolidated billing, combining usage across accounts for volume discounts. AWS Organizations provides hierarchical grouping using Organizational Units (OUs).

Service Control Policies (SCPs)
Service Control Policies define maximum available permissions for member accounts. SCPs do not grant permissions but restrict what IAM policies can allow. SCPs apply to the root account of member accounts (but not the management account).

Consolidated Billing Benefits
• Single payment method for all member accounts
• Combined usage for volume pricing discounts
• Free feature included with AWS Organizations
• Shared Reserved Instances and Savings Plans across accounts

AWS Support Plans

Basic Support Plan
Basic Support is included free with all AWS accounts. Basic Support provides 24/7 access to customer service, documentation, and forums. Basic Support includes access to 7 core AWS Trusted Advisor checks. Basic Support provides access to AWS Personal Health Dashboard.

Developer Support Plan
Developer Support costs $29/month or 3% of monthly AWS charges (greater of the two). Developer Support provides business-hours email access to Cloud Support Associates. Developer Support offers general guidance within 24 hours and system impaired response within 12 hours. Developer Support is recommended for testing and development environments.

Business Support Plan
Business Support costs $100/month or 3-10% of monthly AWS charges (tiered percentage). Business Support provides 24/7 phone, email, and chat access to Cloud Support Engineers. Business Support offers production system impaired response within 4 hours and production system down response within 1 hour. Business Support includes full access to all AWS Trusted Advisor checks. Business Support provides access to Infrastructure Event Management for additional fee.

Enterprise On-Ramp Support Plan
Enterprise On-Ramp costs $5,500/month or tiered percentage of monthly AWS charges. Enterprise On-Ramp provides 30-minute response time for business-critical system down events. Enterprise On-Ramp includes pool of Technical Account Managers (TAMs). Enterprise On-Ramp provides Concierge Support Team for billing and account questions.

Enterprise Support Plan
Enterprise Support costs $15,000/month or tiered percentage of monthly AWS charges. Enterprise Support provides 15-minute response time for business-critical system down events. Enterprise Support includes a designated Technical Account Manager (TAM). Enterprise Support provides Infrastructure Event Management included at no additional cost. Enterprise Support includes access to online self-paced labs and AWS Incident Detection and Response.

Support Plan Comparison

| Feature | Basic | Developer | Business | Enterprise On-Ramp | Enterprise |
|---------|-------|-----------|----------|-------------------|------------|
| Price | Free | $29/mo+ | $100/mo+ | $5,500/mo+ | $15,000/mo+ |
| Trusted Advisor | 7 Core Checks | 7 Core Checks | Full Access | Full Access | Full Access |
| 24/7 Support | No | No | Yes | Yes | Yes |
| Critical Response | N/A | N/A | 1 hour | 30 minutes | 15 minutes |
| TAM | No | No | No | Pool of TAMs | Designated TAM |

Additional Billing Concepts

Pay-As-You-Go
AWS charges only for resources consumed with no minimum commitments. Pay-as-you-go pricing eliminates upfront capital expenditure requirements.

Pay Less When You Reserve
AWS provides significant discounts for capacity reservations through Reserved Instances and Savings Plans. Reservation discounts increase with longer commitment terms.

Pay Less As AWS Grows
AWS passes savings from economies of scale to customers through price reductions. AWS has reduced prices over 100 times since launching in 2006.

AWS Compute Optimizer
AWS Compute Optimizer analyzes resource utilization and recommends optimal AWS resources. AWS Compute Optimizer reduces costs by identifying over-provisioned instances.

AWS Marketplace
AWS Marketplace is a digital catalog of third-party software solutions that run on AWS. AWS Marketplace offers software with flexible pricing models including hourly, monthly, annual, and BYOL.

Technical Account Manager (TAM)

TAM Overview
TAM provides proactive guidance and advocacy for Enterprise and Enterprise On-Ramp customers. TAM conducts Well-Architected reviews and operational reviews. TAM assists with architectural guidance and service optimization. TAM is the primary point of contact for technical account needs.

AWS Concierge Support Team

Concierge Overview
AWS Concierge Support Team assists with billing and account-level inquiries. Concierge is available to Enterprise On-Ramp and Enterprise Support customers. Concierge handles non-technical questions about accounts, billing, and AWS Organizations.