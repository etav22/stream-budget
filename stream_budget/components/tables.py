import streamlit as st
import pandas as pd


def create_inflow_outflow_tables(dataframe: pd.DataFrame) -> None:
    """Creates two tables, one for inflow and one for outflow along
    with their respective totals using the streamlit metric compnent.

    Args:
            dataframe (pd.DataFrame): The dataframe to be used for the tables.
    """

    df_inflow = dataframe[dataframe["amount"] >= 0]
    df_outflow = dataframe[dataframe["amount"] < 0]
    total_inflow = round(df_inflow["amount"].sum(), 2)
    total_outflow = round(df_outflow["amount"].sum(), 2)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("## Inflow")
        st.metric(label="Total Inflow", value=f"${total_inflow:,.2f}")
        st.dataframe(df_inflow)

    with col2:
        st.markdown("## Outflow")
        st.metric(label="Total Outflow", value=f"${total_outflow:,.2f}")
        st.dataframe(df_outflow)
