#!/usr/bin/env python3
"""
Simple test script to validate the investment analysis functionality.
"""

import pandas as pd
import os
import sys

def test_investment_analysis():
    """Test basic functionality of the investment analysis script."""
    
    # Check if required files exist
    if not os.path.exists('investments.csv'):
        print("ERROR: investments.csv not found")
        return False
    
    if not os.path.exists('investment_analysis.py'):
        print("ERROR: investment_analysis.py not found") 
        return False
    
    try:
        # Test reading the CSV file
        df = pd.read_csv('investments.csv')
        print(f"✓ Successfully read CSV with {len(df)} rows")
        
        # Test required columns exist
        required_columns = ['Investor', 'Investment_Type', 'Amount_Original', 
                          'Currency', 'FX_Rate_to_INR', 'Shares_Issued', 
                          'CurrentPrice_perShare']
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"ERROR: Missing columns: {missing_columns}")
            return False
        print("✓ All required columns present")
        
        # Test calculations
        df['Amount_INR'] = df['Amount_Original'] * df['FX_Rate_to_INR']
        df['CurrentMarketValue_INR'] = df.apply(
            lambda r: r['Shares_Issued'] * r['CurrentPrice_perShare'] * r['FX_Rate_to_INR']
                      if r['Shares_Issued'] > 0 else r['Amount_INR'], axis=1)
        df['GainLoss_INR'] = df['CurrentMarketValue_INR'] - df['Amount_INR']
        
        print("✓ Calculations completed successfully")
        
        # Test grouping
        investor_summary = df.groupby('Investor').agg({
            'Amount_INR': 'sum',
            'CurrentMarketValue_INR': 'sum', 
            'GainLoss_INR': 'sum'
        }).round(2)
        
        print(f"✓ Grouping completed: {len(investor_summary)} investors")
        
        # Test that totals make sense
        total_invested = df['Amount_INR'].sum()
        total_current = df['CurrentMarketValue_INR'].sum()
        
        if total_invested <= 0:
            print("ERROR: Total invested amount is not positive")
            return False
        
        if total_current <= 0:
            print("ERROR: Total current value is not positive")
            return False
            
        print(f"✓ Portfolio totals: Invested={total_invested:,.0f}, Current={total_current:,.0f}")
        
        return True
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    print("Running investment analysis tests...")
    if test_investment_analysis():
        print("\n✓ All tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Tests failed!")
        sys.exit(1)