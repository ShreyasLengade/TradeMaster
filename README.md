![Project Banner](https://github.com/ShreyasLengade/Github-Images/blob/ef29d605ec72d22236a2485cb6164f2886873ed4/Trade%20Master.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Introduction

Welcome to the Trade Master Project! The project was developed to provide different features of data analytics and machine learning for stock trading, portfolio optimisation and generate backtest trading strategies. <br>
<b style="color: red;">The project is hosted on Google Cloud and may experience a cold start delay. Please allow up to 30 seconds to 1 minute for the website to fully load. Thank you for your patience.</b><br>
<h3> Link to website: </h3> <a href="https://trade-master-21758012479.asia-south1.run.app/">Click here</a>

## Features

# Trade Master Project

## Overview
Trade Master provides a comprehensive suite of tools for stock and ETF analysis, catering to both novice and experienced investors. This platform offers in-depth visualizations, statistical analysis, portfolio optimization, and machine learning-based predictions, empowering users to make data-driven investment decisions.

---

## Features

### **1. Popular Stocks Dashboard (Home)**
- Displays the stock prices of the top 6 tech companies for the current day.
- Offers users a quick overview of key stock market leaders.

---

### **2. Daily Return Analysis**
The Daily Return Analysis module enables users to evaluate the historical performance of selected ETFs or stocks through interactive tools and visualizations.

#### Features:
- **Dropdown Selection**:
  - A dynamic dropdown menu allows users to select from a range of ETFs and stocks, such as SPY (S&P 500 Index ETF), QQQ (Nasdaq 100 Index ETF), and others.
  
- **Return Summary**:
  - Displays key metrics for the selected stock/ETF, including:
    - Current close price
    - 1-month, 3-month, 1-year, and 3-year returns (percentage)
    - Compound Annual Growth Rate (CAGR)
    - Annualized volatility

- **Price Chart**:
  - A line chart visualizes the historical price trends over the years, providing insights into long-term performance and growth patterns.

- **Volatility Clusters**:
  - A scatter plot of daily percentage price changes highlights periods of high volatility to help users identify riskier timeframes.

- **Return Distribution**:
  - A histogram illustrates the distribution of daily percentage returns, while a box plot provides a summary of outliers, medians, and quartiles.

- **Quantile-Quantile (Q-Q) Plot**:
  - Visualizes how closely the distribution of daily percentage returns aligns with a theoretical Gaussian (normal) distribution.

- **Kolmogorov-Smirnov (KS) Test**:
  - Statistically evaluates whether the daily percentage price changes conform to a Normal Gaussian Distribution.
  - Provides:
    - KS statistic value
    - p-value
    - Conclusion about normality (based on a threshold of p < 0.05)

#### Key Insights:
This module helps users:
1. Evaluate **recent and long-term performance**.
2. Assess **volatility and risk**.
3. Identify **trends** and significant market events.
4. Validate the distribution of returns for informed decision-making.

---

### **3. Stock Return Comparison**
- Users can select up to four stocks from a dropdown menu and compare their financial metrics, including:
  - Daily return distribution
  - 60-day rolling volatility
  - 60-day rolling Sharpe ratio
  - 60-day rolling Sortino volatility
  - 60-day rolling Sortino ratio
- This feature enables comparative analysis to identify outperforming stocks.

---

### **4. Portfolio Optimizer**
- Allows users to select a minimum of 5 stocks from the dropdown menu.
- Extracts historical stock returns (including dividends) from January 2020.
- Constructs optimized portfolios based on user-defined parameters to maximize returns or minimize risk.

---

### **5. Cluster Analysis**
- Provides tools for clustering financial data from stocks within the Dow 30 index.
- Users can:
  - Select input features for clustering.
  - Visualize resulting clusters in a 3D graph for deeper insights into stock relationships.

---

### **6. Backtest Trading Strategy**
- Simulates trading strategies using historical stock data.
- Helps traders:
  - Analyze the performance and risk of a strategy before committing capital.
  - Understand whether a strategy that worked well in the past is likely to succeed in the future.

---

### **7. ML Predictions**
- Allows users to select machine learning models, stocks, input features, and model parameters from a dropdown menu.
- Predicts the magnitude or direction of stock price changes for the next trading day using advanced machine learning techniques.

---

## How to Use
- **Start with the Popular Stocks Dashboard** to get a quick overview of top tech companies.
- Dive deeper into **Daily Return Analysis** for historical performance, volatility, and statistical insights.
- Compare multiple stocks using the **Stock Return Comparison** feature to identify trends and outperformers.
- Use the **Portfolio Optimizer** to build diversified investment portfolios.
- Leverage **Cluster Analysis** to understand the grouping and similarities among stocks.
- Test and refine your trading strategies with the **Backtest Trading Strategy** feature.
- Predict stock movements using the **ML Predictions** tool for advanced decision-making.

---

This project serves as a complete toolset for stock and ETF analysis, combining traditional financial analysis with cutting-edge machine learning techniques. Perfect for investors, traders, and analysts looking to make informed decisions in the financial markets.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ShreyasLengade/TradeMaster.git
    ```

2. Navigate to the project directory:
    ```bash
    cd TradeMaster
    ```

3. Install docker and then run following command:
    ```bash
    docker build -t image_name  // image_name = whatever image name you want to have
    ```
4. Run the docker container from docker desktop app.

## Examples

Below are some examples of the visualizations and analysis you can perform with this project:

1. **Home page**
  ![image](https://github.com/user-attachments/assets/e0111eda-d6a5-46ed-972f-ab68d7a3dd4a)

2. **Portfolio Optimiser**
    ![image](https://github.com/user-attachments/assets/5585ca6c-b054-4a67-80f7-d3998b74ed2d)
   ![image](https://github.com/user-attachments/assets/7c9aeb17-76e8-4e21-900a-7c460d573874)
  ![image](https://github.com/user-attachments/assets/96a47cd6-ef5c-4de4-a524-f3566a01087a)
![image](https://github.com/user-attachments/assets/490bcd76-bb4c-48ef-9cf1-f2c7b2b5ecc0)



---

Thank you for checking out my project! If you find it useful, please give it a star ⭐ on GitHub.
