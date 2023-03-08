import sys

from stockprice.shared import calculate_price_movement


def main(args: list = sys.argv):
    raw_input = args[1]
    stocks = raw_input.upper().split(",")

    for ticker in stocks:
        (
            current_price,
            percentage_change_1day,
            percentage_change_7day,
            percentage_change_30day,
        ) = calculate_price_movement(ticker)

        summary = f"{ticker} -- Current price: {current_price:.2f} -- Daily change: {percentage_change_1day:.2f}%, 7-day change: {percentage_change_7day:.2f}%, 30-day change: {percentage_change_30day:.2f}%"

        print(summary)


if __name__ == "__main__":
    main()