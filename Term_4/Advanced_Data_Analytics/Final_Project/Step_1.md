**Step-by-Step: Initializing the Databricks Environment**

The following steps outline the procedure for establishing and configuring the Databricks workspace for all team members.

**Step 1: Establish the Workspace**
1. Databricks operates on top of primary cloud providers such as Azure, AWS, or GCP.
2. Navigate to the designated cloud portal (e.g., an institutional student cloud account).
3. Search for the "Databricks" service and initiate the creation of a new workspace.

**Step 2: Provision a Compute Cluster**
1. A compute cluster is required to process and execute code within the workspace.
2. Locate and select the "Compute" tab on the left-hand navigation sidebar.
3. Click the "Create Compute" button.
4. Configure a standard, lightweight cluster, ensuring the selection of a Databricks Runtime that includes Machine Learning capabilities (indicated by "ML" in the runtime dropdown).
5. Cost-Optimization Measure: Set the cluster to automatically terminate after a specified period of inactivity (e.g., 30 to 60 minutes) to conserve available cloud credits.

**Step 3: Integrate Version Control (GitHub)**
1. Version control integration is necessary to maintain a centralized and versioned codebase.
2. Navigate to "Settings", select "Linked accounts", and authenticate the project's GitHub account using a Personal Access Token (PAT).
3. Proceed to the "Workspace" tab, select "Repos", and clone the designated GitHub repository.
4. Once configured, all team members will have the capability to collaborate within the Databricks environment and push commits directly to the shared repository.

**Step 4: Upload Initial Datasets (DBFS)**
1. Ensure the necessary raw datasets are downloaded to a local machine.
2. Within the Databricks interface, navigate to "Catalog" (or "Data") and select "Add Data".
3. Upload the respective CSV files directly into the Databricks File System (DBFS) to make them accessible for the data pipeline.
