import streamlit as st
import matplotlib.pyplot as plt
from backtest import run_backtest

st.set_page_config(layout="wide")
st.title("📊 Moving Average Crossover Strategy Dashboard")

# Run backtest
results, df = run_backtest()

# Show metrics
st.subheader("Performance Metrics")
st.json(results)

# Plot signals
st.subheader("Chart: Price + Moving Averages + Buy/Sell Signals")

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(df["time"], df["price"], label="Price", alpha=0.5)
ax.plot(df["time"], df["fast_ma"], label="Fast MA (20)", color="blue")
ax.plot(df["time"], df["slow_ma"], label="Slow MA (50)", color="red")

buy_signals = df[df["signal"] == "BUY"]
sell_signals = df[df["signal"] == "SELL"]

ax.scatter(buy_signals["time"], buy_signals["price"], marker="^", color="green", label="Buy", alpha=0.8)
ax.scatter(sell_signals["time"], sell_signals["price"], marker="v", color="red", label="Sell", alpha=0.8)

ax.legend()
st.pyplot(fig)
