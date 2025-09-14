import pandas as pd
from strategy import moving_average_crossover
from utils import calculate_pnl

def run_backtest():
    # --- Load data ---
    # For now, generate synthetic data (replace with Databento later)
    rng = pd.date_range("2024-01-01", periods=500, freq="T")
    prices = pd.Series(100 + pd.Series(range(500)).apply(lambda x: (x % 50) - 25).cumsum())
    data = pd.DataFrame({"time": rng, "price": prices})

    # --- Apply strategy ---
    signals = moving_average_crossover(data)

    # --- Calculate PnL ---
    results, trades = calculate_pnl(signals)

    return results, signals

if __name__ == "__main__":
    results, df = run_backtest()
    print("Backtest Results:")
    for k, v in results.items():
        print(f"{k}: {v}")
