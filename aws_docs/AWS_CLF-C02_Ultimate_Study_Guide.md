# AWS Certified Cloud Practitioner (CLF-C02) — Ultimate RAG Study Guide

---

## Domain 1: Cloud Concepts

---

### The 6 Advantages of Cloud Computing

**Advantage 1: Trade Capital Expense (CapEx) for Variable Expense (OpEx)**
Capital Expense (CapEx) refers to upfront investments in physical infrastructure such as servers, data centers, and networking hardware. Operational Expense (OpEx) refers to paying only for the resources consumed, billed as ongoing operating costs. AWS Cloud eliminates the need to invest in data centers before knowing how they will be used. AWS customers pay only for what they consume, with no long-term financial commitments required.

**Advantage 2: Benefit from Massive Economies of Scale**
AWS aggregates usage from hundreds of thousands of customers, allowing AWS to achieve higher economies of scale than any individual business. AWS passes these savings to customers in the form of lower pay-as-you-go prices. AWS continuously lowers prices as a result of these economies of scale. Individual AWS customers benefit from pricing they could never achieve by operating their own infrastructure.

**Advantage 3: Stop Guessing Capacity**
On-premises infrastructure requires businesses to predict capacity needs months or years in advance, resulting in either idle resources or insufficient capacity. AWS Cloud allows resources to be scaled up or down in minutes based on actual demand. Amazon EC2 Auto Scaling can automatically adjust compute capacity to match fluctuating workloads. AWS eliminates the risk of purchasing too much or too little capacity.

**Advantage 4: Increase Speed and Agility**
In a cloud environment, new IT resources are only a click away, reducing the time to make resources available to developers from weeks to minutes. AWS dramatically increases organizational agility by making it faster to experiment and develop. The cost and time required to experiment is significantly reduced in the AWS Cloud. Development teams can provision and decommission AWS resources rapidly without waiting for hardware procurement.

**Advantage 5: Stop Spending Money Running and Maintaining Data Centers**
AWS allows businesses to focus on projects that differentiate their business rather than managing infrastructure. AWS handles the undifferentiated heavy lifting of racking, stacking, and powering physical servers. Businesses can redirect resources previously spent on data center operations toward customer-facing innovation. AWS data center management, including physical security and hardware maintenance, is handled entirely by AWS.

**Advantage 6: Go Global in Minutes**
AWS operates a global infrastructure spanning multiple geographic Regions around the world. AWS customers can deploy applications in multiple AWS Regions with just a few clicks. Deploying globally with AWS allows businesses to provide lower latency and a better experience for customers at minimal cost. AWS Global Infrastructure enables businesses to reach global markets far faster than traditional infrastructure procurement allows.

---

### CapEx vs. OpEx in Cloud Computing

**Capital Expenditure (CapEx)**
CapEx involves paying upfront for physical infrastructure such as servers, networking equipment, and data center facilities. CapEx assets are depreciated over time and represent a fixed, sunk cost regardless of actual utilization. Businesses that own on-premises infrastructure must maintain and refresh hardware on a multi-year cycle. CapEx models require capacity planning years in advance, risking over-provisioning or under-provisioning.

**Operational Expenditure (OpEx)**
OpEx involves paying for services or products as needed, treating cloud costs as a recurring operational expense. AWS billing is consumption-based, meaning AWS customers only pay for compute, storage, and data transfer they actually use. OpEx costs are variable and can scale up or down in direct proportion to business activity. AWS Cloud converts the traditional CapEx model of IT spending entirely into an OpEx model.

---

### Types of Cloud Computing

#### Infrastructure as a Service (IaaS)

IaaS provides virtualized computing resources over the internet, including compute, storage, and networking. AWS customers who use IaaS are responsible for managing the operating system, middleware, runtime, data, and applications. Amazon EC2 (Elastic Compute Cloud) is the primary AWS IaaS offering, providing resizable virtual servers in the AWS Cloud. IaaS gives AWS customers the highest level of flexibility and control over their IT resources.

#### Platform as a Service (PaaS)

PaaS removes the need for organizations to manage the underlying infrastructure, allowing customers to focus on application deployment and management. AWS Elastic Beanstalk is an AWS PaaS service that automatically handles the deployment, scaling, load balancing, and monitoring of applications. AWS customers using PaaS are responsible only for the application code and data, while AWS manages the runtime, middleware, OS, and infrastructure. PaaS accelerates development by abstracting infrastructure management from developers.

#### Software as a Service (SaaS)

SaaS provides a complete product that is run and managed by the service provider, accessible via a web browser or API. AWS customers using SaaS are responsible only for their own data and user access configuration. Amazon WorkMail is an example of an AWS-adjacent SaaS offering providing managed business email and calendaring. SaaS eliminates all infrastructure, platform, and application management responsibilities from the end user.

---

### Cloud Deployment Models

#### Public Cloud

The public cloud deployment model refers to running workloads entirely on AWS-managed infrastructure accessible over the public internet. AWS owns and operates all physical data centers, networking, and hypervisors in the public cloud model. Public cloud on AWS is ideal for variable workloads, startups, and organizations seeking to eliminate all capital infrastructure spending. All AWS commercial services operate within the public cloud deployment model.

#### Private Cloud (On-Premises)

A private cloud deployment model involves running cloud-like infrastructure within a company's own data center. AWS Outposts is an AWS service that extends AWS infrastructure, services, APIs, and tools to on-premises facilities to support private cloud deployments. Private cloud is used for workloads that require strict data residency, regulatory compliance, or very low latency to on-premises systems. AWS Outposts enables consistent AWS APIs and services in private cloud environments.

#### Hybrid Cloud

A hybrid cloud deployment model connects on-premises infrastructure or private cloud environments with public cloud resources. AWS Direct Connect provides a dedicated private network connection from an on-premises data center to AWS, supporting hybrid architectures. AWS VPN (Virtual Private Network) allows encrypted connectivity between on-premises environments and AWS VPCs (Virtual Private Clouds) over the public internet. Hybrid cloud is used for workloads requiring gradual migration, data sovereignty compliance, or integration with legacy on-premises systems.

#### Multi-Cloud

A multi-cloud deployment model uses services from two or more cloud providers simultaneously. AWS supports multi-cloud strategies through open standards, Kubernetes compatibility via Amazon EKS (Elastic Kubernetes Service), and AWS-native management tools. Multi-cloud reduces vendor lock-in and allows organizations to use best-of-breed services from different providers. AWS services such as AWS Control Tower and AWS Organizations can manage governance even in complex multi-cloud environments.

---

## Domain 2: Security and Compliance

---

### The AWS Shared Responsibility Model

The AWS Shared Responsibility Model divides security and compliance obligations between AWS and the customer. AWS is responsible for security **of** the cloud; the customer is responsible for security **in** the cloud. The boundary of responsibility shifts depending on the service model being used (IaaS, PaaS, SaaS). Understanding the Shared Responsibility Model is critical for correctly architecting secure AWS workloads.

