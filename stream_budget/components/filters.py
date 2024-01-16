import streamlit as st
import pandas as pd


class Filters:
    """A class to handle the various streamlit filters applied to the dataframe."""

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def date_filter(self, title: str, col: str) -> list:
        min_max_date = [self.df[col].min(), self.df[col].max()]
        date_range = st.date_input(
            title,
            value=min_max_date,
            min_value=min_max_date[0],
            max_value=min_max_date[1],
        )
        return date_range

    def amount_filter(self, title: str, col: str) -> list:
        min_max_amount = [self.df[col].min(), self.df[col].max()]
        amount = st.slider(
            title,
            min_value=min_max_amount[0],
            max_value=min_max_amount[1],
            value=min_max_amount,
        )
        return amount

    def description_filter(self, title: str, col: str) -> str:
        options = self.df[col].unique()
        description = st.selectbox(title, options)
        return description

    def type_filter(self, title: str, col: str) -> str:
        options = self.df[col].unique()
        transax_type = st.selectbox(title, options)
        return transax_type

    def card_filter(self, title: str, col: str) -> str:
        options = self.df[col].unique()
        category = st.selectbox(title, options)
        return category
