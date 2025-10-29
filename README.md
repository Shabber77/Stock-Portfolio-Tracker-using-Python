##Stock Portfolio Tracker

Overview
This is a command-line Python application that helps users track their stock investments. It allows users to input stock symbols and quantities, calculates the total value based on predefined prices, and optionally saves the results to a .txt or .csv file.

🔧 Features
Predefined stock prices for popular companies:
AAPL, TSLA, MSFT, GOOGL, AMZN
Interactive input for stock symbols and quantities
Input validation for symbols and numeric values
Portfolio summary with total investment calculation
Option to save results in either text or CSV format
How to Run
Ensure Python 3 is installed on your system.
Save the code in a file named portfolio_tracker.py.
Open a terminal and run:
python portfolio_tracker.py
📋 Usage Instructions
The program displays available stock prices.
Enter stock symbols and quantities one by one.
Leave the symbol field empty and press Enter to finish.
After entering your portfolio, the program shows a summary.
You’ll be prompted to save the results:
Choose between .txt or .csv format.
Specify a file path or press Enter to use the default filename.
Example Output
Simple Stock Portfolio Tracker
Available stock prices:
  AAPL: $180.0
  TSLA: $250.0
  MSFT: $330.0
  GOOGL: $140.0
  AMZN: $130.0

Enter your stocks. Leave symbol empty and press Enter to finish.
Symbol: AAPL
Quantity: 10
Symbol: TSLA
Quantity: 5
Symbol:

Your Portfolio:
Symbol    Qty       Price       Value
---------------------------------------
AAPL      10.00     $180.00     $1800.00
TSLA       5.00     $250.00     $1250.00
---------------------------------------
Total Investment: $3050.00
File Output
Text Format (.txt): Human-readable summary with aligned columns.
CSV Format (.csv): Comma-separated values for spreadsheet use.
License
This project is free to use and modify for educational or personal purposes.