#### AWS Responsibilities ("Security of the Cloud")

AWS is responsible for protecting the infrastructure that runs all AWS Cloud services, including physical hardware, software, networking, and facilities. AWS manages and controls the host operating system, the virtualization layer, and the physical security of the data centers where AWS services operate. AWS is responsible for the security of managed services such as Amazon S3, Amazon RDS, and AWS Lambda at the infrastructure level. AWS compliance with global security standards (ISO 27001, SOC 1/2/3, PCI DSS) is an AWS responsibility covered by AWS Artifact.

Specific AWS responsibilities include:
- Physical security of AWS data centers (access control, surveillance, environmental controls)
- Hardware and firmware management for AWS servers and networking equipment
- Software patches and security updates for the AWS hypervisor and managed service infrastructure
- Global network infrastructure, including AWS backbone and edge locations
- Virtualization infrastructure security for Amazon EC2 hosts

#### Customer Responsibilities ("Security in the Cloud")

AWS customers are responsible for configuring and securing everything they deploy on top of the AWS infrastructure. For Amazon EC2 instances, customers are responsible for the guest operating system (including updates and security patches), application software, and data. Customers are responsible for configuring AWS security services such as AWS Security Groups, Network ACLs, and AWS WAF rules. Customer responsibilities include Identity and Access Management (IAM) policy configuration, data encryption choices, and network traffic protection.

Specific customer responsibilities include:
- AWS IAM user, group, role, and policy management
- Guest OS patching and hardening on Amazon EC2 instances
- Application-level security for customer-deployed code
- Data classification, data encryption at rest and in transit
- Amazon S3 bucket policy and access control configuration
- Amazon VPC security group and Network ACL configuration
- Multi-Factor Authentication (MFA) enforcement on AWS accounts

#### Shared Responsibilities

Patch management is a shared responsibility: AWS patches the infrastructure for managed services, while customers patch guest operating systems and applications on Amazon EC2. Configuration management is shared: AWS configures and secures the infrastructure, while customers configure their own AWS resources. Awareness and training is shared: AWS trains its employees, and customers are responsible for training their own employees in secure AWS usage.

---

### AWS Identity and Access Management (IAM)

**Amazon IAM (Identity and Access Management)** is an AWS service that controls who is authenticated and authorized to use AWS resources. IAM is a global AWS service, meaning IAM Users, Groups, Roles, and Policies apply across all AWS Regions. IAM follows the principle of least privilege: granting only the minimum permissions required to perform a task. IAM is available at no additional charge; customers pay only for the AWS resources accessed via IAM-managed identities.

#### IAM Users

An IAM User is an entity created in AWS that represents a person or application that interacts with AWS services and resources. IAM Users are assigned long-term credentials: a username and password for AWS Management Console access, and/or Access Keys for programmatic AWS API access. Each IAM User has no permissions by default; permissions must be explicitly granted via IAM Policies. Best practice requires enabling MFA (Multi-Factor Authentication) for all IAM Users, especially the AWS Root User.

#### IAM Groups

An IAM Group is a collection of IAM Users that share the same set of IAM permissions. IAM Groups simplify permission management by allowing administrators to assign policies to a group rather than to individual IAM Users. IAM Users can belong to multiple IAM Groups simultaneously. IAM Groups cannot be nested — an IAM Group cannot contain another IAM Group.

#### IAM Roles

An IAM Role is an IAM identity with specific permissions that can be assumed by trusted entities such as AWS services, IAM Users, or external identity providers. IAM Roles do not have long-term credentials; instead, IAM Roles issue temporary security credentials via AWS STS (Security Token Service) when assumed. Amazon EC2 instances use IAM Roles (attached as Instance Profiles) to securely interact with other AWS services without embedding Access Keys in code. IAM Roles are used for cross-account access, AWS service-to-service communication, and federated identity (SSO).

#### IAM Policies

An IAM Policy is a JSON document that defines permissions by specifying allowed or denied actions on AWS resources. IAM Policies are attached to IAM Users, IAM Groups, or IAM Roles to grant or restrict access. AWS Managed Policies are pre-built by AWS and can be reused across multiple identities; Customer Managed Policies are created and managed by the AWS customer. An IAM Policy evaluation follows the deny-by-default rule: all requests are denied unless an explicit Allow is present, and an explicit Deny always overrides any Allow.

**IAM Policy Structure (JSON):**
- `Version`: Policy language version (always `"2012-10-17"`)
- `Statement`: Array of individual permission statements
- `Effect`: Either `"Allow"` or `"Deny"`
- `Action`: The specific AWS API actions being permitted or denied (e.g., `"s3:GetObject"`)
- `Resource`: The ARN (Amazon Resource Name) of the AWS resource the statement applies to

#### IAM Best Practices

- Lock the AWS Root User account with MFA and do not use the Root User for daily tasks.
- Create individual IAM Users rather than sharing a single IAM User account.
- Use IAM Groups to assign permissions to collections of IAM Users.
- Grant only the least privilege permissions required for each IAM User or IAM Role.
- Use IAM Roles for AWS service-to-service communication instead of embedding Access Keys.
- Rotate IAM Access Keys regularly and remove unused credentials.
- Enable AWS CloudTrail to log all IAM API calls for audit purposes.

---

### AWS WAF vs. AWS Shield

#### AWS WAF (Web Application Firewall)

**AWS WAF** is a web application firewall service that protects web applications from common web exploits and attacks defined in OWASP Top 10, such as SQL injection and cross-site scripting (XSS). AWS WAF is deployed in front of Amazon CloudFront, Application Load Balancers (ALB), Amazon API Gateway, and AWS AppSync. AWS WAF uses Web ACLs (Access Control Lists) containing rules that inspect HTTP/HTTPS request headers, body, URI, query strings, and IP addresses. AWS WAF is a customer-configured service; customers define the specific rules and conditions that trigger allow or block actions.

#### AWS Shield

**AWS Shield** is a managed DDoS (Distributed Denial of Service) protection service that safeguards AWS applications against network and transport layer attacks. AWS Shield Standard is automatically enabled at no extra charge for all AWS customers and protects against common Layer 3 and Layer 4 DDoS attacks. AWS Shield Advanced is a paid tier that provides enhanced DDoS protection, 24/7 access to the AWS DDoS Response Team (DRT), and cost protection for scaling charges incurred during DDoS attacks. AWS Shield Advanced is recommended for applications on Amazon EC2, Elastic Load Balancing, Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53.

**Key Difference:** AWS WAF filters malicious application-layer (Layer 7) web traffic based on rules; AWS Shield protects against volumetric DDoS attacks at the network (Layer 3) and transport (Layer 4) layers.

---

### Security Groups vs. Network ACLs

