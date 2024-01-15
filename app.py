import streamlit as st
import pandas as pd
from stream_budget.components.filters import Filters

st.set_page_config(layout="wide")
st.title("Stream-Budget")

# Get data and apply preprocessing
df = pd.read_csv("data/transactions.csv", index_col=False).reset_index(drop=True)
df = df.drop(columns=["Check or Slip #"])
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
df["posting_date"] = pd.to_datetime(df["posting_date"], format="%m/%d/%Y").dt.date


st.markdown("## Transactions")

with st.sidebar:
    st.markdown("## Filters")
    filter = Filters(dataframe=df)

    date_range = filter.date_filter("Date Range", col="posting_date")
    amount = filter.amount_filter("Amount Range", col="amount")
    description = filter.description_filter("Description", col="description")
    card = filter.card_filter("Card", col="details")
    transax_type = filter.type_filter("Type", col="type")

    btn = st.button("Filter", use_container_width=True)

if btn:
    # Filter the dataframe based on the user's selections
    df = df[
        (df["type"] == transax_type)
        & (df["details"] == card)
        & (df["posting_date"].between(date_range[0], date_range[1]))
        & (df["amount"].between(amount[0], amount[1]))
    ]

    st.dataframe(df)
else:
    st.dataframe(df)

# Create a plotly line chart of balance over time
st.markdown("## Balance over time")
st.line_chart(data=df, x="posting_date", y="balance")
