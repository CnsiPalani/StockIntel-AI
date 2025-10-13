from glob import glob
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
from market_summary import preprocess_data


def sector_wise(df):
    # 3 - Sector-wise Performance ---

    # Load sector mapping CSV
    # 
    sector_map_path = 'C:\\Users\\Python\\Sector_data.csv'
    sector_df = pd.read_csv(sector_map_path)  # columns: Ticker, Sector
    summary_df = df
    # Clean up Ticker columns for matching
    sector_df['Ticker'] = sector_df['Ticker'].astype(str).str.strip()
    summary_df['Ticker'] = summary_df['Ticker'].astype(str).str.strip()

    # Merge sector info with summary_df
    summary_sector_df = pd.merge(summary_df, sector_df, on='Ticker', how='left')

    # Drop rows with missing sector (optional, or fill with 'Unknown')
    summary_sector_df['Sector'] = summary_sector_df['Sector'].fillna('Unknown')

    # Calculate average yearly return per sector
    sector_perf = summary_sector_df.groupby('Sector', as_index=False)['Yearly Return'].mean()

    # Sort by performance
    sector_perf = sector_perf.sort_values('Yearly Return', ascending=False)

    
    st.subheader("📈  Top 10 Sector-wise Performance")
    # Bar chart for sector performance
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sector_perf['Sector'], sector_perf['Yearly Return'], color='teal')
    ax.set_xlabel('Sector')
    ax.set_ylabel('Average Yearly Return')
    ax.set_title('Average Yearly Return by Sector')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Interactive sector selection
    sector_list = sector_perf['Sector'].tolist()
    selected_sector = st.selectbox('Select a sector to view stock details:', sector_list)

    # Show stock details for selected sector
    st.markdown(f"#### Stocks in {selected_sector} sector")
    sector_stocks = summary_sector_df[summary_sector_df['Sector'] == selected_sector][['Ticker', 'Yearly Return']]
    st.dataframe(sector_stocks, use_container_width=True)

    # Show sector performance table
    st.markdown("---")
    st.subheader("Sector-wise Performance")
    st.dataframe(sector_perf, use_container_width=True)