#### AWS Security Groups

An AWS Security Group is a virtual stateful firewall that controls inbound and outbound traffic at the Amazon EC2 instance (ENI — Elastic Network Interface) level. Security Groups are stateful: if an inbound rule allows a request, the corresponding outbound response is automatically allowed regardless of outbound rules. Security Groups support Allow rules only; there are no explicit Deny rules in a Security Group. By default, a new Security Group denies all inbound traffic and allows all outbound traffic.

#### AWS Network ACLs (Access Control Lists)

An AWS Network ACL is a stateless firewall that controls traffic at the Amazon VPC Subnet level. Network ACLs are stateless: both inbound and outbound rules must be explicitly configured for each traffic direction. Network ACLs support both Allow and Deny rules, evaluated in order from lowest to highest rule number. The default Network ACL in an Amazon VPC allows all inbound and outbound traffic; custom Network ACLs deny all traffic until rules are explicitly added.

**Comparison Table:**

| Feature | Security Group | Network ACL |
|---|---|---|
| Level of operation | EC2 instance (ENI) | VPC Subnet |
| Statefulness | Stateful | Stateless |
| Rule types | Allow only | Allow and Deny |
| Rule evaluation | All rules evaluated | Rules evaluated in order (lowest number first) |
| Default behavior (new) | Deny all inbound, Allow all outbound | Depends on default vs. custom ACL |

---

### AWS Artifact

**AWS Artifact** is a self-service portal that provides on-demand access to AWS compliance documentation and AWS security reports. AWS Artifact allows customers to download AWS audit reports, including SOC reports, PCI DSS reports, and ISO certifications. AWS Artifact Agreements allows customers to review, accept, and manage agreements such as the Business Associate Agreement (BAA) required for HIPAA compliance. AWS Artifact is available at no additional charge through the AWS Management Console.

---

### Additional Security Services

#### AWS Inspector

**Amazon Inspector** is an automated vulnerability management service that continuously scans AWS workloads for software vulnerabilities and unintended network exposure. Amazon Inspector automatically discovers Amazon EC2 instances, container images in Amazon ECR, and AWS Lambda functions for vulnerability scanning. Primary use case: automated CVE (Common Vulnerabilities and Exposures) scanning and security findings for EC2 and container workloads.

#### AWS GuardDuty

**Amazon GuardDuty** is a threat detection service that continuously monitors AWS accounts and workloads for malicious activity using machine learning, anomaly detection, and integrated threat intelligence. Amazon GuardDuty analyzes AWS CloudTrail event logs, Amazon VPC Flow Logs, and DNS logs to identify threats such as compromised instances or unauthorized access. Primary use case: intelligent threat detection and continuous security monitoring across AWS accounts.

#### AWS Macie

**Amazon Macie** is a data security service that uses machine learning to automatically discover, classify, and protect sensitive data stored in Amazon S3. Amazon Macie identifies Personally Identifiable Information (PII) and other sensitive data, and provides alerts when data security risks are detected. Primary use case: automated sensitive data discovery and protection in Amazon S3.

#### AWS Config

**AWS Config** is a service that continuously monitors and records AWS resource configurations and evaluates configurations against desired settings using Config Rules. AWS Config maintains a historical record of AWS resource configuration changes, enabling compliance auditing and change management. Primary use case: compliance auditing, configuration drift detection, and resource change history for AWS environments.

#### AWS CloudTrail

**AWS CloudTrail** is a service that records AWS API calls and account activity across an AWS account, delivering log files to Amazon S3. AWS CloudTrail captures who made a request, from which IP address, at what time, and what response was returned. Primary use case: governance, compliance, operational auditing, and forensic analysis of AWS account activity.

#### AWS Security Hub

**AWS Security Hub** is a cloud security posture management service that aggregates, organizes, and prioritizes security findings from multiple AWS services and third-party tools into a single dashboard. AWS Security Hub continuously checks AWS environments against security best practices and compliance standards such as CIS AWS Foundations Benchmark. Primary use case: centralized security findings management and automated compliance checks across an AWS account.

#### AWS KMS (Key Management Service)

**AWS Key Management Service (KMS)** is a managed service that enables creation and control of cryptographic keys used to encrypt and decrypt data across AWS services. AWS KMS integrates natively with Amazon S3, Amazon EBS, Amazon RDS, and other AWS services for envelope encryption. Primary use case: centralized management of encryption keys for data at rest across AWS services.

#### AWS Secrets Manager

**AWS Secrets Manager** is a service that helps protect access to applications, services, and IT resources by enabling secure storage, retrieval, and automatic rotation of secrets such as database credentials, API keys, and OAuth tokens. AWS Secrets Manager eliminates the need to hard-code credentials in application code. Primary use case: secure storage and automatic rotation of application secrets and credentials.

---

## Domain 3: Cloud Technology and Services

---

### Compute Services

#### Amazon EC2 (Elastic Compute Cloud)

**Amazon EC2** is an AWS service that provides resizable virtual server instances in the AWS Cloud, allowing customers to run applications on virtual machines with configurable CPU, memory, storage, and networking. Amazon EC2 instances are launched from Amazon Machine Images (AMIs), which define the operating system and pre-installed software. Amazon EC2 supports Linux, Windows, and macOS operating systems. Primary use case: general-purpose compute for web servers, application servers, batch processing, and any workload requiring full OS control.

#### EC2 Instance Types

EC2 instance types are grouped into families optimized for specific workloads, defined by a combination of CPU, memory, storage, and networking capacity.

**General Purpose (T, M families)**
General Purpose instances provide a balance of compute, memory, and networking resources. Amazon EC2 T3 and T4g instances use a burstable CPU credit model suitable for workloads with variable CPU usage. Amazon EC2 M6i instances are optimized for web servers, small databases, and development environments. Use case: web servers, code repositories, microservices, and small-to-medium databases.

**Compute Optimized (C family)**
Compute Optimized instances provide a high ratio of vCPU to memory for compute-intensive workloads. Amazon EC2 C7g instances (Graviton3 processor) are designed for high-performance web servers, scientific modeling, and batch processing. Use case: high-performance computing (HPC), media transcoding, machine learning inference, and CPU-bound applications.

**Memory Optimized (R, X, z families)**
Memory Optimized instances deliver high memory capacity relative to CPU, suitable for memory-intensive applications. Amazon EC2 R7i instances are optimized for in-memory databases, real-time big data analytics, and large-scale caching workloads. Amazon EC2 X2idn instances provide the highest memory capacity for large in-memory databases such as SAP HANA. Use case: high-performance databases, in-memory caches (Redis, Memcached), and real-time big data processing.

