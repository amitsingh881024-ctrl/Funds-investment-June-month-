# Funds Investment Analysis - June Month

This repository contains a Python script for analyzing investment portfolio performance, including currency conversions, current market values, and gain/loss calculations.

## Features

- **Multi-currency support**: Handles investments in different currencies (USD, EUR) with automatic conversion to INR
- **Flexible investment types**: Supports both share-based investments and fixed-amount investments
- **Comprehensive analysis**: Calculates current market values, gains/losses, and percentage returns
- **Investor grouping**: Provides summary statistics grouped by investor
- **Portfolio overview**: Shows overall portfolio performance

## Files

- `investment_analysis.py`: Main Python script for investment analysis
- `investments.csv`: Sample investment data
- `requirements.txt`: Python dependencies

## Data Format

The script expects a CSV file with the following columns:
- `Investor`: Name of the investor
- `Investment_Type`: Type of investment (e.g., Equity Fund, Mutual Fund)
- `Amount_Original`: Original investment amount in source currency
- `Currency`: Currency of the original investment (USD, EUR, etc.)
- `FX_Rate_to_INR`: Exchange rate from source currency to INR
- `Shares_Issued`: Number of shares (0 for fixed-amount investments)
- `CurrentPrice_perShare`: Current price per share (0 for fixed-amount investments)

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure your investment data is in `investments.csv` format

3. Run the analysis:
   ```bash
   python investment_analysis.py
   ```

## Output

The script provides:
1. Detailed investment data with calculated INR values
2. Summary by investor showing total investments, current values, and returns
3. Overall portfolio summary with total gains/losses and return percentage

## Example Output

```
=== Investment Analysis Summary ===

Detailed Investment Data:
     Investor    Investment_Type  Amount_INR  CurrentMarketValue_INR  GainLoss_INR
     John Doe        Equity Fund    831200.0                831200.0           0.0
   Jane Smith        Mutual Fund    415600.0                436380.0       20780.0
...

=== Summary by Investor ===
               Amount_INR  CurrentMarketValue_INR  GainLoss_INR  Return_Percentage
Investor                                                                          
Alice Johnson   1214320.0               1239256.0       24936.0               2.05
Bob Wilson      1496160.0               1832796.0      336636.0              22.50
...

=== Overall Portfolio Summary ===
Total Amount Invested (INR): 8,048,320.00
Total Current Value (INR): 8,837,469.40
Total Gain/Loss (INR): 789,149.40
Overall Return Percentage: 9.81%
```
