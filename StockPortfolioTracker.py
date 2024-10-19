import yfinance as yf
import pandas as pd
class StockPortfolio:
    def __init__(self):
        # Initialize an empty portfolio as a DataFrame
        self.portfolio = pd.DataFrame(columns=['Ticker', 'Shares', 'Purchase Price'])
    def add_stock(self, ticker, shares, purchase_price):
        """
        Add a stock to the portfolio.
        :param ticker: Stock ticker symbol (e.g., 'AAPL')
        :param shares: Number of shares purchased
        :param purchase_price: Price per share at the time of purchase
        """
        # Create a new row for the stock
        new_stock = pd.DataFrame([[ticker, shares, purchase_price]], columns=self.portfolio.columns)
        # Append the new stock to the portfolio
        self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)
    def remove_stock(self, ticker):
        """
        Remove a stock from the portfolio by ticker symbol.
        :param ticker: Stock ticker symbol to remove
        """
        self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]
    def get_portfolio_value(self):
        """
        Calculate the total value of the portfolio based on current stock prices.
        :return: Total value of the portfolio
        """
        total_value = 0
        for index, row in self.portfolio.iterrows():
            # Fetch current stock price
            stock = yf.Ticker(row['Ticker'])
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            # Calculate total value for this stock
            total_value += current_price * row['Shares']
        return total_value
    def display_portfolio(self):
        """
        Display the current portfolio.
        """
        print("Current Portfolio:")
        print(self.portfolio)
        print(f"Total Portfolio Value: ${self.get_portfolio_value():.2f}")
# Example usage
if __name__ == "__main__":
    # Create a StockPortfolio instance
    my_portfolio = StockPortfolio()
    # Add stocks to the portfolio
    my_portfolio.add_stock('AAPL', 10, 150.00)  # 10 shares of Apple at $150 each
    my_portfolio.add_stock('GOOGL', 5, 2800.00)  # 5 shares of Google at $2800 each
    # Display the portfolio
    my_portfolio.display_portfolio()
    # Remove a stock from the portfolio
    my_portfolio.remove_stock('AAPL')
    # Display the updated portfolio
    my_portfolio.display_portfolio()