**Storage Optimized (I, D, H families)**
Storage Optimized instances deliver high sequential read/write access to very large datasets on local NVMe SSD storage. Amazon EC2 I4i instances are designed for transactional databases (NoSQL) requiring very high I/O operations per second (IOPS). Amazon EC2 D3 instances are optimized for distributed file systems, Hadoop, and data warehousing workloads. Use case: high-frequency OLTP databases, Elasticsearch, data warehousing.

**Accelerated Computing (P, G, Inf, Trn families)**
Accelerated Computing instances use hardware accelerators (GPUs or AWS Trainium/Inferentia chips) to perform floating-point calculations, graphics processing, and ML training. Amazon EC2 P4d instances with NVIDIA A100 GPUs are used for ML training and HPC simulation. Amazon EC2 Inf2 instances powered by AWS Inferentia2 chips are optimized for large-scale ML model inference at low cost and latency. Use case: machine learning training, deep learning inference, graphics rendering, and genomics.

**High Performance Computing (Hpc family)**
Amazon EC2 Hpc7g instances are purpose-built for large-scale HPC workloads requiring tightly coupled parallel processing. HPC instances use AWS Elastic Fabric Adapter (EFA) for ultra-low latency, high-bandwidth networking between instances. Use case: computational fluid dynamics, weather simulation, financial modeling, and other tightly coupled HPC simulations.

---

#### AWS Lambda

**AWS Lambda** is a serverless compute service that runs code in response to events without requiring the customer to provision or manage any servers. AWS Lambda automatically scales by running code in parallel in response to the number of incoming requests or events. AWS Lambda supports multiple programming language runtimes including Python, Node.js, Java, Go, Ruby, and .NET. Primary use case: event-driven processing, backend APIs (via API Gateway), data transformation, automated responses to AWS service events (S3, DynamoDB, SNS, SQS).

**AWS Lambda Key Facts:**
- Maximum execution timeout: 15 minutes per invocation
- Memory: configurable from 128 MB to 10,240 MB
- Pricing: based on the number of requests and duration of execution (measured in GB-seconds)
- AWS Lambda is triggered by event sources including Amazon S3, Amazon DynamoDB Streams, Amazon Kinesis, Amazon SQS, Amazon SNS, Amazon API Gateway, and AWS CloudWatch Events

---

#### Amazon ECS (Elastic Container Service)

**Amazon ECS** is a fully managed container orchestration service that enables customers to run, stop, and manage Docker containers on a cluster of Amazon EC2 instances or using AWS Fargate serverless compute. Amazon ECS integrates natively with AWS services including Amazon ECR (Elastic Container Registry), Elastic Load Balancing, AWS IAM, and Amazon CloudWatch. Amazon ECS supports two launch types: EC2 (customer manages the EC2 host instances) and Fargate (AWS manages the underlying compute infrastructure). Primary use case: deploying microservices architectures, containerized web applications, and batch processing workloads using Docker containers.

---

#### Amazon EKS (Elastic Kubernetes Service)

**Amazon EKS** is a managed Kubernetes service that simplifies deploying, managing, and scaling Kubernetes containerized applications on AWS without needing to install, operate, or maintain the Kubernetes control plane. Amazon EKS automatically manages Kubernetes control plane availability, patching, and upgrades. Amazon EKS integrates with Amazon EC2, AWS Fargate, Amazon ECR, AWS IAM, Elastic Load Balancing, and AWS CloudWatch. Primary use case: running Kubernetes workloads on AWS for organizations that require Kubernetes compatibility, portability, and open-source ecosystem tools.

---

#### AWS Elastic Beanstalk

**AWS Elastic Beanstalk** is a PaaS service that automatically handles the deployment, capacity provisioning, load balancing, auto-scaling, and application health monitoring for applications written in Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker. AWS Elastic Beanstalk does not charge for the service itself; customers pay only for the underlying AWS resources (EC2, RDS, ELB, etc.) provisioned by Elastic Beanstalk. Primary use case: rapid deployment of web applications and APIs without managing the underlying infrastructure.

---

#### AWS Fargate

**AWS Fargate** is a serverless compute engine for Amazon ECS and Amazon EKS that removes the need to provision, configure, and manage EC2 instances for container workloads. AWS Fargate allows customers to specify CPU and memory requirements at the container task level and AWS manages the underlying compute. AWS Fargate pricing is based on the vCPU and memory resources consumed per second. Primary use case: running containers without managing the underlying server infrastructure.

---

### Storage Services

#### Amazon S3 (Simple Storage Service)

**Amazon S3** is an object storage service that provides industry-leading scalability, data availability, security, and performance for storing and retrieving any amount of data at any time. Amazon S3 stores data as objects (files) within buckets (containers), with each object addressable by a unique key. Amazon S3 provides 11 nines (99.999999999%) of data durability for all S3 storage classes by automatically distributing data across multiple Availability Zones (except S3 One Zone-IA). Amazon S3 is a regional service; bucket names must be globally unique across all AWS accounts.

#### Amazon S3 Storage Classes

**S3 Standard**
Amazon S3 Standard is designed for frequently accessed data requiring high throughput and low latency. S3 Standard provides 99.99% availability and 11 nines of durability, replicating data across a minimum of three AWS Availability Zones. S3 Standard has no minimum storage duration and no retrieval fees. Use case: active content distribution, web applications, big data analytics, and mobile and gaming applications.

**S3 Standard-IA (Infrequent Access)**
Amazon S3 Standard-IA is designed for data that is accessed less frequently but requires rapid access when needed. S3 Standard-IA provides the same 11 nines durability and millisecond latency as S3 Standard but at a lower storage cost with a per-GB retrieval fee. S3 Standard-IA has a minimum storage duration of 30 days. Use case: disaster recovery backups, long-term storage for infrequently accessed data requiring immediate retrieval.

**S3 One Zone-IA**
Amazon S3 One Zone-IA stores data in a single AWS Availability Zone, making it less resilient to AZ-level failures than other S3 storage classes. S3 One Zone-IA costs 20% less than S3 Standard-IA but does not replicate data across multiple Availability Zones. S3 One Zone-IA has a minimum storage duration of 30 days and a per-GB retrieval fee. Use case: secondary backup copies of on-premises data or easily re-creatable data that does not require multi-AZ resilience.

**S3 Intelligent-Tiering**
Amazon S3 Intelligent-Tiering automatically moves objects between access tiers (Frequent Access, Infrequent Access, Archive Instant Access, Archive Access, Deep Archive Access) based on changing access patterns. S3 Intelligent-Tiering charges a small monthly monitoring and automation fee per object but does not charge retrieval fees when moving between the Frequent and Infrequent Access tiers. S3 Intelligent-Tiering is ideal for data with unpredictable or changing access patterns. Use case: data lakes, analytics archives, and any storage where access patterns are unknown or variable.

