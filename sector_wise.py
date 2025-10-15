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
    #sector_df['Ticker'] = sector_df['Ticker'].astype(str).str.strip()
    sector_df['Ticker'] = sector_df['Symbol'].str.split(':').str[1].astype(str).str.strip()
    
    summary_df['Ticker'] = summary_df['Ticker'].astype(str).str.strip()

    # Merge sector info with summary_df
    summary_sector_df = pd.merge(summary_df, sector_df, on='Ticker', how='left')

    # Drop rows with missing sector (optional, or fill with 'Unknown')
    summary_sector_df['Sector'] = summary_sector_df['sector'].fillna('Unknown')

    # Calculate average yearly return per sector
    sector_perf = summary_sector_df.groupby('Sector', as_index=False)['Yearly Return'].mean()

    # Sort by performance
    sector_perf = sector_perf.sort_values('Yearly Return', ascending=False)

    
    st.subheader("📈  Top 10 Sector-wise Performance")
    # Bar chart for sector performance using Plotly for tooltips
    import plotly.express as px
    fig = px.bar(
        sector_perf,
        x='Sector',
        y='Yearly Return',
        color='Sector',
        color_discrete_sequence=px.colors.qualitative.Plotly,
        hover_data={"Sector": True, "Yearly Return": ":.2f"},
        title='Average Yearly Return by Sector',
        text='Yearly Return',
        template='plotly_white',
    )
    fig.update_traces(
        texttemplate='%{text:.2f}',
        textposition='outside',
        marker=dict(line=dict(width=1, color='black')),
    )
    fig.update_layout(
        xaxis_title='Sector',
        yaxis_title='Average Yearly Return',
        xaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True, tickangle=45),
        yaxis=dict(showline=True, linewidth=2, linecolor='black', mirror=True, gridcolor='lightgrey'),
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Segoe UI, Arial', size=14),
        margin=dict(t=60, b=120, l=60, r=30),
        showlegend=False,
    hoverlabel=dict(bgcolor='black', font_size=14, font_family='Segoe UI', font_color='white', bordercolor='black'),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Interactive sector selection
    sector_list = sector_perf['Sector'].tolist()
    selected_sector = st.selectbox('Select a sector to view stock details:', sector_list)

    # Show stock details for selected sector
    st.markdown(f"#### Stocks in {selected_sector} sector")
    sector_stocks = summary_sector_df[summary_sector_df['Sector'] == selected_sector][['Ticker', 'Yearly Return']]
    st.dataframe(sector_stocks, use_container_width=True)

    # # Show sector performance table
    # st.markdown("---")
    # st.subheader("Sector-wise Performance")
    # st.dataframe(sector_perf, use_container_width=True)