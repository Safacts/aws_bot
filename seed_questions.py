import asyncio
import json
import logging
from database import init_db, AsyncSessionLocal, QuestionBank

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Curated CLF-C02 Question Bank (50+ questions)
QUESTION_BANK = [
    # Domain 1: Cloud Concepts
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "Which cloud benefit allows a company to stop guessing about capacity needs and instead use only what they need?",
        "options": ["High Availability", "Elasticity", "Global Reach", "Security"],
        "correct_index": 1,
        "explanation": "Stay steady, Partha. Elasticity allows resources to scale up and down as needed, eliminating the need to over-provision capacity for peak loads while saving costs during low-demand periods."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "A startup wants to trade their upfront capital expenses (CapEx) for variable operational expenses (OpEx). Which cloud advantage does this describe?",
        "options": ["Speed and Agility", "Economy of Scale", "Stop spending money running data centers", "Increase Speed and Agility"],
        "correct_index": 2,
        "explanation": "Focus your mind, Partha. By using the cloud, businesses can stop spending money on heavy capital expenses like physical data centers and instead pay for only what they consume as an operational cost."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "Which of the following describes a 'Hybrid' cloud deployment model?",
        "options": ["Running all workloads on AWS", "Running all workloads in a local private data center", "Connecting an on-premises data center to an AWS VPC", "Using multiple public cloud providers simultaneously"],
        "correct_index": 2,
        "explanation": "Look at the path, Partha. A hybrid model combines on-premises infrastructure (private cloud) with public cloud resources (like AWS) to create a unified environment."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "Which service model gives the customer the most control over the underlying operating system and networking?",
        "options": ["SaaS", "PaaS", "IaaS", "Serverless"],
        "correct_index": 2,
        "explanation": "Identify the foundation, Partha. Infrastructure as a Service (IaaS) provides the highest level of control over networking, servers, and storage, while the provider manages the physical hardware."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "Which AWS Global Infrastructure component consists of one or more discrete data centers with redundant power and networking?",
        "options": ["Region", "Availability Zone", "Edge Location", "Local Zone"],
        "correct_index": 1,
        "explanation": "Seek the details, Partha. An Availability Zone (AZ) is a cluster of data centers within a Region that are physically separated to provide isolation from failures."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "What is the primary purpose of an AWS Edge Location?",
        "options": ["To run compute workloads", "To store long-term archival data", "To deliver content to users with lower latency via CloudFront", "To provide backup power for Regions"],
        "correct_index": 2,
        "explanation": "Aim for efficiency, Partha. Edge Locations are cached content delivery nodes that bring data closer to end-users to reduce latency."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "Which pillar of the AWS Well-Architected Framework focuses on the ability to prevent, and quickly recover from failures?",
        "options": ["Operational Excellence", "Security", "Reliability", "Performance Efficiency"],
        "correct_index": 2,
        "explanation": "Find your strength, Partha. The Reliability pillar ensures that a system can perform its intended function correctly and recover from infrastructure or service disruptions."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "Which pillar of the AWS Well-Architected Framework focuses on running and monitoring systems to deliver business value?",
        "options": ["Operational Excellence", "Security", "Reliability", "Cost Optimization"],
        "correct_index": 0,
        "explanation": "Understand the action, Partha. Operational Excellence focuses on improving processes, monitoring systems, and delivering business value through automation."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "Which cloud benefit refers to the ability to deploy an application in multiple regions around the world in minutes?",
        "options": ["High Availability", "Elasticity", "Global Reach", "Durability"],
        "correct_index": 2,
        "explanation": "See the world, Partha. Global Reach (or Go Global in Minutes) refers to the ease of deploying infrastructure in different AWS Regions worldwide to serve global customers."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "A customer is using Gmail for their company email. Which cloud service model does this represent?",
        "options": ["IaaS", "PaaS", "SaaS", "DBaaS"],
        "correct_index": 2,
        "explanation": "Recognize the finished product, Partha. Software as a Service (SaaS) provides a complete application that is managed by the service provider, leaving the customer responsible only for usage."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "How does AWS achieve 'High Availability' for most services?",
        "options": ["Using one powerful data center", "Distributing resources across multiple Availability Zones", "Using multiple cloud providers", "Increasing CPU power automatically"],
        "correct_index": 1,
        "explanation": "Build for resilience, Partha. High availability is achieved by spreading workloads across multiple discrete Availability Zones within a region so that the failure of one does not bring down the entire system."
    },
    {
        "domain": "Domain 1: Cloud Concepts",
        "question": "In the public cloud, who is responsible for the physical security of the server hardware?",
        "options": ["The Customer", "The Cloud Provider (AWS)", "Third-party security firms", "The Internet Service Provider"],
        "correct_index": 1,
        "explanation": "Know the roles, Partha. In a public cloud model, the provider (AWS) is always responsible for the security 'of' the cloud, which includes the physical data centers and hardware."
    },

    # Domain 2: Security
    {
        "domain": "Domain 2: Security",
        "question": "Under the AWS Shared Responsibility Model, which task is the responsibility of the customer?",
        "options": ["Maintaining hardware and software infrastructure", "Patching the guest operating system on EC2", "Physical security of the data center", "Decommissioning old hard drives"],
        "correct_index": 1,
        "explanation": "Carry your own burden, Partha. While AWS manages the host infrastructure, the customer is responsible for patching and securing the guest OS and applications (Security IN the Cloud)."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which AWS IAM component is used to manage a collection of users with the same permissions?",
        "options": ["IAM Users", "IAM Groups", "IAM Roles", "IAM Policies"],
        "correct_index": 1,
        "explanation": "Gather your allies, Partha. IAM Groups allow you to assign a set of permissions to multiple users at once, simplifying management as your team grows."
    },
    {
        "domain": "Domain 2: Security",
        "question": "An employee needs temporary permissions to access an S3 bucket without using permanent credentials. What should they use?",
        "options": ["IAM User", "IAM Role", "MFA", "AWS Root Account"],
        "correct_index": 1,
        "explanation": "Assume a new form, Partha. IAM Roles provide temporary security credentials for users, applications, or services that need to perform actions they don't normally have permission for."
    },
    {
        "domain": "Domain 2: Security",
        "question": "What is the best practice for the AWS Root user account?",
        "options": ["Use it for daily administrative tasks", "Share the password with all developers", "Enable MFA and stop using it for everyday tasks", "Disable it entirely"],
        "correct_index": 2,
        "explanation": "Guard the source, Partha. The root account has absolute permissions; it should be secured with MFA and used only for a few specific tasks that strictly require it."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which AWS service helps manage multiple AWS accounts centrally with consolidated billing?",
        "options": ["AWS Config", "AWS Organizations", "AWS Control Tower", "AWS Trusted Advisor"],
        "correct_index": 1,
        "explanation": "Unify the kingdom, Partha. AWS Organizations allows you to centrally govern and manage multiple accounts, including setting Service Control Policies (SCPs) and using consolidated billing."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which AWS service provides managed DDoS protection at no extra cost for all AWS customers?",
        "options": ["AWS WAF", "AWS Shield Standard", "AWS GuardDuty", "AWS Firewall Manager"],
        "correct_index": 1,
        "explanation": "Deflect the arrows, Partha. AWS Shield Standard is automatically active for all AWS customers and protects against common infrastructure (layer 3 and 4) DDoS attacks."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which service acts as an intelligent threat detection system that monitors for malicious activity in your AWS accounts?",
        "options": ["AWS Shield", "AWS Inspector", "AWS GuardDuty", "AWS Config"],
        "correct_index": 2,
        "explanation": "Keep watch, Partha. GuardDuty uses machine learning and threat intelligence to analyze logs and detect unauthorized or malicious behavior across your AWS environment."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which service is used to discover and protect sensitive data in S3 using machine learning?",
        "options": ["AWS Macie", "AWS Inspector", "AWS Shield", "AWS Secrets Manager"],
        "correct_index": 0,
        "explanation": "Find the secrets, Partha. Macie is a fully managed data security and privacy service that automatically discovers and protects sensitive data like PII in Amazon S3."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which service allows you to create, manage, and rotate cryptographic keys used for encryption at rest?",
        "options": ["AWS CloudHSM", "AWS KMS", "AWS ACM", "AWS Secrets Manager"],
        "correct_index": 1,
        "explanation": "Secure the treasury, Partha. Key Management Service (KMS) makes it easy to create and control the keys used to encrypt your data across AWS services."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which service is primarily used to securely store and automatically rotate database credentials and API keys?",
        "options": ["AWS KMS", "AWS IAM", "AWS Secrets Manager", "AWS Systems Manager Parameter Store"],
        "correct_index": 2,
        "explanation": "Hide the keys, Partha. Secrets Manager allows you to manage lifecycle secrets, including automatic rotation for supported databases, reducing the risk of credential leakage."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which tool provides automated security assessments to improve the security and compliance of applications deployed on EC2?",
        "options": ["AWS Shield", "AWS Amazon Inspector", "AWS GuardDuty", "AWS Trusted Advisor"],
        "correct_index": 1,
        "explanation": "Examine the work, Partha. Amazon Inspector analyzes EC2 instances for exposure, vulnerabilities, and deviations from best practices."
    },
    {
        "domain": "Domain 2: Security",
        "question": "Which of these is an AWS responsibility under the Shared Responsibility Model?",
        "options": ["Data encryption in transit", "Configuring network ACLs", "Managing the hardware virtualization layer", "IAM user management"],
        "correct_index": 2,
        "explanation": "Trust the master, Partha. AWS is responsible for the 'infrastructure layer' of the cloud, which includes the physical host, hardware, and the virtualization software."
    },

    # Domain 3: Cloud Technology
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which EC2 pricing model offers the deepest discount (up to 90%) but can be interrupted at any time?",
        "options": ["On-Demand", "Reserved Instances", "Spot Instances", "Dedicated Hosts"],
        "correct_index": 2,
        "explanation": "Seize the moment, Partha. Spot Instances allow you to use spare AWS compute capacity at a massive discount, but AWS can reclaim them with a 2-minute notice."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which S3 storage class is intended for data that is infrequently accessed but requires immediate retrieval when needed?",
        "options": ["S3 Standard", "S3 Standard-IA", "S3 One Zone-IA", "S3 Glacier"],
        "correct_index": 1,
        "explanation": "Choose wisely, Partha. S3 Standard-IA (Infrequent Access) is designed for data that is rarely accessed but needs milliseconds-fast retrieval when requested."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which database service is a managed NoSQL database capable of millisecond latency at any scale?",
        "options": ["Amazon RDS", "Amazon DynamoDB", "Amazon Redshift", "Amazon Aurora"],
        "correct_index": 1,
        "explanation": "Seek the swift, Partha. DynamoDB is a fully managed, key-value, and document database that delivers single-digit millisecond performance at massive scale."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which compute service allows you to run code without provisioning or managing servers?",
        "options": ["Amazon EC2", "Amazon ECS", "AWS Lambda", "AWS Lightsail"],
        "correct_index": 2,
        "explanation": "Act without weight, Partha. AWS Lambda is a serverless compute service that runs your code only in response to triggers and scales automatically."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which service automatically distributes incoming application traffic across multiple targets like EC2 instances?",
        "options": ["Auto Scaling", "Elastic Load Balancing (ELB)", "Route 53", "CloudFront"],
        "correct_index": 1,
        "explanation": "Distribute the burden, Partha. ELB manages the flow of incoming traffic by distributing it across multiple health targets in different AZs for higher availability."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which service allows a company to add or remove EC2 instances automatically based on changing demand?",
        "options": ["Elastic Load Balancing", "Amazon CloudWatch", "Amazon EC2 Auto Scaling", "AWS OpsWorks"],
        "correct_index": 2,
        "explanation": "Flow with the tide, Partha. Auto Scaling ensures you have the right number of EC2 instances available to handle the load for your application."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which service provides a highly available and scalable Domain Name System (DNS) web service?",
        "options": ["Amazon CloudFront", "Amazon Route 53", "AWS Direct Connect", "Amazon VPC"],
        "correct_index": 1,
        "explanation": "Find the path, Partha. Route 53 is AWS's cloud DNS service that connects user requests to infrastructure running in AWS or on-premises."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which service acts as a Content Delivery Network (CDN) to speed up distribution of static and dynamic web content?",
        "options": ["Amazon CloudFront", "Amazon Route 53", "S3 Transfer Acceleration", "AWS Global Accelerator"],
        "correct_index": 0,
        "explanation": "Bring it closer, Partha. CloudFront caches data at Edge Locations globally to decrease latency for users accessing your website or data."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which AWS feature allows you to create a logically isolated section of the AWS Cloud where you can launch resources?",
        "options": ["Region", "Availability Zone", "Amazon VPC", "AWS Subnet"],
        "correct_index": 2,
        "explanation": "Carve your space, Partha. Virtual Private Cloud (VPC) gives you full control over your virtual networking environment, including IP ranges, subnets, and routes."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which service provides a dedicated network connection from an on-premises data center to AWS?",
        "options": ["AWS Site-to-Site VPN", "AWS Direct Connect", "Amazon VPC Peering", "AWS Transit Gateway"],
        "correct_index": 1,
        "explanation": "Link the worlds, Partha. Direct Connect establishes a private, physical fiber-optic connection between your network and AWS, bypassing the public internet."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which member of the AWS Snow Family is a petabyte-scale data transport device with on-board storage and compute?",
        "options": ["Snowcone", "Snowball Edge", "Snowmobile", "S3 Glacier"],
        "correct_index": 1,
        "explanation": "Move the mass, Partha. Snowball Edge devices can transport massive amounts of data out of or into AWS when the internet is too slow or unavailable."
    },
    {
        "domain": "Domain 3: Cloud Technology",
        "question": "Which storage service provides high-performance block storage for Amazon EC2 instances?",
        "options": ["Amazon S3", "Amazon EFS", "Amazon EBS", "Amazon Storage Gateway"],
        "correct_index": 2,
        "explanation": "Bind it tight, Partha. Elastic Block Store (EBS) provides persistent block-level storage volumes for use with EC2, similar to a physical hard drive."
    },

    # Domain 4: Billing
    {
        "domain": "Domain 4: Billing",
        "question": "Which AWS Support Plan is the first tier that provides access to the full set of Trusted Advisor checks?",
        "options": ["Basic", "Developer", "Business", "Enterprise"],
        "correct_index": 2,
        "explanation": "Level up your support, Partha. The Business and Enterprise support plans provide the full set of Trusted Advisor checks (Basic/Developer only provide core checks)."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which AWS Support Plan provides a Dedicated Technical Account Manager (TAM)?",
        "options": ["Developer", "Business", "Enterprise On-Ramp", "Enterprise"],
        "correct_index": 3,
        "explanation": "Secure your guide, Partha. Only the Enterprise support plan provides a dedicated TAM to help you plan and build using best practices."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which tool allows you to visualize, understand, and manage your AWS costs and usage over time?",
        "options": ["AWS Pricing Calculator", "AWS Cost Explorer", "AWS Budgets", "AWS Trusted Advisor"],
        "correct_index": 1,
        "explanation": "Review the past, Partha. Cost Explorer allows you to see historical costs, forecast future costs, and identify trends in your AWS usage."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which AWS billing feature allows you to receive a discount for using multiple accounts under one organization?",
        "options": ["Service Control Policies", "Consolidated Billing", "Resource Tagging", "Savings Plans"],
        "correct_index": 1,
        "explanation": "Consolidate your strength, Partha. Consolidated billing allows you to combine the usage from all accounts in an AWS Organization to reach volume discount tiers faster."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "A user wants to set an alert that triggers when their monthly spend exceeds $100. Which service should they use?",
        "options": ["AWS Cost Explorer", "AWS Budgets", "AWS Trusted Advisor", "AWS Config"],
        "correct_index": 1,
        "explanation": "Set your limits, Partha. AWS Budgets allows you to set custom cost and usage budgets and receive notifications when you exceed (or are forecasted to exceed) your thresholds."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which tool would you use to estimate the cost of moving an on-premises workload to AWS before actually doing it?",
        "options": ["AWS Cost Explorer", "AWS Pricing Calculator", "AWS Budgets", "AWS Marketplace"],
        "correct_index": 1,
        "explanation": "Calculate the journey, Partha. The AWS Pricing Calculator is used to estimate the cost of AWS services based on your expected architecture and usage."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which AWS Free Tier category contains services that do not expire after the first 12 months?",
        "options": ["12-Month Free", "Always Free", "Trials", "Premium"],
        "correct_index": 1,
        "explanation": "Know what lasts, Partha. The 'Always Free' category includes services like AWS Lambda (1M requests) and Amazon DynamoDB (25GB) that stay free indefinitely within limits."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which pricing model offers a consistent discount (up to 72%) on EC2 and Fargate in exchange for a commitment to a consistent amount of compute usage (e.g., $/hour) for 1 or 3 years?",
        "options": ["Reserved Instances", "Savings Plans", "Spot Instances", "Dedicated Instances"],
        "correct_index": 1,
        "explanation": "Commit to the path, Partha. Savings Plans are a flexible pricing model that offers low prices on AWS compute usage in exchange for a commitment to a specific $/hour rate for 1 or 3 years."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "What is the primary benefit of 'Consolidated Billing'?",
        "options": ["It increases security", "Multiple accounts get one bill and can share volume discounts", "It replaces IAM", "It automatically optimizes EC2 instances"],
        "correct_index": 1,
        "explanation": "Simplify the complexity, Partha. Consolidated billing combines the bills for all accounts in an organization and aggregates usage to help qualify for volume discounts."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Where can you go to find, buy, and immediately start using software (like Firewalls or pre-configured AMIs) that runs on AWS?",
        "options": ["AWS Service Catalog", "AWS Marketplace", "AWS Artifact", "AWS App Mesh"],
        "correct_index": 1,
        "explanation": "Visit the bazaar, Partha. AWS Marketplace is a digital catalog where you can find third-party software products to run on your AWS infrastructure."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which of the following is most likely to reduce the Total Cost of Ownership (TCO) when moving to AWS?",
        "options": ["Managing your own physical servers", "Highly manual deployment processes", "Automation and Economies of Scale", "Increasing upfront CapEx"],
        "correct_index": 2,
        "explanation": "Focus on the goal, Partha. AWS reduces TCO by using automation, reducing the need for physical data center staff, and passing on savings through massive economies of scale."
    },
    {
        "domain": "Domain 4: Billing",
        "question": "Which AWS Support Plan includes a 15-minute response time for business-critical system failures?",
        "options": ["Basic", "Developer", "Business", "Enterprise"],
        "correct_index": 3,
        "explanation": "Seek the fastest help, Partha. The Enterprise support plan offers a < 15-minute response time for business-critical system failures (Business plan is < 1 hour)."
    }
]

async def seed_data():
    logger.info("Seeding curated CLF-C02 question bank...")
    await init_db()
    
    async with AsyncSessionLocal() as session:
        count = 0
        for q in QUESTION_BANK:
            # Prepare data field as JSON string
            q_data = {
                "question": q["question"],
                "options": q["options"],
                "correct_index": q["correct_index"],
                "explanation": q["explanation"]
            }
            
            new_entry = QuestionBank(
                domain=q["domain"],
                question_data=json.dumps(q_data),
                is_used=0
            )
            session.add(new_entry)
            count += 1
            
        await session.commit()
    
    logger.info(f"Successfully seeded {count} exam-grade questions into the vault.")

if __name__ == "__main__":
    asyncio.run(seed_data())
