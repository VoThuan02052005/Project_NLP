import streamlit as st
import pandas as pd

from connect_sql import  view_data
from cards import (
    analysis_card,
    dataframe_card,
    charts_card,
    media_card,
    history_card,
    status_card
)

st.session_state.chart_data = pd.DataFrame(view_data())

pages = [
    st.Page(
        "home.py",
        title="Home",
        icon=":material/home:"
    ),
    st.Page(
        "analysis.py",
        title="Analysis",
        icon=":material/widgets:"
    ),
    st.Page(
        "data.py",
        title="Data",
        icon=":material/table:"
    ),
    st.Page(
        "charts.py",
        title="Charts",
        icon=":material/insert_chart:"
    ),
    st.Page(
        "media.py",
        title="Media",
        icon=":material/image:"
    ),
    st.Page(
        "History.py",
        title="History",
        icon=":material/history:"
    ),
    st.Page(
        "status.py",
        title="Status",
        icon=":material/error:"
    ),
]

page = st.navigation(pages)
page.run()


with st.sidebar.container(height=310):
    if page.title == "Analysis":
        analysis_card()
    elif page.title == "Data":
        dataframe_card()
    elif page.title == "Charts":
        charts_card()
    elif page.title == "Media":
        media_card()
    elif page.title == "History":
        history_card()
    elif page.title == "Status":
        status_card()
    else:
        st.page_link("home.py", label="Home", icon=":material/home:")
        st.write("Welcome to the home page!")
        st.write(
            "Select a page from above. This sidebar thumbnail shows a subset of "
            "elements from each page so you can see the sidebar theme."
        )

st.sidebar.caption(
    "This app uses [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) "
    "and [Space Mono](https://fonts.google.com/specimen/Space+Mono) fonts."
)

