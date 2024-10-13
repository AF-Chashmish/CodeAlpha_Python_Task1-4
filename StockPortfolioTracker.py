    portfolio.track_performance()
    portfolio.remove_stock("AAPL", 2)

    portfolio.track_performance()
    portfolio.add_stock("GOOG", 5)
    portfolio.add_stock("AAPL", 10)

    portfolio = StockPortfolio(api_key)
    api_key = "YOUR_API_KEY_HERE"
if __name__ == "__main__":
# Example usage

        print(f"Total Portfolio Value: ${total_value:.2f}")
            print(f"{symbol}: ${current_price:.2f} ({percentage_change:.2f}%)")
            percentage_change = ((current_price - info["price"]) / info["price"]) * 100
            total_value += current_price * info["quantity"]
            current_price = self.get_current_price(symbol)
        for symbol, info in self.portfolio.items():
        total_value = 0
    def track_performance(self):

        return float(data['05. price'].iloc[0])  # Convert to float and use iloc
        data, meta_data = ts.get_quote_endpoint(symbol=symbol)
        ts = TimeSeries(key=self.api_key, output_format='pandas')
    def get_current_price(self, symbol):

            print("Stock not found in portfolio.")
        else:
                print("Insufficient quantity to remove.")
            else:
                self.portfolio[symbol]["quantity"] -= quantity
            if self.portfolio[symbol]["quantity"] >= quantity:
        if symbol in self.portfolio:
    def remove_stock(self, symbol, quantity):

            self.portfolio[symbol] = {"quantity": quantity, "price": self.get_current_price(symbol)}
        else:
            self.portfolio[symbol]["quantity"] += quantity
        if symbol in self.portfolio:
    def add_stock(self, symbol, quantity):

        self.portfolio = {}
        self.api_key = api_key
    def __init__(self, api_key):
class StockPortfolio:

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import alpha_vantage