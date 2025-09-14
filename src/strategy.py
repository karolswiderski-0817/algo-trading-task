import pandas as pd

def moving_average_crossover(data: pd.DataFrame, fast: int = 20, slow: int = 50):
    """
    Generate buy/sell signals using moving average crossover strategy.
    :param data: DataFrame with 'time' and 'price'
    :return: DataFrame with columns [time, price, fast_ma, slow_ma, signal]
    """
    df = data.copy()
    df["fast_ma"] = df["price"].rolling(window=fast).mean()
    df["slow_ma"] = df["price"].rolling(window=slow).mean()
    df["signal"] = None

    for i in range(1, len(df)):
        if df["fast_ma"].iloc[i-1] < df["slow_ma"].iloc[i-1] and df["fast_ma"].iloc[i] > df["slow_ma"].iloc[i]:
            df.loc[df.index[i], "signal"] = "BUY"
        elif df["fast_ma"].iloc[i-1] > df["slow_ma"].iloc[i-1] and df["fast_ma"].iloc[i] < df["slow_ma"].iloc[i]:
            df.loc[df.index[i], "signal"] = "SELL"

    return df.dropna(subset=["fast_ma", "slow_ma"])
