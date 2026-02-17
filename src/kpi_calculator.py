import pandas as pd

def calculate_marketing_kpis(df):
    print(df.columns)

    df.columns = df.columns.str.strip().str.lower()

    df['cpa'] = df['spend'] / df['conversions'].replace(0, 1)
    df['roas'] = df['revenue'] / df['spend'].replace(0, 1)
    df['conversion_rate'] = (df['conversions'] / df['clicks'].replace(0, 1)) * 100

    return df


def generate_summary_stats(df):
    summary = {
        'Total_Spend': df['spend'].sum(),
        'Total_Revenue': df['revenue'].sum(),
        'Total_Conversions': df['conversions'].sum(),
        'Avg_ROAS': df['roas'].mean(),
        'Avg_CPA': df['cpa'].mean()
    }

    return summary
