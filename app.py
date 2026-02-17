import streamlit as st
import pandas as pd
from src.data_cleaning import load_and_clean_data
from src.kpi_calculator import calculate_marketing_kpis, generate_summary_stats

# Page config
st.set_page_config(page_title="Marketing Insights Engine", layout="wide")

# Title
st.title("📊 Marketing Performance Dashboard")
st.markdown("**Automated KPI Tracking & ROI Analysis**")

# Load data
@st.cache_data
def load_data():
    df = load_and_clean_data('data/raw_data_sample.csv')
    df = calculate_marketing_kpis(df)
    return df

df = load_data()

# Summary metrics
summary = generate_summary_stats(df)

# Display KPI cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Spend", f"${summary['Total_Spend']:,.0f}")
col2.metric("Total Revenue", f"${summary['Total_Revenue']:,.0f}")
col3.metric("Avg ROAS", f"{summary['Avg_ROAS']:.2f}x")
col4.metric("Avg CPA", f"${summary['Avg_CPA']:.0f}")

# Filters
st.sidebar.header("Filters")

selected_channel = st.sidebar.multiselect(
    "Select Channels",
    options=df['channel'].unique(),
    default=df['channel'].unique()
)

filtered_df = df[df['channel'].isin(selected_channel)]

# Charts
st.subheader("ROAS by Campaign")

chart_data = filtered_df.set_index('campaign_name')['roas']
st.bar_chart(chart_data)

# Data table
st.subheader("Detailed KPI Table")

st.dataframe(
    filtered_df.style.format({
        'spend': '${:,.0f}',
        'revenue': '${:,.0f}',
        'cpa': '${:.0f}',
        'roas': '{:.2f}x',
        'conversion_rate': '{:.2f}%'
    })
)
