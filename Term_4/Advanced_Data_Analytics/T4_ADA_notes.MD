# Advanced Data Analytics - Term 4 - DAMO - 630 - 4
**Prof.Hamed Afshari** ; *hamed.afshari@unfc.ca* ; *h.h.afshari@gmail.com* \
This Readme is a summary of all the works and classnotes of this subject during my course period.

## Week_1
*06 April 2026, 3.45PM - 5.45PM* \
1. Class Cancelled due to holiday, received recorded video class instead. \
2. Install Databricks Free tier

### W1.1 Keynotes from the video and presentation file.
1. **The Foundations of Big Data & Scalability:** Advanced Data Analytics (ADA) focuses on extracting insights from massive, complex datasets. To understand big data, we use the "4 Vs" framework:\
1.1 Volume: High data quantities require massive storage and strong infrastructure.\
1.2 Velocity: Rapid, time-sensitive data is crucial for things like fraud detection and online recommendations.\
1.3 Variety: Data must be integrated across diverse formats, including text, audio, images, and structured data.\
1.4 Veracity: High-stakes analytics demand strict data quality and reliability. \
<br />
Traditional systems struggle with this exponential data growth. The solution is scalability, which is a system's ability to handle increasing amounts of work by adding resources without losing performance.Scaling-Out (Horizontal Scaling): Adding more resources to a distributed environment, such as adding more web servers to support a busy site.Scaling-Up (Vertical Scaling): Adding more resources to an existing deployment, such as installing more RAM into a single server.\

2. **Apache Hadoop Framework:** To manage big data horizontally, we use distributed frameworks like Apache Hadoop. Hadoop is an open-source framework that processes large datasets across clusters of computers.<br />
*Key Components of Hadoop:* <br />
2.1 HDFS (Hadoop Distributed File System): A distributed storage system that makes copies of your data across multiple systems. This makes the system fault-tolerant, meaning data is never lost even if a node crashes.<br />
2.2 MapReduce: A batch processing model. The "Mapper" phase filters and sorts the data, while the "Reduce" phase summarizes it.\
2.3 YARN: A tool that manages cluster resources and schedules jobs.\
2.4 Spark: An in-memory engine used for batch processing, machine learning, and stream analytics.

3. **Cloud Analytics:** Cloud analytics platforms process massive datasets using internet-based services instead of traditional, on-premise servers. This goes beyond basic storage to include real-time insights, machine learning, and data visualization. \
**Top Benefits of Cloud Analytics:** \
3.1 Elastic Scalability: Resources automatically adjust to fit your current workload.\
3.2 Reduced IT Costs: Eliminates capital investments in hardware and ongoing maintenance.\
3.3 Speed & Agility: Automated reports and real-time dashboards speed up business decisions.\

**3.4 Cloud Service Models:** \
3.4.1 SaaS (Software as a Service): Targeted at end-users where the provider manages everything (e.g., Tableau Cloud, Power BI).\
3.4.2 PaaS (Platform as a Service): Targeted at developers where the user manages apps and data, but the provider manages infrastructure and runtime (e.g., Google BigQuery).\
3.4.3 IaaS (Infrastructure as a Service): Targeted at IT admins who manage everything from the OS up, while the provider supplies only the bare infrastructure (e.g., AWS EC2).\

**3.5 The "Big 3" Cloud Providers:** \
3.5.1 Amazon Web Services (AWS): Features tools like Redshift (data warehouse) and Glue (data preparation).\
3.5.2 Microsoft Azure: Features Synapse Analytics and Power BI.\
3.5.3 Google Cloud Platform (GCP): Features BigQuery and Vertex AI.

4. **Real-World Applications of Advanced Analytics**\
4.1 Mining Data Streams: Continuous data from sensors, images, or internet traffic is processed in real-time by Data-Stream-Management Systems. This is used for disease tracking and DoS attack monitoring, though it faces challenges with limited memory.\
4.2 Recommendation Systems: These predict a user's preference for items like movies or products. They rely on Content-Based Filtering (recommending items with similar features) and Collaborative Filtering (finding similar users or items).\
4.3 Mining Social Networks: Social relationships are analyzed by representing them as graphs, utilizing the formal structure $nodes=people,edges=relationships$. Analysts use community detection and triangle counting to measure trust and local connectivity.

## Week_2
*13 April 2026, 3.45 PM - 5.45 PM* 

### W2.1 To do / keynotes
1. Submit class activity by sunday. \
2. Install / try GCP by next class. \
3. Final presentation will be online. \
4. Project should cover 3 modules - databricks, sentiment analysis.

### W1.1 Classnotes (Recap)
**A. Scalability and Bigdata Challenges:** \
1. Volume of data is increasing exponentially over time. (90% of world's data was created in last 2 years). We have 2 solutions to manage this. \
1.1 Big Data Processing (In-House): \
You need actual physical servers, be present at the place where servers are accesible, inaccesible from any other parts of the world, multiple higher ups involved in messy accesibility process, lots of communication, storage issues or limitations, very costly to set it up, very costly to manage, maintain, upgrade or replace, cooling systems etc.\
1.1.1 Hadoop (a bit older)\
1.1.2 Spark (a bit new, dividing the big data over several processors and compute to finally stich them back, This term's more focus will be on it)\
1.2 Cloud Computing:\
In, 2013-14 Amazon (AWS), Google (GCP) and Microsoft (Azure); Recently DataBricks (very easy comapred to others, like learning python) offered cloud features. \
**Scaling:** Increase or decrease the capabilities of technology used. Provides service and resource elasticity to upgrade or downgrade whenever needed. There are mainly 2 types of scaling. Let us compare it with processor types. \
1.2.1 The Hardware (The "Trucks")

| Hardware | Best For... | Analogy |
| :--- | :--- | :--- |
| **CPU** (Central Processing Unit) | General tasks, logic, and daily software. | A versatile "Manager" handling one task at a time. |
| **GPU** (Graphics Processing Unit) | Parallel tasks, gaming, and AI training. | A "Team of 1,000 Workers" doing small tasks at once. |
| **TPU** (Tensor Processing Unit) | High-speed AI math (Google-specific). | A "Specialized Factory" built for one specific product. |
<br />
1.2.2 The Scaling Strategies 

| Feature | **Vertical Scaling** (Scale Up) | **Horizontal Scaling** (Scale Out) |
| :--- | :--- | :--- |
| **The Action** | Adding more power to **one** machine. | Adding **more** machines to a cluster. |
| **CPU Example** | Upgrading from a 4-core to a 64-core CPU. | Connecting 10 servers to handle web traffic. |
| **GPU/TPU Example** | Swapping an old GPU for a high-end 80GB model. | Linking 1,000 TPUs to train a model like Gemini. |
| **The "Wall"** | Limited by physical chip size and heat. | Virtually unlimited; just keep adding more nodes. |
| **Complexity** | Simple; usually requires no code changes. | Complex; requires "distributed" software. |
<br />

The Bottom Line:
A CPU is scaled vertically when a single application becomes too demanding for its current resources. GPUs or TPUs are scaled horizontally when a task, such as AI training, is too large for any single machine.

### W2.2 Classnotes
1. Installed DataBricks.
2. 
