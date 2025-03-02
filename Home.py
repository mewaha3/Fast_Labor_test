import streamlit as st

# Set page config
st.set_page_config(page_title="User Registration System", layout="wide")

# Sidebar navigation (built-in multipage system)
st.sidebar.title("Navigation")
st.sidebar.page_link("Home.py", label="🏠 Home", icon="🏠")
st.sidebar.page_link("pages/1_Registration.py", label="📝 Registration")
st.sidebar.page_link("pages/2_Documents.py", label="📂 Document Upload")
st.sidebar.page_link("pages/3_Verification.py", label="✅ Verification")
st.sidebar.page_link("pages/4_Profile.py", label="👤 Profile")
st.sidebar.page_link("pages/5_Findjob.py", label="👤 Find Job")
st.sidebar.page_link("pages/6_Postjob.py", label="👤 Post Job")
st.sidebar.page_link("pages/7_Matchjob.py", label="👤 Payment")
# Main content for Home page
st.markdown("<h1 style='text-align: center;'>Welcome to Registration System</h1>", unsafe_allow_html=True)
st.write("Use the sidebar to navigate through the registration process.")