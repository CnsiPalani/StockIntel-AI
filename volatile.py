from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
from market_summary import preprocess_data

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


    

    # Bar chart for volatility
    fig, ax = plt.subplots(figsize=(10, 4))
    # Generate a color palette with as many colors as there are bars
    colors = plt.cm.tab10(np.linspace(0, 1, len(top10_vol)))
    ax.bar(top10_vol['Ticker'], top10_vol['Volatility'], color=colors)
    ax.set_xlabel('Stock Ticker')
    ax.set_ylabel('Volatility (Std Dev of Daily Returns)')
    ax.set_title('Top 10 Most Volatile Stocks (Past Year)')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.subheader("Top 10 Most Volatile Stocks")
    st.dataframe(top10_vol, use_container_width=True)


def volatile1(df):
    # 1 --- Volatility / Risk Analysis ---
    volatility = []
    for ticker, group in df.groupby('Ticker'):
        group = group.sort_values('date')
        # Calculate Previous day returns
        group['Prev Close'] = group['close'].shift(1)
        # Calculate Daily returns
        group['Daily Return'] = (group['close'] - group['Prev Close']) / group['Prev Close']
        std_dev = group['Daily Return'].std()
        volatility.append({'Ticker': ticker, 'Volatility': std_dev})

    vol_df = pd.DataFrame(volatility).dropna().sort_values('Volatility', ascending=False)
    top10_vol = vol_df.head(10)


    # Two columns and two rows layout
    col1, col2 = st.columns(2)
    # First row with two columns
    with col1:
        st.markdown("---")
        st.subheader("Top 10 Most Volatile Stocks Bar Chart")

        # Bar chart for volatility /
    fig, ax = plt.subplots(figsize=(10, 4))
    # Generate a color palette with as many colors as there are bars
    colors = plt.cm.tab10(np.linspace(0, 1, len(top10_vol)))
    ax.bar(top10_vol['Ticker'], top10_vol['Volatility'], color=colors)
    ax.set_xlabel('Stock Ticker')
    ax.set_ylabel('Volatility (Std Dev of Daily Returns)')
    ax.set_title('Top 10 Most Volatile Stocks (Past Year)')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    with col2:
        # Box plot for volatility
        st.markdown("---")
        st.subheader("Volatility Distribution Box Plot")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.boxplot(y=vol_df['Volatility'], ax=ax2, color='lightblue')
        ax2.set_title('Distribution of Stock Volatilities')
        st.pyplot(fig2)
    # Second row with one column spanning full width
    col1, col2 = st.columns(2)
    with col1:
        # Heatmap for volatility
        st.markdown("---")
        st.subheader("Volatility Heatmap")
        vol_pivot = vol_df.pivot_table(index='Ticker', values='Volatility')
        fig3, ax3 = plt.subplots(figsize=(6, 8))
        sns.heatmap(vol_pivot, annot=True, cmap='Reds', cbar_kws={'label': 'Volatility'}, ax=ax3)
        ax3.set_title('Stock Volatility Heatmap')
        st.pyplot(fig3)