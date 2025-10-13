from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns



# Calculate Yearly Return for each stock (last close - first close) / first close
def preprocess_data(df):
    returns = []
    for ticker, group in df.groupby('Ticker'):
        group = group.sort_values('date')
        first_close = group['close'].iloc[0]
        last_close = group['close'].iloc[-1]
        yearly_return = (last_close - first_close) / first_close
        returns.append({'Ticker': ticker, 'Yearly Return': yearly_return})
    returns_df = pd.DataFrame(returns)
    # print(returns_df)
    # Merge returns with one row per ticker (latest data)
    latest_data = df.sort_values('date').groupby('Ticker').tail(1)
    # print(latest_data)
    summary_df = pd.merge(latest_data, returns_df, on='Ticker')
    # print(summary_df)
    return summary_df


def market_summary(df):
    # Top 10 Green Stocks (highest yearly return)
    top10_green = df.nlargest(10, 'Yearly Return')[['Ticker', 'Yearly Return']]
    # Top 10 Loss Stocks (lowest yearly return)
    top10_loss = df.nsmallest(10, 'Yearly Return')[['Ticker', 'Yearly Return']]
    # Market Summary
    green_count = (df['Yearly Return'] > 0).sum()
    red_count = (df['Yearly Return'] <= 0).sum()
    avg_price = df['close'].mean()
    avg_volume = df['volume'].mean()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 10 Green Stocks")
        st.dataframe(top10_green, use_container_width=True)
    with col2:
        st.subheader("Top 10 Loss Stocks")
        st.dataframe(top10_loss, use_container_width=True)
   
    st.markdown("---")
    st.subheader("Market Summary")
    col3, col4, col5, col6 = st.columns(4)
    col3.metric("Green Stocks", green_count)
    col4.metric("Red Stocks", red_count)
    col5.metric("Avg. Price", f"{avg_price:.2f}")
    col6.metric("Avg. Volume", f"{avg_volume:.0f}")





