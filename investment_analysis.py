import pandas as pd

# Read data
df = pd.read_csv('investments.csv')

# Calculate amount in INR
df['Amount_INR'] = df['Amount_Original'] * df['FX_Rate_to_INR']

# Calculate current market value
df['CurrentMarketValue_INR'] = df.apply(
    lambda r: r['Shares_Issued'] * r['CurrentPrice_perShare'] * r['FX_Rate_to_INR']
              if r['Shares_Issued'] > 0 else r['Amount_INR'], axis=1)

# Calculate gain/loss
df['GainLoss_INR'] = df['CurrentMarketValue_INR'] - df['Amount_INR']

# Group by investor and summarize
investor_summary = df.groupby('Investor').agg({
    'Amount_INR': 'sum',
    'CurrentMarketValue_INR': 'sum',
    'GainLoss_INR': 'sum'
}).round(2)

# Calculate percentage returns
investor_summary['Return_Percentage'] = (
    (investor_summary['GainLoss_INR'] / investor_summary['Amount_INR']) * 100
).round(2)

# Display results
print("=== Investment Analysis Summary ===")
print("\nDetailed Investment Data:")
print(df[['Investor', 'Investment_Type', 'Amount_INR', 'CurrentMarketValue_INR', 'GainLoss_INR']].to_string(index=False))

print("\n=== Summary by Investor ===")
print(investor_summary.to_string())

print(f"\n=== Overall Portfolio Summary ===")
total_invested = df['Amount_INR'].sum()
total_current_value = df['CurrentMarketValue_INR'].sum()
total_gain_loss = df['GainLoss_INR'].sum()
overall_return = (total_gain_loss / total_invested) * 100

print(f"Total Amount Invested (INR): {total_invested:,.2f}")
print(f"Total Current Value (INR): {total_current_value:,.2f}")
print(f"Total Gain/Loss (INR): {total_gain_loss:,.2f}")
print(f"Overall Return Percentage: {overall_return:.2f}%")