**S3 Glacier Instant Retrieval**
Amazon S3 Glacier Instant Retrieval is designed for rarely accessed archive data that still requires millisecond retrieval latency. S3 Glacier Instant Retrieval provides the same retrieval speed as S3 Standard but at significantly lower storage costs. S3 Glacier Instant Retrieval has a minimum storage duration of 90 days and a per-GB retrieval fee. Use case: medical images, news media assets, and genomics data that must be accessed immediately but infrequently.

**S3 Glacier Flexible Retrieval (formerly S3 Glacier)**
Amazon S3 Glacier Flexible Retrieval offers low-cost archive storage with flexible retrieval options ranging from minutes to hours. S3 Glacier Flexible Retrieval offers three retrieval speeds: Expedited (1–5 minutes), Standard (3–5 hours), and Bulk (5–12 hours). S3 Glacier Flexible Retrieval has a minimum storage duration of 90 days. Use case: backup and archive data where periodic access is acceptable and retrieval time flexibility exists.

**S3 Glacier Deep Archive**
Amazon S3 Glacier Deep Archive is the lowest-cost AWS storage option, designed for long-term data retention with retrieval times of 12–48 hours. S3 Glacier Deep Archive offers Standard retrieval (within 12 hours) and Bulk retrieval (within 48 hours). S3 Glacier Deep Archive has a minimum storage duration of 180 days. Use case: regulatory compliance archives, financial records, healthcare records, and digital preservation requiring data retention of 7–10+ years.

**S3 Express One Zone**
Amazon S3 Express One Zone is a high-performance, single-Availability Zone storage class designed for single-digit millisecond latency for the most latency-sensitive applications. S3 Express One Zone stores data in a specific AWS Availability Zone (chosen by the customer) within S3 directory buckets. S3 Express One Zone provides up to 10x faster data access speeds compared to S3 Standard. Use case: machine learning training, interactive analytics, financial modeling, and real-time media processing.

---

#### Amazon EBS (Elastic Block Store)

**Amazon EBS** is a block storage service that provides persistent storage volumes attachable to Amazon EC2 instances, functioning like a virtual hard drive. Amazon EBS volumes exist independently of the EC2 instance lifecycle, persisting after the instance is stopped or terminated (unless configured otherwise). Amazon EBS volumes can only be attached to EC2 instances in the same Availability Zone. Primary use case: operating system volumes for EC2 instances, transactional databases, and applications requiring consistent low-latency block-level storage.

**Amazon EBS Volume Types:**
- **gp3 (General Purpose SSD)**: Cost-effective SSD storage for most workloads; baseline of 3,000 IOPS; use case: boot volumes, development environments, and low-latency interactive applications.
- **io2 Block Express (Provisioned IOPS SSD)**: Highest performance SSD for I/O-intensive workloads; up to 256,000 IOPS; use case: large relational/NoSQL databases requiring sub-millisecond latency.
- **st1 (Throughput Optimized HDD)**: Low-cost HDD for frequently accessed, throughput-intensive workloads; use case: big data, data warehouses, log processing.
- **sc1 (Cold HDD)**: Lowest-cost HDD for infrequently accessed data; use case: archiving and cold data storage.

---

#### Amazon EFS (Elastic File System)

**Amazon EFS** is a fully managed elastic NFS (Network File System) file storage service that automatically scales to petabytes of data as files are added or removed. Amazon EFS can be simultaneously mounted by thousands of Amazon EC2 instances across multiple Availability Zones within a Region, providing shared file storage. Amazon EFS automatically replicates data across multiple AWS Availability Zones, providing high availability and durability. Primary use case: shared file storage for web serving, content management systems (CMS), data sharing between EC2 instances, and containerized workloads.

---

#### AWS Storage Gateway

**AWS Storage Gateway** is a hybrid cloud storage service that provides on-premises applications with seamless access to AWS cloud storage such as Amazon S3, Amazon S3 Glacier, and Amazon EBS. AWS Storage Gateway offers three types: S3 File Gateway (file-based NFS/SMB access to S3), Volume Gateway (block storage backed by S3/EBS Snapshots), and Tape Gateway (virtual tape library backed by S3 Glacier). AWS Storage Gateway enables seamless data migration and hybrid storage architectures without requiring full application refactoring. Primary use case: hybrid cloud storage integration, data backup to AWS, and cloud tiering from on-premises environments.

---

### Database Services

#### Amazon RDS (Relational Database Service)

**Amazon RDS** is a managed relational database service that automates time-consuming administration tasks such as hardware provisioning, database setup, patching, and automated backups for relational databases. Amazon RDS supports six database engines: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle, and Microsoft SQL Server. Amazon RDS Multi-AZ deployments automatically provision and maintain a synchronous standby replica in a different Availability Zone for high availability and automatic failover. Primary use case: transactional relational databases for web applications, ERP systems, and CRM platforms requiring SQL compatibility and managed operations.

---

#### Amazon Aurora

**Amazon Aurora** is a MySQL and PostgreSQL-compatible relational database built for the AWS Cloud that delivers up to 5x the throughput of standard MySQL and 3x the throughput of standard PostgreSQL. Amazon Aurora automatically replicates data across six storage nodes in three AWS Availability Zones, providing high availability and durability. Amazon Aurora Serverless v2 automatically scales compute capacity based on application demand, pausing when idle to minimize costs. Primary use case: high-throughput, high-availability relational database workloads requiring MySQL or PostgreSQL compatibility.

---

#### Amazon DynamoDB

**Amazon DynamoDB** is a fully managed, serverless NoSQL key-value and document database service that delivers single-digit millisecond performance at any scale. Amazon DynamoDB automatically scales storage and throughput capacity based on demand and replicates data across multiple AWS Availability Zones for built-in high availability. Amazon DynamoDB Global Tables enable multi-region, multi-active replication for globally distributed applications. Primary use case: high-traffic web applications, gaming leaderboards, real-time bidding platforms, IoT data stores, and any workload requiring single-digit millisecond latency at scale.

---

#### Amazon Redshift

**Amazon Redshift** is a fully managed, petabyte-scale cloud data warehouse service that uses columnar storage and massively parallel processing (MPP) to deliver fast query performance for analytical workloads. Amazon Redshift integrates with Amazon S3 via Redshift Spectrum, allowing queries directly on data in Amazon S3 without loading it into Redshift. Amazon Redshift Serverless automatically provisions and scales data warehouse capacity based on workload demands. Primary use case: large-scale business intelligence (BI), analytics, and data warehousing workloads requiring complex SQL queries across terabytes to petabytes of structured data.

---

#### Amazon ElastiCache

**Amazon ElastiCache** is a fully managed in-memory caching service supporting Redis and Memcached engines, used to improve application performance by reducing database load. Amazon ElastiCache for Redis supports data persistence, pub/sub messaging, and replication; ElastiCache for Memcached is designed for simple, high-performance caching use cases. Primary use case: caching database query results, session management, real-time leaderboards, and reducing read latency for frequently accessed data.

---

#### Amazon DocumentDB

