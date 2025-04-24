# Microsoft Fabric Medallion Architecture Project

## Overview

This project implements an end-to-end data pipeline that automatically fetches CSV data from GitHub, processes it through various stages in a medallion architecture, and creates visualizations in Power BI. The pipeline leverages Microsoft Fabric, Python, and PySpark to deliver a complete data processing solution.

## Architecture

The pipeline follows a medallion architecture with the following layers:
- **Raw Lakehouse**: Initial data storage of CSV files
- **Bronze Lakehouse**: Structured table format of the raw data
- **Silver Lakehouse**: Processed data in Delta format
- **Semantic Layer**: Business logic and metrics for visualization

## Components

### 1. Data Ingestion
- Python script running in Fabric notebook identifies all CSV files from GitHub repository

### 2. Data Processing
- Lookup activity fetches CSV filename from Json file store in the Raw Lakehouse
- ForEach activity processes each file identified in the JSON
- Copy activity moves data from GitHub URLs to Bronze Lakehouse in table format

### 3. Data Transformation
- PySpark scripts transform data from Bronze Lakehouse
- Transformed data is stored in Silver Lakehouse using Delta format

### 4. Data Visualization
- Semantic model built on top of Silver Lakehouse
- Power BI visualizations connected to semantic model

## Tools Used

- **Microsoft Fabric**: Cloud analytics platform for end-to-end data processing
- **Python**: Used for initial data discovery and processing
- **PySpark**: Used for data transformation at scale
- **Power BI**: Business intelligence tool for visualization

## Implementation

Detailed implementation steps with screenshots are included in this repository:

1. Initial setup and configuration
2. Python script execution in Fabric notebook
3. Data pipeline execution
4. Data transformation with PySpark
5. Semantic model development
6. Power BI visualization design

## Getting Started

### Prerequisites
- Microsoft Fabric account
- GitHub repository with CSV data
- Power BI Desktop

### Setup Instructions
1. Clone this repository
2. Configure Microsoft Fabric workspace
3. Update configuration files with your GitHub repository details
4. Execute the pipeline following the steps in the documentation

## Screenshots

Screenshots of the entire process are 
![screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_1.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_2.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_3.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_4.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_5.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_6.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_7.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_8.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_9.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_10.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_11.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_12.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_13.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_14.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_15.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_16.png)
! [screenshots](https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/blob/main/Screenshort/image_17.png)



## Future Enhancements
- Add data quality checks
- Implement automated testing
- Add incremental load capabilities
- Expand semantic model with additional metrics
