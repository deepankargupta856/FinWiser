# 📊 Financial Data Scraping, Analysis & Dashboard  

This project automates the extraction, processing, and analysis of stock market data from **Yahoo Finance**. It includes data cleaning, ETL, and analytical insights, culminating in an interactive **Streamlit dashboard** to visualize key stock metrics.  

## 🚀 Features  

### 🔹 Data Collection  
- Scraped stock market data from **Yahoo Finance** using **Selenium** and **BeautifulSoup**.  
- Automated data retrieval for multiple companies/stocks.  

### 🔹 Data Processing & Storage  
- Cleaned and processed raw data using **Pandas** and **NumPy**.  
- Stored cleaned data in an **AWS RDS OLTP (Online Transaction Processing) database**.  

### 🔹 ETL & Feature Engineering  
- Performed **ETL (Extract, Transform, Load)** using Python and Pandas.  
- Engineered additional financial features for deeper insights.  
- Uploaded transformed data to an **AWS RDS OLAP (Online Analytical Processing) database**.  

### 🔹 Exploratory Data Analysis (EDA)  
- Extracted and analyzed stock data to identify **market trends, liquidity, and stock performance**.  

### 🔹 Interactive Dashboard  
Built a **Streamlit-based dashboard** with two sections:  
1. **Overall Market Analysis**:  
   - Identifies **undervalued, liquid, blue-chip, and most actively traded stocks**.  
   - Displays percentage breakdowns for each category.  
2. **Stock-Specific Data**:  
   - Users can select a company to view its detailed stock information.  

### 🔹 Deployment  
- Hosted the **Streamlit dashboard** for easy access and visualization.  

## 🛠️ Tech Stack  
- **Python** (Pandas, NumPy, Selenium, BeautifulSoup)  
- **AWS RDS** (OLTP & OLAP Databases)  
- **Streamlit** (Dashboard & Deployment)  