**Amazon DocumentDB** is a fully managed document database service that is compatible with MongoDB workloads and stores data as JSON-like documents. Amazon DocumentDB separates compute and storage, allowing each to scale independently. Primary use case: content management, catalog management, user profiles, and any MongoDB-compatible document database workload.

---

#### Amazon Neptune

**Amazon Neptune** is a fully managed graph database service optimized for storing and querying highly connected datasets using graph query languages (Gremlin, SPARQL, openCypher). Amazon Neptune supports two graph models: property graphs and RDF (Resource Description Framework). Primary use case: knowledge graphs, fraud detection, social networks, recommendation engines, and network/IT operations.

---

### Networking Services

#### Amazon VPC (Virtual Private Cloud)

**Amazon VPC** is a service that enables AWS customers to launch AWS resources in a logically isolated virtual network that the customer defines, including IP address ranges, subnets, route tables, and network gateways. Amazon VPC is the foundational networking layer for all AWS compute services and enables complete control over virtual networking environments. Amazon VPC supports IPv4 and IPv6 addressing and can be connected to on-premises networks via AWS Direct Connect or AWS VPN. Primary use case: network isolation and security for AWS workloads, including multi-tier application architectures.

**Amazon VPC Components:**
- **Subnets**: Subdivisions of a VPC's IP address range, scoped to a single Availability Zone; public subnets route traffic through an Internet Gateway, private subnets do not.
- **Internet Gateway (IGW)**: A horizontally scaled, redundant VPC component that enables communication between VPC resources and the internet.
- **NAT Gateway**: A managed AWS service that allows EC2 instances in private subnets to initiate outbound internet connections without exposing the instances to inbound internet traffic.
- **Route Tables**: Define the routing rules for traffic originating from subnets within a VPC.
- **VPC Peering**: A networking connection between two Amazon VPCs enabling traffic routing using private IP addresses.
- **AWS Transit Gateway**: A network transit hub that connects multiple Amazon VPCs and on-premises networks through a central routing service, simplifying complex hub-and-spoke architectures.

---

#### Subnets

An Amazon VPC Subnet is a range of IP addresses within a VPC scoped to a single AWS Availability Zone. A Public Subnet is a subnet whose associated route table contains a route to an Internet Gateway, allowing resources to communicate with the internet. A Private Subnet does not have a direct route to an Internet Gateway; outbound internet access is provided via a NAT Gateway for resources in private subnets. Subnets are used to separate tiers of an application (e.g., web, application, and database tiers) across different network segments for security and resilience.

---

#### Amazon Route 53

**Amazon Route 53** is a highly available and scalable cloud DNS (Domain Name System) web service that translates domain names (e.g., www.example.com) into IP addresses. Amazon Route 53 supports multiple routing policies including Simple, Weighted, Latency-based, Failover, Geolocation, Geoproximity, Multi-Value Answer, and IP-based routing. Amazon Route 53 Health Checks monitor the health of AWS resources and external endpoints and can automatically reroute traffic during failures. Primary use case: domain registration, DNS management, and traffic routing with health-check-based failover for globally distributed applications.

---

#### Amazon CloudFront

**Amazon CloudFront** is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds through a worldwide network of edge locations. Amazon CloudFront caches content at AWS edge locations closest to end users, reducing latency and offloading origin servers. Amazon CloudFront integrates with AWS Shield for DDoS protection and AWS WAF for web application firewall capabilities at the edge. Primary use case: global delivery of static and dynamic web content, video streaming, APIs, and software distribution.

---

#### AWS Direct Connect

**AWS Direct Connect** is a dedicated private network connection service between an on-premises data center and an AWS Region, bypassing the public internet. AWS Direct Connect provides consistent network performance, reduced bandwidth costs for high-volume data transfer, and a more private connection compared to internet-based VPN. AWS Direct Connect connections are available in 1 Gbps, 10 Gbps, and 100 Gbps capacities. Primary use case: hybrid cloud connectivity requiring consistent low-latency, high-throughput, or private network connections to AWS.

---

#### Elastic Load Balancing (ELB)

**AWS Elastic Load Balancing (ELB)** is a service that automatically distributes incoming application traffic across multiple targets such as Amazon EC2 instances, containers, IP addresses, and AWS Lambda functions. ELB offers three types: Application Load Balancer (ALB) for HTTP/HTTPS Layer 7 routing, Network Load Balancer (NLB) for ultra-high performance Layer 4 TCP/UDP routing, and Gateway Load Balancer (GWLB) for deploying third-party virtual network appliances. Primary use case: fault tolerance and horizontal scaling for web applications, microservices, and multi-tier architectures.

---

#### Amazon API Gateway

**Amazon API Gateway** is a fully managed service that enables developers to create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale. Amazon API Gateway integrates natively with AWS Lambda to enable fully serverless API backends. Primary use case: creating RESTful and WebSocket APIs for serverless backends, mobile applications, and microservices.

---

### Additional AWS Technology Services

#### Amazon SNS (Simple Notification Service)

**Amazon SNS** is a fully managed pub/sub messaging service that enables decoupled communication between distributed systems by sending messages to multiple subscribers simultaneously. Amazon SNS supports delivery protocols including HTTP/HTTPS, email, SMS, mobile push notifications, AWS Lambda, and Amazon SQS. Primary use case: fan-out messaging, application-to-application (A2A) notifications, mobile push notifications, and alert systems.

---

#### Amazon SQS (Simple Queue Service)

**Amazon SQS** is a fully managed message queuing service that enables decoupling of microservices, distributed systems, and serverless applications by storing messages in a queue until processed. Amazon SQS offers two queue types: Standard (best-effort ordering, at-least-once delivery) and FIFO (First-In-First-Out, exactly-once processing). Primary use case: decoupling application components, buffering requests, and ensuring fault-tolerant asynchronous processing between services.

---

#### AWS CloudFormation

**AWS CloudFormation** is an infrastructure-as-code (IaC) service that enables AWS customers to model, provision, and manage AWS resources using declarative JSON or YAML templates. AWS CloudFormation templates define AWS resource configurations, and CloudFormation automatically handles dependencies and provisioning order. Primary use case: repeatable, automated provisioning of AWS infrastructure across multiple environments (dev, staging, production) using version-controlled templates.

---

#### Amazon CloudWatch

**Amazon CloudWatch** is a monitoring and observability service that collects and tracks metrics, collects and monitors log files, and sets alarms for AWS resources and applications. Amazon CloudWatch Alarms trigger automated actions (SNS notifications, Auto Scaling policies, EC2 actions) when metric thresholds are breached. Primary use case: infrastructure monitoring, application performance monitoring, log aggregation, and automated operational responses.

---

#### AWS Auto Scaling

