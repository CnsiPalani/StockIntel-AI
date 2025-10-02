from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns

def stock_price_correlation(df):
    # 4 - Stock Price Correlation ---
    all_df = df.sort_values(['Ticker', 'date'])
    pivot_df = all_df.pivot(index='date', columns='Ticker', values='close').dropna()

    corr_matrix = pivot_df.corr()

    st.markdown("---")
    st.subheader("Stock Price Correlation Matrix")

    # Heatmap for correlation matrix
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_matrix, ax=ax, cmap='coolwarm', center=0, annot=False, cbar_kws={"shrink": .8})
    ax.set_title('Stock Price Correlation Matrix')
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    st.pyplot(fig)