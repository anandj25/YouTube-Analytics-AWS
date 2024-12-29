# YouTube Ad Placement Analytics

This project develops a cloud-based YouTube analytics platform leveraging **Amazon Web Services (AWS)** to help businesses optimize their advertising strategies. By analyzing YouTube trends and viewer behavior, the platform offers insights for data-driven ad placement decisions, maximizing advertising ROI.

---

## Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [System Design and Architecture](#system-design-and-architecture)
- [Technologies Used](#technologies-used)
- [Implementation Steps](#implementation-steps)
- [Key Features](#key-features)
- [Challenges](#challenges)
- [Links and References](#links-and-references)

---

## Introduction

YouTube, the second most visited website globally, offers significant potential for businesses to connect with customers. However, selecting the right channels or videos for ad placements is challenging. This project addresses this problem by creating a data-driven analytics platform using AWS services to extract, transform, and analyze YouTube data.

---

## Objectives

1. **Data Management**: Extract raw data from the YouTube API and store it in AWS S3.
2. **ETL Automation**: Streamline data transformation using AWS Glue and Lambda.
3. **Dashboard Development**: Design an interactive dashboard with AWS QuickSight to visualize trends and inform ad placement strategies.

---

## System Design and Architecture

The system architecture involves:
1. **Data Ingestion**: Data from the YouTube API is uploaded to S3 in raw format (JSON/CSV).
2. **Data Transformation**: Lambda functions convert raw data to Parquet for querying.
3. **ETL Automation**: AWS Glue automates catalog creation and data joining.
4. **Data Analysis**: AWS Athena queries the processed data.
5. **Visualization**: AWS QuickSight builds interactive dashboards for insights.

### Architecture Diagram
![Architecture Diagram](https://github.com/anandj25/YouTube-Analytics-AWS/blob/main/AWS%20Architecture/Architecture%20Detailed.jpg)

---

## Technologies Used

- **YouTube API**: For fetching real-time YouTube data.
- **AWS S3**: Storage for raw and processed data.
- **AWS Glue**: Automates ETL processes and data cataloging.
- **AWS Lambda**: Handles data transformation (JSON to Parquet).
- **AWS Athena**: Querying transformed data.
- **AWS QuickSight**: Interactive dashboards for visualization.
- **AWS CLI**: Command-line interface for managing AWS resources.
- **Python 3.8**: For Lambda functions and ETL scripts.

---

## Implementation Steps

1. **Data Collection**:
   - Fetch data from the YouTube API (JSON/CSV formats).
   - Store raw data in an S3 bucket.
   
2. **Data Transformation**:
   - Convert JSON/CSV files to Parquet format using Lambda functions.
   - Update data types for compatibility and optimize data storage.

3. **ETL Pipeline**:
   - Create a data catalog in AWS Glue.
   - Join datasets and partition data for efficient querying.

4. **Querying**:
   - Use AWS Athena to run SQL queries on the transformed data.
   
5. **Visualization**:
   - Connect Athena to QuickSight for dashboard development.
   - Visualize trends, engagement metrics, and ad placement insights.

---

## Key Features

- **Interactive Dashboard**: Offers insights on:
  - Top viewed categories (e.g., "Entertainment," "Music").
  - Best-performing ad placement categories.
  - Regional trends in content removal and viewership.
- **Automated ETL Process**: Simplifies data preparation for analytics.
- **Scalable Cloud Infrastructure**: Built entirely on AWS, ensuring reliability and scalability.

---

## Challenges

1. **API Rate Limits**: Limited ability to update large datasets efficiently.
2. **Lambda Configuration**:
   - Created manual Lambda layers for Python 3.8 compatibility.
   - Resolved issues related to data type mismatches.
3. **Query Optimization**:
   - Managed data partitioning for efficient querying.
4. **Dataset Updates**: Limited updates to top 500 rows due to time and cost constraints.

---

## Links and References

- [AWS Documentation](https://aws.amazon.com/documentation/)
- [YouTube API Documentation](https://developers.google.com/youtube/v3/getting-started)
- [Dashboard Link (Requires Account)](https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/4e5f0d59-4fa3-430e-9c9b-9e1da61a0ea1)