**AWS Auto Scaling** monitors applications and automatically adjusts compute capacity across Amazon EC2, Amazon ECS, Amazon DynamoDB, and Amazon Aurora to maintain steady, predictable performance at the lowest possible cost. Amazon EC2 Auto Scaling uses Launch Templates and Scaling Policies (Target Tracking, Step, Scheduled) to add or remove EC2 instances based on demand. Primary use case: automatic right-sizing of compute resources in response to traffic fluctuations to maintain performance and minimize costs.

---

## Domain 4: Billing, Pricing, and Support

---

### AWS Pricing Fundamentals

AWS follows three fundamental pricing principles: pay-as-you-go (no upfront costs or long-term commitments for on-demand usage), save when you reserve (lower rates for committed usage via Reserved Instances or Savings Plans), and pay less when using more (volume-based tiered pricing for services like Amazon S3 and Amazon CloudFront). AWS charges for compute, storage, and outbound data transfer. AWS does not charge for inbound data transfer to AWS services. AWS provides a free tier for 12 months after account creation for a limited set of services, plus always-free and trial offerings.

---

### EC2 Pricing Models

#### On-Demand Instances

Amazon EC2 On-Demand Instances allow customers to pay for compute capacity by the hour or second (minimum 60 seconds) with no long-term commitments or upfront payments. On-Demand Instances are the most flexible pricing option and are recommended for unpredictable workloads, short-term development, and testing environments. On-Demand Instances carry the highest per-hour cost compared to other Amazon EC2 pricing models. On-Demand Instances can be started and stopped at any time without penalty.

#### Reserved Instances (RI)

Amazon EC2 Reserved Instances provide a significant discount (up to 72%) compared to On-Demand pricing in exchange for a 1-year or 3-year term commitment for a specific instance type in a specific AWS Region. Reserved Instances are available in three payment options: All Upfront (highest discount), Partial Upfront (mid-level discount), and No Upfront (lowest discount, still lower than On-Demand). Standard Reserved Instances offer the deepest discount but cannot be modified; Convertible Reserved Instances offer a smaller discount but allow instance type and OS changes during the term. Reserved Instances are recommended for steady-state, predictable workloads running continuously for 1–3 years.

#### Spot Instances

Amazon EC2 Spot Instances allow customers to request unused Amazon EC2 capacity at discounts of up to 90% compared to On-Demand prices. Spot Instances can be interrupted by AWS with a 2-minute warning when the Spot capacity is reclaimed by AWS for On-Demand usage. Spot Instances are not suitable for workloads that cannot tolerate interruption; AWS provides the 2-minute Spot Instance interruption notice via instance metadata. Spot Instances are ideal for fault-tolerant, flexible workloads such as batch processing, data analysis, image rendering, and CI/CD pipelines.

#### Savings Plans

AWS Savings Plans offer flexible pricing models that provide significant savings (up to 72%) compared to On-Demand pricing in exchange for a consistent amount of compute usage (measured in $/hour) committed over a 1- or 3-year term. Compute Savings Plans apply automatically to any Amazon EC2 instance (any family, size, OS, tenancy, or Region), AWS Fargate, and AWS Lambda, offering up to 66% savings. EC2 Instance Savings Plans apply to a specific EC2 instance family in a specific Region, offering up to 72% savings. Savings Plans are more flexible than Reserved Instances because they are not tied to a specific instance type or AZ, automatically applying to eligible usage.

**EC2 Pricing Model Comparison:**

| Pricing Model | Discount vs. On-Demand | Commitment | Best For |
|---|---|---|---|
| On-Demand | None | None | Unpredictable, short-term workloads |
| Reserved Instances | Up to 72% | 1 or 3 years | Steady-state, predictable workloads |
| Spot Instances | Up to 90% | None | Fault-tolerant, interruptible workloads |
| Savings Plans | Up to 72% | 1 or 3 years | Flexible compute across EC2, Fargate, Lambda |

---

### Dedicated Hosts and Dedicated Instances

**Amazon EC2 Dedicated Hosts** are physical AWS servers fully dedicated to a single customer, enabling the use of existing per-socket, per-core, or per-VM software licenses (BYOL — Bring Your Own License). Dedicated Hosts provide visibility into physical server details (sockets, cores) for licensing compliance. Use case: regulatory requirements mandating physical server isolation or BYOL software licensing.

**Amazon EC2 Dedicated Instances** run on hardware dedicated to a single customer but do not provide visibility into the physical host details. Dedicated Instances are billed per instance and are isolated at the hardware level from instances belonging to other AWS accounts. Use case: compliance requirements mandating dedicated hardware without specific server-level licensing needs.

---

### AWS Organizations

**AWS Organizations** is an account management service that enables customers to consolidate multiple AWS accounts into an organization that can be centrally managed. AWS Organizations provides consolidated billing, which combines the usage of all member accounts and applies AWS volume pricing tiers across the entire organization. AWS Organizations uses Service Control Policies (SCPs) to centrally control the maximum available permissions for member accounts, providing guardrails without managing individual IAM policies. Primary use case: multi-account governance, consolidated billing to maximize volume discounts, and centralized policy enforcement across an enterprise AWS environment.

**Consolidated Billing Benefits:**
- All member account charges aggregate to a single master/management account invoice, simplifying payment management.
- Volume pricing tiers (e.g., for Amazon S3, Amazon EC2) are applied across the combined usage of all accounts in the organization.
- Reserved Instance and Savings Plan discounts can be shared across member accounts within an AWS Organization.
- AWS Organizations consolidated billing enables detailed cost visibility using AWS Cost Explorer at the organization level.

---

### AWS Cost Management Tools

#### AWS Cost Explorer

**AWS Cost Explorer** is a tool that enables customers to visualize, understand, and manage AWS costs and usage over time using interactive charts and tables. AWS Cost Explorer provides up to 12 months of historical cost data and up to 12 months of cost forecasting using machine learning. AWS Cost Explorer includes Reserved Instance utilization and coverage reports, and Savings Plans recommendations based on historical usage patterns. Primary use case: analyzing historical AWS spending, identifying cost trends, rightsizing EC2 recommendations, and forecasting future AWS costs.

#### AWS Budgets

**AWS Budgets** is a tool that enables customers to set custom cost and usage budgets and receive alerts via Amazon SNS or email when actual or forecasted spending exceeds defined thresholds. AWS Budgets supports four budget types: Cost Budgets (monitor total spend), Usage Budgets (monitor resource consumption), RI Utilization Budgets (track RI usage), and RI Coverage Budgets (track RI coverage). AWS Budgets can trigger automated actions (e.g., applying IAM policies, stopping EC2 instances) when budget thresholds are reached. Primary use case: proactive cost control and overspend prevention through threshold-based budget alerts and automated remediation actions.

**AWS Cost Explorer vs. AWS Budgets:**

