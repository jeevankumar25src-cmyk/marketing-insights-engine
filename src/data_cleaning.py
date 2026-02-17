import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads and cleans marketing data.
    """
    df = pd.read_csv(filepath)
    
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Remove any rows with negative spend (data errors)
    df = df[df['Spend'] >= 0]
    
    # Fill missing values
    df = df.fillna(0)
    
    return df