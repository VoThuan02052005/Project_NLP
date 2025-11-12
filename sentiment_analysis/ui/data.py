import streamlit as st

chart_data = st.session_state.chart_data
st.header("Data elements")

display_type = st.segmented_control("Display type", ["Raw data", "Data clean"], default="Raw data")

cols = st.columns(3)
event = None
if display_type == "Raw data":
    st.info("YouTube comment data.")
    event = st.dataframe(chart_data, use_container_width=True, on_select="rerun", selection_mode="multi-row")
elif display_type == "Data clean":
    st.data_editor(chart_data, num_rows="dynamic", use_container_width=True)

