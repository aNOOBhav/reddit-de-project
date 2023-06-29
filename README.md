# reddit-de-project

This project aims to create a simple end to end batch processing data pipeline which extracts data from Reddit API and build a Quicksight dashboard for analytics
The orchestration is managed using MAGE - www.mage.ai which is a data management platform for creating DAG flows, similar to Airflow, Kedro, DAGster and Prefect
For more information, you can read docs - https://docs.mage.ai/introduction/overview


## Data flow 

Reddit API -> AWS S3 - Mage on EC2 -> AWS S3 -> Glue Crawler -> AWS Athena -> AWS Quicksight
Refer to the HLD for a detailed architecture
