import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="Work Confirmation", layout="wide")

# Main Title
st.markdown("<h1 style='text-align: center;'>Work Confirmation Page</h1>", unsafe_allow_html=True)

# Sample Employees & Employers
employees = ["John Doe", "Jane Smith", "Ali Khane"]
employers = ["Company A", "Company B", "Company C"]

# Form Inputs
st.write("### Select Employee & Employer")
col1, col2 = st.columns(2)

with col1:
    selected_employee = st.selectbox("Choose an Employee", employees, index=None, placeholder="Select an employee")

with col2:
    selected_employer = st.selectbox("Choose an Employer", employers, index=None, placeholder="Select an employer")

job_description = st.text_area("Job Description", placeholder="Enter job details here...")

# Initialize Session State for Confirmations
if "confirmations" not in st.session_state:
    st.session_state.confirmations = []

# Confirm Button
if st.button("✅ Confirm Agreement"):
    if selected_employee and selected_employer and job_description:
        new_confirmation = {
            "Employee": selected_employee,
            "Employer": selected_employer,
            "Job Description": job_description,
            "Status": "Pending"
        }
        st.session_state.confirmations.append(new_confirmation)
        st.success(f"Confirmation Submitted for {selected_employee} & {selected_employer}")
    else:
        st.error("Please fill in all fields!")

# Display Confirmation Table
if st.session_state.confirmations:
    st.write("### Pending Confirmations:")
    df = pd.DataFrame(st.session_state.confirmations)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No confirmations yet. Fill out the form above to submit.")

# Styling
st.markdown("""
<style>
    .stTextArea > div {
        border-radius: 10px;
        padding: 10px;
    }
    .stSelectbox > div {
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #008CBA;
        color: white;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)