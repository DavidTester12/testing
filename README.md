# Regional Inventory Sync Service

This microservice is responsible for aggregating and synchronizing regional warehouse inventory levels across various endpoints. It polls local databases and pushes updates to the central API gateway.

**Note:** This repository is currently for internal testing purposes and staging environments only. Do not deploy to production.

## Setup

1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the service:
   `python main.py`
