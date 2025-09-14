# 📈 Strategy Report: Moving Average Crossover Strategy

## 1. 🛠️ Approach
The task was to implement and analyze a **Moving Average Crossover strategy** for E-mini S&P 500 futures.

- ⚡ **Fast Moving Average**: 20 periods  
- 🐢 **Slow Moving Average**: 50 periods  
- ✅ **Buy Signal**: when the fast MA crosses above the slow MA  
- ❌ **Sell Signal**: when the fast MA crosses below the slow MA  

I structured the project into:
- `strategy.py` → strategy logic  
- `backtest.py` → backtest engine  
- `utils.py` → performance metrics  
- `dashboard.py` → 📊 Streamlit dashboard (mock historical analysis)  
- `realtime_dashboard.py` → ⏱️ Streamlit real-time dashboard (simulation + Databento live API option)  

---

## 2. ⚙️ Technical Decisions
- **Synthetic Data First**: ✅ Started with generated fake data so the project runs without external setup.  
- **Modular Design**: 📦 Strategy, backtest, metrics, and dashboards separated into clean modules.  
- **Dashboards**:
  - 📊 **Static Dashboard** (`dashboard.py`) → shows historical charts with signals.  
  - ⏱️ **Real-Time Dashboard** (`realtime_dashboard.py`) → simulates live updates, one bar at a time.  
  - 🌍 Ready to integrate with **Databento Live API** for real market data.  

---

## 3. 📊 Results
Backtest on **synthetic test data** (500 bars, 1-minute resolution):

- 💰 **Final Cash:** 97,672  
- 📉 **Total Return:** -2,328  
- 🔁 **Number of Trades:** 17  

The results were saved in `reports/backtest_results.txt`.  
➡️ The raw strategy was **not profitable** on this dataset.  

---

## 4. 🖥️ Dashboard Analysis
- **Static Dashboard (`dashboard.py`)**
  - 📈 Visualizes price, moving averages, and signals.  
  - Helps understand when and why trades were triggered.  

- **Real-Time Dashboard (`realtime_dashboard.py`)**
  - ⏱️ Simulates streaming data with 1 bar per second.  
  - 🔄 Continuously updates chart and latest signal.  
  - 🌍 Includes code to connect to **Databento Live API** for real-time data.  

---

## 5. 🔍 Analysis
- ✅ Captures **trend-following behavior** when markets move strongly.  
- ⚠️ Generates **false signals in sideways markets**, causing losses.  
- 📊 Dashboards make it clear where the strategy performs well or poorly.  

---

## 6. 🚀 Possible Improvements
- 📉 Use **EMA** instead of SMA for faster reactions.  
- 🕵️ Add **filters** (volatility, higher timeframe trend).  
- 🛑 Add **stop-loss / take-profit** rules.  
- 📡 Backtest on **Databento ES 2024 real data** instead of synthetic.  
- 📈 Extend dashboards with **PnL curves, trade logs, KPIs**.  

---

## 7. ⚠️ Limitations
- 🧪 Results are based on **fake synthetic data** (not real markets).  
- 💸 No commissions, fees, or slippage modeled.  
- 📏 Position sizing = fixed (1 contract).  
- ⚡ Simplified backtest vs. pro frameworks like Nautilus Trader.  

---

## 8. ✅ Conclusion
This project demonstrates:
- 📝 A working **Moving Average Crossover strategy**  
- 🧮 A **backtest engine** with summary metrics  
- 📊 An **interactive dashboard** for historical analysis  
- ⏱️ A **real-time dashboard** simulating live trading and prepared for **Databento integration**  

While the base strategy isn’t profitable on synthetic data, the workflow is clear:  
👉 **strategy → backtest → analysis → dashboard → real-time readiness** 🎯
