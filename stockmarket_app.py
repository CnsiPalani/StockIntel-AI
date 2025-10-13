from glob import glob
from pdb import main
import pandas as pd
import yaml
import os
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns
from load_data import load_yaml_data
from market_summary import preprocess_data, market_summary
# Import and run individual analysis modules
from volatile import volatile
from cumulative_return import cumulative_return
from stock_price_correlation import stock_price_correlation

from gainers_losers import gainers_losers
from sector_wise import sector_wise
from utlity import get_connection, close_connection, execute_query, insert_bulk_data


st.set_page_config(page_title=" 📊 Stock Market Analysis Dashboard", layout="wide")

def main():
    # Sidebar logo and description with reliable online logo
    st.sidebar.image("https://static.vecteezy.com/system/resources/previews/016/227/291/non_2x/bull-with-chart-bar-logo-design-finance-logo-design-free-vector.jpg", use_container_width=True)
    # Title with custom style
    st.markdown("<h1 style='text-align: center; color: #2E86C1;'>📊 Stock Market Analysis Dashboard</h1>", unsafe_allow_html=True)

    # Load and preprocess data
    df = execute_query("SELECT * FROM stock_prices")
    df = pd.DataFrame(df)
    df1 = preprocess_data(df)

    # Sidebar navigation with tooltips
    st.sidebar.title("Navigation")
    MARKET_SUMMARY = "Market Summary"
    page = st.sidebar.radio(
        "Select Analysis",
        [
            MARKET_SUMMARY,
            "Volatility",
            "Cumulative Return",
            "Sector Performance",
            "Correlation",
            "Gainers/Losers"
            #,"Processed Data"
        ],
        help="Choose the type of analysis to display"
    )

    # Main content area with expanders and columns
    if page == MARKET_SUMMARY:
        with st.expander("View Market Summary", expanded=True):
             market_summary(df1)
           
    elif page == "Volatility":
        with st.expander("View Volatility Details", expanded=True):
           volatile(df)
    elif page == "Cumulative Return":
        with st.expander("View Cumulative Return", expanded=True,):
            cumulative_return(df)
    elif page == "Sector Performance":
        with st.expander("View Sector Performance", expanded=True):
            sector_wise(df1)
    elif page == "Correlation":
        with st.expander("View Correlation Matrix", expanded=True):
            stock_price_correlation(df)
    elif page == "Gainers/Losers":
        with st.expander("View Gainers/Losers", expanded=True):
            gainers_losers(df)
    # elif page == "Processed Data":
    #     with st.expander("View Processed Data", expanded=True):
    #         st.dataframe(df1)

    # Footer
    st.markdown("""
    <hr style='border:1px solid #eee;'>
    <div style='text-align: center;'>
        <small>Developed by <b>StockIntel AI</b> | <a href='https://github.com/your-repo' target='_blank'>GitHub</a></small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
