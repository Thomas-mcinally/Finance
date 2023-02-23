from matplotlib.figure import Figure
import pandas as pd
import yfinance as yf
from mplfinance import figure, plot, show
import argparse
import datetime


def calculate_price_movement(
    data_1day: pd.DataFrame, data_90day: pd.DataFrame
) -> tuple[float, float, float, float]:
    """
    Parameters:
        data_1day (pd.DataFrame): Price for ticker, every 30m for last 24h
        data_90day (pd.DataFrame): Price for ticker evert 1h for last 90days

    Returns:
        current_price (float): Current price for ticker
        change_1day (float): Percentage price change over last 24hr
        change_7day (float): Percentage price change over last 7days
        change_30day (float): Percentage price change over last 30days
    """
    current_price = data_1day.iloc[-1, 3]

    datetime_30_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    datetime_7_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)

    finding_trading_day_data_30 = True
    while finding_trading_day_data_30:
        try:
            date_30_days_ago = datetime_30_days_ago.strftime("%Y-%m-%d")
            change_30day = (
                (current_price - data_90day.loc[date_30_days_ago, "Close"])
                / data_90day.loc[date_30_days_ago, "Close"]
                * 100
            )
            finding_trading_day_data_30 = False
        except KeyError:
            # no data because this day was not a trading day
            datetime_30_days_ago = datetime_30_days_ago - datetime.timedelta(days=1)

    finding_trading_day_data_7 = True
    while finding_trading_day_data_7:
        try:
            date_7_days_ago = datetime_7_days_ago.strftime("%Y-%m-%d")
            change_7day = (
                (current_price - data_90day.loc[date_7_days_ago, "Close"])
                / data_90day.loc[date_7_days_ago, "Close"]
                * 100
            )
            finding_trading_day_data_7 = False
        except KeyError:
            # no data because this day was not a trading day
            datetime_7_days_ago = datetime_7_days_ago - datetime.timedelta(days=1)

    change_1day = (current_price - data_1day.iloc[0, 0]) / data_1day.iloc[0, 0] * 100

    return current_price, change_1day, change_7day, change_30day


def visualize_results(
    ticker: str,
    data_1day: pd.DataFrame,
    data_90day: pd.DataFrame,
    current_price: float,
    change_1day: float,
    change_7day: float,
    change_30day: float,
) -> Figure:
    """
    Parameters:
        ticker (str): Stock ticker
        data_1day (pd.DataFrame): Price for ticker every 30m for last 24h
        data_90day (pd.DataFrame): Price for ticker evert 1h for last 90days
        current_price (float): Current price for ticker
        change_1day (float): Percentage price change over last 24hr
        change_7day (float): Percentage price change over last 7days
        change_30day (float): Percentage price change over last 30days

    Returns:
        fig (Figure): Matplotlib finance figure containing 90day line plot and 24hr candle stick plot of price movement
    """
    last_trading_day = data_1day.index.format()[0].split(" ")[0]

    fig = figure(figsize=(13, 6), style="blueskies")

    ax1 = fig.add_subplot(2, 2, 1)
    ax1_vol = fig.add_subplot(2, 2, 3)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2_vol = fig.add_subplot(2, 2, 4)

    plot(
        data_90day,
        ax=ax1,
        volume=ax1_vol,
        type="line",
        datetime_format="%d-%m",
        xrotation=20,
        axtitle=f"{ticker} last 90 days",
    )
    plot(
        data_1day,
        ax=ax2,
        volume=ax2_vol,
        type="candle",
        xrotation=20,
        axtitle=f"{ticker} last trading day ({last_trading_day})",
    )
    fig.suptitle(
        f"Current market price: {current_price:.2f} , Daily change {change_1day:.2f}% , 7-day change: {change_7day:.2f}%, 30-day change: {change_30day:.2f}%"
    )

    return fig


def main():
    # fetch ticker argument from bash terminal command
    parser = argparse.ArgumentParser()
    parser.add_argument("-ticker")
    args = parser.parse_args()
    ticker = args.ticker
    ticker = ticker.upper()

    data_1day = yf.download(
        ticker, period="1d", interval="30m", auto_adjust=True, progress=False
    )
    data_90day = yf.download(
        ticker, period="90d", interval="1d", auto_adjust=True, progress=False
    )

    current_price, change_1day, change_7day, change_30day = calculate_price_movement(
        data_1day, data_90day
    )

    fig = visualize_results(
        ticker,
        data_1day,
        data_90day,
        current_price,
        change_1day,
        change_7day,
        change_30day,
    )
    show()


if __name__ == "__main__":
    main()