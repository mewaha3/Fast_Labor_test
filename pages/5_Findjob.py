import streamlit as st

# Page Config
st.set_page_config(page_title="Skill Input System", layout="wide")
st.title("Find Job")
st.write("Select your skills")


# Main Title
st.markdown("<h1 style='text-align: center;'>Select Your Skills</h1>", unsafe_allow_html=True)

# Predefined Skills List
skill_options = ["ทำความสะอาด", "ทำสวน", "ขนของ"]

# Initialize Session State for Skills
if "skills" not in st.session_state:
    st.session_state.skills = []

# Dropdown Menu for Skills
st.write("### Choose from Predefined Skills")
selected_skill = st.selectbox("Select a skill", skill_options, index=None, placeholder="Select a skill")

# Button to Add Selected Skill
if st.button("➕ Add Skill"):
    if selected_skill and selected_skill not in st.session_state.skills:
        st.session_state.skills.append(selected_skill)
        st.success(f"Added: {selected_skill}")
    elif selected_skill in st.session_state.skills:
        st.warning("Skill already added!")
    else:
        st.error("Please select a skill!")

# Custom Skill Input
st.write("### Or Add Your Own Skill")
custom_skill = st.text_input("Enter a skill")

if st.button("➕ Add Custom Skill"):
    if custom_skill and custom_skill not in st.session_state.skills:
        st.session_state.skills.append(custom_skill)
        st.success(f"Added: {custom_skill}")
    elif custom_skill in st.session_state.skills:
        st.warning("Skill already added!")
    else:
        st.error("Please enter a skill!")

# Display Selected Skills
if st.session_state.skills:
    st.write("### Your Selected Skills:")
    for s in st.session_state.skills:
        col1, col2 = st.columns([4, 1])
        col1.write(f"🛠 {s}")
        if col2.button("❌ Remove", key=s):
            st.session_state.skills.remove(s)
            st.experimental_rerun()
else:
    st.info("No skills selected yet. Start by choosing or adding a skill!")

# Styling
st.markdown("""
<style>
    .stSelectbox > div {
        border-radius: 10px;
        padding: 10px;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)