| Feature | AWS Cost Explorer | AWS Budgets |
|---|---|---|
| Primary purpose | Historical cost analysis and forecasting | Proactive alerting and budget enforcement |
| Direction | Reactive (analyze past spend) | Proactive (alert on future spend) |
| Automation | No direct automated actions | Can trigger automated actions (IAM policies, EC2 stop) |
| Data | 12 months historical, 12-month forecast | Current and forecasted spend vs. budget |

---

#### AWS Pricing Calculator

**AWS Pricing Calculator** is a free web-based tool that allows customers to estimate the cost of AWS services before deploying resources. AWS Pricing Calculator supports building cost estimates for multi-service architectures and exporting estimates for sharing with stakeholders. Primary use case: pre-deployment cost estimation and TCO (Total Cost of Ownership) comparisons for AWS migrations.

---

#### AWS Cost and Usage Report (CUR)

**AWS Cost and Usage Report (CUR)** is the most comprehensive and granular source of AWS cost and usage data, delivering detailed billing reports to Amazon S3 at hourly, daily, or monthly granularity. AWS CUR includes cost data broken down by AWS service, usage type, resource ID, tags, and linked accounts. Primary use case: detailed billing analysis, chargeback/showback reporting, and integration with BI tools such as Amazon Quicksight and Tableau.

---

#### AWS Trusted Advisor

**AWS Trusted Advisor** is an AWS tool that provides real-time guidance and best practice recommendations across five categories: Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits. AWS Trusted Advisor checks compare the customer's AWS infrastructure against AWS best practices and surface actionable recommendations. The number of Trusted Advisor checks available depends on the AWS Support Plan: Basic/Developer plans provide access to a core set of checks; Business and Enterprise plans unlock all checks. Primary use case: identifying cost savings opportunities, security vulnerabilities, and architectural improvements across an AWS account.

---

### AWS Support Plans

AWS offers four support plan tiers with progressively increasing features, response times, and costs: Basic, Developer, Business, and Enterprise.

#### AWS Basic Support

AWS Basic Support is included at no additional charge for all AWS accounts. AWS Basic Support provides access to AWS documentation, whitepapers, AWS re:Post (community forums), AWS Personal Health Dashboard, and a limited set of AWS Trusted Advisor checks. AWS Basic Support does not provide access to AWS Support engineers via phone, email, or chat for technical cases. Basic Support is suitable for AWS accounts in the early exploration or development phase with no production workloads.

#### AWS Developer Support

AWS Developer Support costs a minimum of $29/month or 3% of monthly AWS usage (whichever is greater). AWS Developer Support provides business hours email access to Cloud Support Associates for technical questions. AWS Developer Support guarantees a response time of less than 24 hours for general guidance and less than 12 hours for system impaired cases. Developer Support is recommended for customers experimenting with AWS or in early development phases with non-production workloads.

#### AWS Business Support

AWS Business Support costs a minimum of $100/month or a percentage of monthly AWS usage (10% for the first $0–$10K, scaling down at higher tiers). AWS Business Support provides 24/7 phone, email, and chat access to Cloud Support Engineers for technical issues affecting production workloads. AWS Business Support guarantees a response time of less than 4 hours for production system impaired cases and less than 1 hour for production system down cases. AWS Business Support includes full access to all AWS Trusted Advisor checks, AWS Support API access, and access to Infrastructure Event Management for an additional fee.

#### AWS Enterprise On-Ramp Support

AWS Enterprise On-Ramp Support costs a minimum of $5,500/month or a percentage of monthly AWS usage. AWS Enterprise On-Ramp Support provides 24/7 access to Cloud Support Engineers and a pool of Technical Account Managers (TAMs) for proactive guidance. AWS Enterprise On-Ramp guarantees a response time of less than 30 minutes for business-critical system down cases. Use case: production/business-critical workloads that need some TAM engagement without the full Enterprise TAM commitment.

#### AWS Enterprise Support

AWS Enterprise Support costs a minimum of $15,000/month or a percentage of monthly AWS usage. AWS Enterprise Support provides 24/7 access to senior Cloud Support Engineers, a designated Technical Account Manager (TAM), and access to the AWS Infrastructure Event Management service. AWS Enterprise Support guarantees a response time of less than 15 minutes for business-critical system down cases. AWS Enterprise Support includes Concierge Support for billing and account assistance, Well-Architected Reviews, and operational reviews with the designated TAM.

**AWS Support Plan Comparison:**

| Feature | Basic | Developer | Business | Enterprise On-Ramp | Enterprise |
|---|---|---|---|---|---|
| Cost | Free | $29/month min | $100/month min | $5,500/month min | $15,000/month min |
| Technical support access | None | Business hours email | 24/7 phone/email/chat | 24/7 phone/email/chat | 24/7 phone/email/chat |
| Business-critical response | N/A | N/A | < 1 hour | < 30 minutes | < 15 minutes |
| Trusted Advisor checks | Limited | Limited | All checks | All checks | All checks |
| Technical Account Manager | No | No | No | Pool of TAMs | Designated TAM |
| Concierge Support | No | No | No | No | Yes |

---

### AWS Marketplace

**AWS Marketplace** is a digital catalog of thousands of software solutions from independent software vendors (ISVs) that can be deployed and billed directly through AWS. AWS Marketplace listings include AMIs, CloudFormation templates, SaaS subscriptions, containers, and professional services. AWS Marketplace purchases are consolidated into the customer's AWS bill through AWS consolidated billing. Primary use case: rapid procurement of third-party software solutions (security tools, databases, ML models, networking tools) with simplified billing through AWS accounts.

---

### AWS Free Tier

The AWS Free Tier provides three types of free offers to help customers explore AWS services at no cost. Always Free offers never expire and are available to all AWS customers (e.g., AWS Lambda: 1 million free requests/month; Amazon DynamoDB: 25 GB storage; AWS CloudWatch: 10 custom metrics). 12 Months Free offers are available for 12 months after the initial AWS account sign-up date (e.g., Amazon EC2: 750 hours/month of t2.micro or t3.micro; Amazon S3: 5 GB Standard storage; Amazon RDS: 750 hours/month of db.t3.micro). Trials are short-term free offers available for specific services (e.g., Amazon Redshift: 2-month free trial).

---

### AWS Total Cost of Ownership (TCO)

TCO analysis for cloud migration compares the full cost of running on-premises infrastructure (including hardware, facilities, power, cooling, and IT staff) against equivalent AWS Cloud infrastructure costs. AWS Pricing Calculator and AWS Migration Evaluator (formerly TSO Logic) can be used to build TCO comparisons for cloud migration decisions. AWS Cloud typically reduces TCO by eliminating capital expenditure on hardware, reducing data center operational costs, and enabling right-sizing of resources. TCO analysis should account for AWS volume discounts, Reserved Instance pricing, and reduced operational overhead when comparing to on-premises costs.

---

*End of AWS CLF-C02 Ultimate RAG Study Guide*
