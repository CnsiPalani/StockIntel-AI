from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
from market_summary import preprocess_data


def cumulative_return(df):
    # 2 - Cumulative Return Over Time ---
    # Calculate daily returns and cumulative returns for each stock
    all_df = df.sort_values(['Ticker', 'date'])
    all_df['Prev Close'] = all_df.groupby('Ticker')['close'].shift(1)
    all_df['Daily Return'] = (all_df['close'] - all_df['Prev Close']) / all_df['Prev Close']
    all_df['Daily Return'] = all_df['Daily Return'].fillna(0)

    # Cumulative sum return for each stock
    all_df['Cumulative Return'] = all_df.groupby('Ticker')['Daily Return'].cumsum()

    # Get last cumulative return for each stock
    last_cum_return = all_df.groupby('Ticker').tail(1)[['Ticker', 'Cumulative Return']]
    top5_cum = last_cum_return.nlargest(5, 'Cumulative Return')['Ticker'].tolist()

    # Filter data for top 5 stocks
    top5_df = all_df[all_df['Ticker'].isin(top5_cum)]

    # Plot cumulative return line chart
    st.subheader("📈 Cumulative Return for Top 5 Performing Stocks")

    fig, ax = plt.subplots(figsize=(10, 5))
    for ticker in top5_cum:
        stock_data = top5_df[top5_df['Ticker'] == ticker]
        ax.plot(stock_data['date'], stock_data['Cumulative Return'], label=ticker)
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Return')
    ax.set_title('Cumulative Return Over Time (Top 5 Stocks)')
    plt.xticks(rotation=45)
    ax.legend()
    st.pyplot(fig)