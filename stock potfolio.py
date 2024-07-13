class StockPortfolio:
    def __init__(self):
        self.stocks = {}  # Dictionary to store stocks (ticker: quantity)

    def add_stock(self, ticker, quantity):
        if ticker in self.stocks:
            self.stocks[ticker] += quantity
        else:
            self.stocks[ticker] = quantity
        print(f"Added {quantity} shares of {ticker}.")

    def remove_stock(self, ticker, quantity):
        if ticker in self.stocks:
            if self.stocks[ticker] >= quantity:
                self.stocks[ticker] -= quantity
                print(f"Removed {quantity} shares of {ticker}.")
                if self.stocks[ticker] == 0:
                    del self.stocks[ticker]
            else:
                print(f"Not enough shares of {ticker} to remove.")
        else:
            print(f"No shares of {ticker} found in portfolio.")

    def track_portfolio(self):
        print("Current Portfolio:")
        for ticker, quantity in self.stocks.items():
            print(f"{ticker}: {quantity} shares")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            ticker = input("Enter stock ticker: ")
            quantity = int(input("Enter quantity to add: "))
            portfolio.add_stock(ticker, quantity)
        elif choice == '2':
            ticker = input("Enter stock ticker: ")
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(ticker, quantity)
        elif choice == '3':
            portfolio.track_portfolio()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
