# Funds-investment-June-month-
import pandas as pd  # Read data df = pd.read_csv('investments.csv')  # Calculate amount in INR df['Amount_INR'] = df['Amount_Original'] * df['FX_Rate_to_INR']  # Calculate current market value df['CurrentMarketValue_INR'] = df.apply(     lambda r: r['Shares_Issued'] * 
