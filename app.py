import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Stream-Budget")

# Get data and convert the date column to datetime objects
df = pd.read_csv("data/transactions.csv", index_col=False).reset_index(drop=True)
df = df.drop(columns=["Check or Slip #"])
df["Posting Date"] = pd.to_datetime(df["Posting Date"], format="%m/%d/%Y").dt.date
st.markdown("## Transactions")

with st.sidebar:
    st.markdown("## Filters")
    min_max_date = [df["Posting Date"].min(), df["Posting Date"].max()]
    min_max_amount = [df["Amount"].min(), df["Amount"].max()]
    date_range = st.date_input(
        "Start date",
        value=min_max_date,
        min_value=min_max_date[0],
        max_value=min_max_date[1],
    )
    amount = st.slider(
        "Transaction Amount",
        min_value=df["Amount"].min(),
        max_value=df["Amount"].max(),
        value=min_max_amount,
    )
    description = st.selectbox("Description", df["Description"].unique())
    card = st.selectbox("Card", df["Details"].unique())
    transax_type = st.selectbox("Transaction Type", df["Type"].unique())
    btn = st.button("Filter", use_container_width=True)

if btn:
    # Filter the dataframe based on the user's selections
    df = df[df["Type"] == transax_type]
    df = df[df["Details"] == card]
    df = df[df["Posting Date"].between(date_range[0], date_range[1])]
    df = df[df["Amount"].between(amount[0], amount[1])]

    st.dataframe(df)
else:
    st.dataframe(df)

# Create a plotly line chart of balance over time
st.markdown("## Balance over time")
st.line_chart(data=df, x="Posting Date", y="Balance")
