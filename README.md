# 📈 StockIntel AI

**StockIntel AI** is a data-driven stock analysis application that leverages Artificial Intelligence (AI), Machine Learning (ML), and statistical techniques to analyze and visualize stock market data. It integrates Python, Pandas, SQL, Power BI, and statistical modeling to provide actionable insights for investors and analysts.

---

## 🚀 Features

- 📊 Historical stock data ingestion and preprocessing
- 📈 Technical and fundamental analysis
- 🧠 Machine learning models for prediction and clustering
- 📉 Statistical analysis and hypothesis testing
- 📊 Power BI dashboards for interactive visualization
- 🗃️ SQL database integration for scalable data storage
- 📈 Streamlit dashboard for interactive Python analytics
- 🏆 Top gainers/losers, volatility, sector-wise analysis, cumulative returns, and price correlation

---

## 🛠️ Tech Stack

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly, yfinance, Streamlit
- **Database**: MySQL / PostgreSQL
- **Visualization**: Power BI, Plotly, Streamlit
- **ML Frameworks**: Scikit-learn, XGBoost, TensorFlow (optional)
- **Data Sources**: Yahoo Finance, Alpha Vantage

---

## 📁 Folder Structure

StockIntel_AI/
├── data/                # Raw and processed datasets
├── notebooks/           # Jupyter notebooks for exploration and modeling
├── models/              # Saved ML models
├── dashboards/          # Power BI or visualization outputs
├── scripts/             # Python scripts for ingestion, preprocessing, etc.
├── cumulative_return.py # Cumulative return calculations
├── gainers_losers.py    # Monthly top gainers/losers analysis
├── load_data.py         # Data loading utilities
├── market_summary.py    # Market summary logic
├── sector_wise.py       # Sector performance analysis
├── stock_price_correlation.py # Correlation matrix visualization
├── stockmarket_app.py   # Main Streamlit app
├── utlity.py            # Database and helper functions
├── volatile.py          # Volatility analysis
├── requirements.txt     # Python dependencies

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StockIntel_AI.git
   cd StockIntel_AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your data:
   - Ensure your SQL database contains the following table:

     ```sql
     CREATE TABLE stock_prices (
         Ticker VARCHAR(20),
         close FLOAT,
         date DATETIME,
         high FLOAT,
         low FLOAT,
         month VARCHAR(7),
         open FLOAT,
         volume BIGINT
     );
     ```

   - Place your stock price data in the appropriate location.
   - Ensure sector mapping CSV is available as referenced in `sector_wise.py`.

4. Run the dashboard:
   ```bash
   streamlit run stockmarket_app.py
   ```

---

## 📦 Main Python Modules

- `load_data.py`: Efficient loading and preprocessing of stock data from CSV or SQL.
- `cumulative_return.py`: Calculates and visualizes cumulative returns for top-performing stocks.
- `gainers_losers.py`: Identifies monthly top 5 gainers and losers.
- `volatile.py`: Analyzes most and least volatile stocks.
- `sector_wise.py`: Sector-wise performance analysis.
- `stock_price_correlation.py`: Visualizes correlations between stock prices.
- `market_summary.py`: Provides market summary and preprocessing utilities.
- `utlity.py`: Database connection and helper functions.

---

## 📄 License

MIT License

---

*For questions or contributions, please open an issue or pull request.*
