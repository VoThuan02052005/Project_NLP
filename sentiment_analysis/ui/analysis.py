import streamlit as st

st.header("Analysis")
tabs = st.tabs(["Selections", "Media"])
with tabs[0]:
    cols = st.columns(3)
    with st.form(key="button_form"):
        st.subheader("Form")
        st.text_area("Text input")
        st.form_submit_button("Submit button")

    st.link_button("Link button", url="https://streamlit.io", icon=":material/open_in_new:")
    st.page_link("analysis.py", label="Page link (this page)", icon=":material/my_location:")


