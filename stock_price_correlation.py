from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
    
def stock_price_correlation(df):
    # 4 - Stock Price Correlation ---
    # Select top ten stocks by average volume
    if 'volume' in df.columns:
        top_tickers = df.groupby('Ticker')['volume'].mean().nlargest(10).index.tolist()
        df = df[df['Ticker'].isin(top_tickers)]
    all_df = df.sort_values(['Ticker', 'date'])
    # Calculate daily percentage returns for each stock
    all_df['pct_return'] = all_df.groupby('Ticker')['close'].pct_change() * 100
    # Pivot to get percentage returns for each stock as columns
    pivot_df = all_df.pivot(index='date', columns='Ticker', values='pct_return').dropna()

    corr_matrix = pivot_df.corr()

    # Interactive heatmap for correlation matrix using Plotly
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale='RdBu',
        zmin=-1,
        zmax=1,
        colorbar=dict(title='Correlation'),
        hoverongaps=False
    ))
    fig.update_layout(
        title='Stock Closing Percentage Return Correlation Matrix',
        xaxis_nticks=36,
        width=900,
        height=700
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Stock Closing Percentage Return Correlation Matrix")

    st.dataframe(corr_matrix, use_container_width=True)
    # Save correlation matrix to CSV
    corr_matrix.to_csv('correlation_matrix.csv')
    
