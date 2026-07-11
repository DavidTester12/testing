# Regional Inventory Sync Service

This microservice is responsible for aggregating and synchronizing regional warehouse inventory levels across various endpoints. It polls local databases and pushes updates to the central API gateway.

# **Important Note:** This repository and its contents are currently for internal testing purposes and staging environments only. Specifically, this is a **test for accuracy** regarding our automated deployment pipelines, configuration parsing, and environment monitoring tools. Do not deploy to production.

## Setup

1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the service:
   `python main.py`
