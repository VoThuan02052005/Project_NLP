import streamlit as st

def analysis_card():
    st.page_link("analysis.py", label="Analysis", icon=":material/widgets:")
    st.text_input("Text input")

def dataframe_card():
    st.page_link("data.py", label="Data", icon=":material/table:")
    st.dataframe(st.session_state.chart_data, height=220)

def charts_card():
    st.page_link("charts.py", label="Charts", icon=":material/insert_chart:")


def media_card():
    st.page_link("media.py", label="Media", icon=":material/image:")
    st.video("https://www.youtube.com/watch?v=cnHHCR7EW10&list=RDMMNrSkiem0t8I&index=4", autoplay=True)


def history_card():
    st.page_link("History.py", label="History", icon=":material/history:")
    st.chat_message("user").write("Hello, world!")
    st.chat_message("assistant").write("Hello, user!")
    st.chat_input("Type something")

def status_card():
    st.page_link("status.py", label="Status", icon=":material/error:")
    cols = st.columns(2)
    cols[0].error("Error")
    cols[0].warning("Warning")
    cols[1].info("Info")
    cols[1].success("Success")