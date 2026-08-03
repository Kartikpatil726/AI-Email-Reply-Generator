import streamlit as st
from utils import generate_replies

st.set_page_config(page_title="AI Email Reply Generator", page_icon="✉️")
st.title("✉️ AI Email Reply Generator")

email_text = st.text_area("Paste the email you received:", height=200)
tone = st.selectbox("Select reply tone:", ["Professional", "Friendly", "Formal", "Casual"])

if st.button("Generate Replies"):
    if email_text.strip() == "":
        st.warning("Please paste an email first.")
    else:
        with st.spinner("Generating replies..."):
            replies = generate_replies(email_text, tone)
        st.markdown(replies)