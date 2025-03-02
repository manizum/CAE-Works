import streamlit as st

# Page Configuration
st.set_page_config(page_title="Centered Button", page_icon="😔", layout="wide")

# Custom CSS for Centering Button & Styling Background
st.markdown("""
    <style>
        body {
            background-color: #f7d9e3; /* Soft Pink Background */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .stButton > button {
            display: block;
            margin: auto;
            background-color: #ff4b4b;
            color: white;
            border-radius: 12px;
            font-size: 120px;
            padding: 110px 124px;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #ff1c1c;
        }
        .sorry-text {
            text-align: center;
            font-size: 250px;
            font-weight: bold;
            color: #990000;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Centering the Button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Click Me"):
    st.markdown("<p class='sorry-text'>Sorry Babes! 😔</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)