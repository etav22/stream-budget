import streamlit as st
import pandas as pd
from loguru import logger

st.set_page_config(layout="wide")
st.title("Stream-Budget")

# Get data and convert the date column to datetime objects
df = pd.read_csv("data/transactions.csv", index_col=False)
df["Posting Date"] = pd.to_datetime(df["Posting Date"], format="%m/%d/%Y").dt.date
st.markdown("## Transactions")

# Create a time series selector to filter the dataframe
col1, col2 = st.columns([0.2, 0.8])

with col1:
    min_max_date = (df["Posting Date"].min(), df["Posting Date"].max())
    date_range = st.date_input(
        "Start date",
        value=min_max_date,
        min_value=min_max_date[0],
        max_value=min_max_date[1],
    )
    transax_type = st.selectbox("Transaction Type", df["Type"].unique())
    card = st.selectbox("Card", df["Details"].unique())
    check_slip = st.selectbox("Check or Slip", df["Check or Slip #"].unique())

# Wait until the user has both start and end dates
if len(date_range) == 2:
    # Convert datetime objects to strings for filtering
    with col2:
        # date_range = [str(date_range[0]), str(date_range[1])]
        logger.debug(f"date_range: {date_range}")

        # # Filter the dataframe by the date range
        df = df[df["Posting Date"].between(date_range[0], date_range[1])]
        st.dataframe(df)

    # Create a plotly line chart of balance over time
    st.markdown("## Balance over time")
    st.line_chart(data=df, x="Posting Date", y="Balance")
