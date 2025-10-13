
# � StockIntel AI

StockIntel AI is a comprehensive stock market analysis dashboard built with Python and Streamlit. It provides interactive visualizations and analytics for stock data, including volatility, cumulative returns, sector performance, price correlation, and gainers/losers analysis.

---

## 🚀 Features

- Interactive dashboard for stock market analysis
- Volatility, cumulative return, sector-wise performance, price correlation, and gainers/losers modules
- SQL database integration for scalable data storage
- Data preprocessing and summary statistics
- Modern UI with Streamlit

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit, SQLAlchemy, yfinance, scikit-learn, xgboost, tensorflow (optional)
- **Database:** MySQL or PostgreSQL
- **Visualization:** Streamlit, Plotly

---

## 📁 Folder Structure

```
StockIntel_AI/
├── cumulative_return.py         # Cumulative return calculations
├── gainers_losers.py           # Monthly top gainers/losers analysis
├── load_data.py                # Data loading utilities
├── market_summary.py           # Market summary logic
├── sector_wise.py              # Sector performance analysis
├── stock_price_correlation.py  # Correlation matrix visualization
├── stockmarket_app.py          # Main Streamlit app
├── utlity.py                   # Database and helper functions
├── volatile.py                 # Volatility analysis
├── requirements.txt            # Python dependencies
├── environment/                # Python virtual environment
├── models/                     # Saved ML models
├── notebooks/                  # Jupyter notebooks
├── scripts/                    # Utility scripts
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/yourusername/StockIntel_AI.git
   cd StockIntel_AI
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Prepare your data:**
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
   - Place your stock price data in the database.
   - Ensure sector mapping CSV is available as referenced in `sector_wise.py` (default path: `C:\Users\Python\Sector_data.csv`).

4. **Run the dashboard:**
   ```powershell
   streamlit run stockmarket_app.py
   ```

---

## 📦 Main Python Modules

- `load_data.py`: Loads and preprocesses stock data from CSV or SQL
- `cumulative_return.py`: Calculates and visualizes cumulative returns
- `gainers_losers.py`: Identifies monthly top gainers and losers
- `volatile.py`: Analyzes volatility
- `sector_wise.py`: Sector-wise performance analysis
- `stock_price_correlation.py`: Visualizes price correlations
- `market_summary.py`: Market summary and preprocessing
- `utlity.py`: Database connection and helper functions

---

## 📄 License

MIT License

---

*For questions or contributions, please open an issue or pull request.*