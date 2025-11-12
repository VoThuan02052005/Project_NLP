import streamlit as st
from cards import (
    analysis_card,
    dataframe_card,
    charts_card,
    media_card,
    history_card,
    status_card
)

st.title("Element explorer")

st.markdown(
    "This app displays most of Streamlit's built-in elements so you can "
    "conveniently explore how they look with different theming configurations "
    "applied."
)

cols = st.columns(2)
with cols[0].container(height=310):
    analysis_card()
with cols[1].container(height=310):
    dataframe_card()
with cols[0].container(height=310):
    charts_card()
with cols[1].container(height=310):
    media_card()
with cols[0].container(height=310):
    history_card()
with cols[1].container(height=310):
    status_card()
