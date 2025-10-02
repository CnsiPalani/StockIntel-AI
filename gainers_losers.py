from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
from market_summary import preprocess_data, load_data


def gainers_losers(df):
    # 5 - Top 5 Gainers and Losers (Month-wise):
    all_df = df.sort_values(['Ticker', 'date'])
    # Ensure 'date' is datetime
    all_df['date'] = pd.to_datetime(all_df['date'])
    all_df['month'] = all_df['date'].dt.to_period('M').astype(str)

    # Calculate monthly return for each stock
    monthly_returns = []
    for (ticker, month), group in all_df.groupby(['Ticker', 'month']):
        group = group.sort_values('date')
        first_close = group['close'].iloc[0]
        last_close = group['close'].iloc[-1]
        monthly_return = (last_close - first_close) / first_close
        monthly_returns.append({'Ticker': ticker, 'Month': month, 'Monthly Return': monthly_return})
    monthly_returns_df = pd.DataFrame(monthly_returns)

    # Get sorted list of months
    months = sorted(monthly_returns_df['Month'].unique())

    st.markdown("---")
    st.subheader("Top 5 Gainers and Losers by Month")

    for month in months:
        month_df = monthly_returns_df[monthly_returns_df['Month'] == month]
        top5_gainers = month_df.nlargest(5, 'Monthly Return')
        top5_losers = month_df.nsmallest(5, 'Monthly Return')
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**{month} - Top 5 Gainers**")
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.bar(top5_gainers['Ticker'], top5_gainers['Monthly Return'], color='green')
            ax.set_ylabel('Monthly Return')
            ax.set_title(f'Top 5 Gainers ({month})')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        with col2:
            st.markdown(f"**{month} - Top 5 Losers**")
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.bar(top5_losers['Ticker'], top5_losers['Monthly Return'], color='red')
            ax.set_ylabel('Monthly Return')
            ax.set_title(f'Top 5 Losers ({month})')
            plt.xticks(rotation=45)
            st.pyplot(fig)