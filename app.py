import streamlit as st
import pandas as pd

st.title("Stream-Budget")

# Get data and convert the date column to datetime objects
df = pd.read_csv("data/chase_activity.csv", index_col=False)
df["Posting Date"] = pd.to_datetime(df["Posting Date"])

# Create a time series selector to filter the dataframe
st.markdown("## Filter by date")
min_max_date = (df["Posting Date"].min(), df["Posting Date"].max())
date_range = st.date_input(
    "Start date",
    value=min_max_date,
    min_value=min_max_date[0],
    max_value=min_max_date[1],
)

# Wait until the user has both start and end dates
if len(date_range) == 2:
    # Convert datetime objects to strings for filtering
    date_range = [str(date_range[0]), str(date_range[1])]

    # Filter the dataframe by the date range
    df = df[df["Posting Date"].between(date_range[0], date_range[1])]
    st.dataframe(df)

    # Create a plotly line chart of balance over time
    st.markdown("## Balance over time")
    st.line_chart(data=df, x="Posting Date", y="Balance")
