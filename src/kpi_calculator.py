import pandas as pd

def calculate_marketing_kpis(df):
    """
    Calculates essential marketing metrics from raw campaign data.
    """
    # Avoid division by zero
    df['CPA'] = df['Spend'] / df['Conversions'].replace(0, 1)
    df['ROAS'] = df['Revenue'] / df['Spend'].replace(0, 1)
    df['Conversion_Rate'] = (df['Conversions'] / df['Clicks'].replace(0, 1)) * 100
    
    return df[['Date', 'Campaign_Name', 'Channel', 'Spend', 'Revenue', 'CPA', 'ROAS', 'Conversion_Rate']]

def generate_summary_stats(df):
    """Generates overall performance summary."""
    summary = {
        'Total_Spend': df['Spend'].sum(),
        'Total_Revenue': df['Revenue'].sum(),
        'Total_Conversions': df['Conversions'].sum(),
        'Avg_ROAS': df['ROAS'].mean(),
        'Avg_CPA': df['CPA'].mean()
    }
    return summary