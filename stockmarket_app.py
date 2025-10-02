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
from market_summary import preprocess_data, load_data, market_summary
# Import and run individual analysis modules
from volatile import volatile
from cumulative_return import cumulative_return
from stock_price_correlation import stock_price_correlation

from gainers_losers import gainers_losers
from sector_wise import sector_wise
from utlity import get_connection, close_connection, execute_query, insert_bulk_data


st.set_page_config(page_title="📊 Stock Market Analysis Dashboard", layout="wide")

def main():
    # Image and title

    st.title(" Stock Market Analysis Dashboard")

    # Load and preprocess data

    df = execute_query("SELECT * FROM stock_prices")
    df = pd.DataFrame(df)
    df1 = preprocess_data(df)

    # Sidebar navigation
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
            
        ]
    )

    if page == MARKET_SUMMARY:
        st.header("Market Summary")
        market_summary(df1)
    elif page == "Volatility":
        volatile(df)
    elif page == "Cumulative Return":
        cumulative_return(df)
    elif page == "Sector Performance":
        sector_wise(df1) 
    elif page == "Correlation":
        stock_price_correlation(df)
    elif page == "Gainers/Losers":
        gainers_losers(df)
    


if __name__ == "__main__":
    main()
