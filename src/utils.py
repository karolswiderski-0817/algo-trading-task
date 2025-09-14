import pandas as pd

def calculate_pnl(df: pd.DataFrame, initial_cash: float = 100000):
    """
    Simple PnL calculation based on buy/sell signals.
    Assumes 1 contract per trade, no fees/slippage.
    """
    cash = initial_cash
    position = 0
    entry_price = 0
    trades = []

    for i, row in df.iterrows():
        if row["signal"] == "BUY" and position == 0:
            position = 1
            entry_price = row["price"]
            trades.append(("BUY", row["time"], row["price"]))
        elif row["signal"] == "SELL" and position == 1:
            profit = row["price"] - entry_price
            cash += profit
            position = 0
            trades.append(("SELL", row["time"], row["price"], profit))

    results = {
        "Final Cash": cash,
        "Total Return": cash - initial_cash,
        "Number of Trades": len(trades),
    }

    return results, trades
