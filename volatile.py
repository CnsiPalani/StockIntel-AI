from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
from market_summary import preprocess_data, load_data

def volatile(df):
    # 1 --- Volatility Analysis ---
    volatility = []
    for ticker, group in df.groupby('Ticker'):
        group = group.sort_values('date')
        group['Prev Close'] = group['close'].shift(1)
        group['Daily Return'] = (group['close'] - group['Prev Close']) / group['Prev Close']
        std_dev = group['Daily Return'].std()
        volatility.append({'Ticker': ticker, 'Volatility': std_dev})

    vol_df = pd.DataFrame(volatility).dropna().sort_values('Volatility', ascending=False)
    top10_vol = vol_df.head(10)


    st.markdown("---")
    st.subheader("Top 10 Most Volatile Stocks")
    st.dataframe(top10_vol, use_container_width=True)

    # Bar chart for volatility
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(top10_vol['Ticker'], top10_vol['Volatility'], color='orange')
    ax.set_xlabel('Stock Ticker')
    ax.set_ylabel('Volatility (Std Dev of Daily Returns)')
    ax.set_title('Top 10 Most Volatile Stocks (Past Year)')
    plt.xticks(rotation=45)
    st.pyplot(fig)