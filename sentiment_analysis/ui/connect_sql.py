import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('youtube_comments', type='sql')

def view_data() :
    all_comment = conn.query('select * from comments limit 10000')
    return all_comment
