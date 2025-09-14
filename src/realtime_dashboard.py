import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import databento as db
from strategy import moving_average_crossover

st.set_page_config(layout="wide")
st.title("⚡ Real-Time Moving Average Crossover (Databento)")

# Initialize Databento Live client
API_KEY = "your_api_key_here"  # <- replace with your real key or env var
client = db.Live(api_key=API_KEY)

# Subscribe to ES futures, 1-min OHLCV bars
client.subscribe(
    dataset="GLBX.MDP3",   # CME Globex
    schema="ohlcv-1m",     # 1-minute OHLCV
    symbols="ES"
)

# Placeholders
placeholder_chart = st.empty()
placeholder_signal = st.empty()

# DataFrame to store incoming bars
df = pd.DataFrame(columns=["time", "price", "fast_ma", "slow_ma", "signal"])

# Stream live bars
for bar in client:
    # Parse bar (Databento returns a struct-like object)
    new_row = {
        "time": pd.to_datetime(bar.ts_event, unit="ns"),
        "price": float(bar.close)
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # Only calculate signals if we have enough data
    if len(df) > 60:
        df = moving_average_crossover(df)

        # Plot latest data
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df["time"], df["price"], label="Price", alpha=0.5)
        ax.plot(df["time"], df["fast_ma"], label="Fast MA (20)", color="blue")
        ax.plot(df["time"], df["slow_ma"], label="Slow MA (50)", color="red")

        buy_signals = df[df["signal"] == "BUY"]
        sell_signals = df[df["signal"] == "SELL"]

        ax.scatter(buy_signals["time"], buy_signals["price"], marker="^", color="green", label="Buy", alpha=0.8)
        ax.scatter(sell_signals["time"], sell_signals["price"], marker="v", color="red", label="Sell", alpha=0.8)

        ax.legend()
        placeholder_chart.pyplot(fig)

        placeholder_signal.metric("Latest Signal", df["signal"].iloc[-1])
