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

- **Popular Stocks Dashboard(Home)**: In this section you can check top 6 tech companies stock prices for present day.
- **Daily Return Analysis**: For the stock selected from the dropdown below, users will be presented with a summary of the stock return, a price chart, the daily percentage price change over time (highlighting volatility clusters), a histogram of daily percent return, a QQ plot, and a KS statistics test. This test assesses whether the daily percentage price changes conform to a Normal Gaussian Distribution.
- **Stock Return Comparison**: For the four stocks selected from the dropdown below, users can compare metrics including: daily return distribution, 60-day rolling volatility, 60-day rolling Sharpe ratio, 60-day Sortino volatility, and 60-day rolling Sortino ratio.
- **Portfolio Optimiser**: Select a minimum of 5 stocks from the dropdown list below. This application will extract stock returns, including dividends, from January 2020 and construct portfolios with the following characteristics:
- **Cluster Analysis**: In this tab, users can perform cluster analysis on the financial data of stocks within the Dow 30 index. They can select the input features for the analysis and visualize the resulting clusters in a 3D graph.
- **Backtest Trading Strategy**: Backtesting allows traders to simulate a trading strategy using historical data, generating results and analyzing risk before committing any actual capital. The underlying theory is that a strategy that worked well in the past is likely to succeed in the future. Conversely, a strategy that performed poorly in the past is likely to do so in the future.
- **ML Predictions**: From the dropdown menu below, users can select various ML models, stocks, input features, and model parameters to predict the magnitude or direction of stock price changes for the next day.

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

Thank you for checking out our project! If you find it useful, please give it a star ⭐ on GitHub.
