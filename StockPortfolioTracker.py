import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

class StockPortfolio:
    def __init__(self, api_key):
        """
        Initialize the stock portfolio with an Alpha Vantage API key.

        Args:
            api_key (str): Alpha Vantage API key
        """
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        """
        Add a stock to the portfolio.

        Args:
            symbol (str): Stock symbol (e.g. "AAPL")
            quantity (int): Number of shares to add
        """
        if symbol in self.portfolio:
            self.portfolio[symbol]["quantity"] += quantity
        else:
            self.portfolio[symbol] = {"quantity": quantity, "price": self.get_current_price(symbol)}

    def remove_stock(self, symbol, quantity):
        """
        Remove a stock from the portfolio.

        Args:
            symbol (str): Stock symbol (e.g. "AAPL")
            quantity (int): Number of shares to remove
        """
        if symbol in self.portfolio:
            if self.portfolio[symbol]["quantity"] >= quantity:
                self.portfolio[symbol]["quantity"] -= quantity
            else:
                print("Insufficient quantity to remove")
        else:
            print("Stock not found in portfolio")

    def get_current_price(self, symbol):
        """
        Get the current price of a stock using the Alpha Vantage API.

        Args:
            symbol (str): Stock symbol (e.g. "AAPL")

        Returns:
            float: Current stock price
        """
        ts = TimeSeries(key=self.api_key, output_format='pandas')
        data, meta_data = ts.get_quote_endpoint(symbol=symbol)
        return float(data['05. price'].iloc[0])

    def track_performance(self):
        """
        Track the performance of the portfolio by calculating the total value and percentage change.
        """
        total_value = 0
        for symbol, info in self.portfolio.items():
            current_price = self.get_current_price(symbol)
            total_value += current_price * info["quantity"]
            percentage_change = ((current_price - info["price"]) / info["price"]) * 100
            print(f"{symbol}: ${current_price:.2f} ({percentage_change:.2f}%)")
        print(f"Total portfolio value: ${total_value:.2f}")

# Example usage
api_key = "YOUR_API_KEY_HERE"
portfolio = StockPortfolio(api_key)

portfolio.add_stock("AAPL", 10)
portfolio.add_stock("GOOG", 5)

portfolio.track_performance()

portfolio.remove_stock("AAPL", 5)

portfolio.track_performance()