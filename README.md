# Algorithmic Trading Task – Moving Average Crossover Strategy

## 📌 Overview
This project implements a **Moving Average Crossover trading strategy** for E-mini S&P 500 futures:
- **Fast Moving Average (20 periods)**
- **Slow Moving Average (50 periods)**
- **Buy Signal** when fast MA crosses above slow MA
- **Sell Signal** when fast MA crosses below slow MA

The project includes:
- A **backtest engine** with synthetic (fake) data
- A **static dashboard** for analyzing historical signals
- A **real-time dashboard** (simulated) with option to connect to **Databento Live API**

---

## ⚙️ Tech Stack
- Python 3.10+
- [pandas](https://pandas.pydata.org/)  
- [numpy](https://numpy.org/)  
- [matplotlib](https://matplotlib.org/)  
- [streamlit](https://streamlit.io/)  
- [databento](https://docs.databento.com/) (for historical/live data)  

---

## 📂 Project Structure
```

algo-trading-task/
│
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── src/
│   ├── strategy.py            # Moving average crossover logic
│   ├── backtest.py            # Backtest script
│   ├── utils.py               # Metrics and helpers
│   ├── dashboard.py           # Streamlit dashboard (historical)
│   └── realtime\_dashboard.py  # Streamlit dashboard (simulated real-time)
│
├── reports/
│   ├── backtest\_results.txt   # Backtest metrics
│   └── strategy\_report.md     # Strategy write-up

````

---

## 🚀 Setup & Installation
1. Clone the project:
   ```bash
   git clone <repo-url>
   cd algo-trading-task
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up Databento:

   * Create an account at [Databento](https://databento.com)
   * Get your API key
   * Set it as environment variable:

     ```bash
     export DATABENTO_API_KEY="your_api_key_here"
     ```

   On Windows PowerShell:

   ```powershell
   $env:DATABENTO_API_KEY="your_api_key_here"
   ```

---

## ▶️ Running the Project

### 1. Backtest (synthetic data)

```bash
python src/backtest.py
```

Results are saved in `reports/backtest_results.txt`.

### 2. Static Dashboard

```bash
streamlit run src/dashboard.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

### 3. Real-Time Dashboard (simulation)

```bash
streamlit run src/realtime_dashboard.py
```

Simulates streaming one bar at a time.
With a valid API key, can connect to **Databento Live API** for real market data.

---

## 📊 Deliverables

* **Code**: `src/`
* **Backtest Results**: `reports/backtest_results.txt`
* **Report**: `reports/strategy_report.md`

---

## 📌 Notes

* Current backtest uses **synthetic fake data** for demonstration.
* Replace with **Databento historical ES 2024 data** (`ohlcv-1m`) for real evaluation.
* The dashboards can be extended with more analytics (PnL curve, Sharpe ratio, drawdowns).

---

## ✅ Conclusion

This project demonstrates:

* A clean Python implementation of the **moving average crossover strategy**
* A backtesting pipeline
* Interactive dashboards (static + real-time simulation)
* Extensibility toward real trading data with Databento

```
