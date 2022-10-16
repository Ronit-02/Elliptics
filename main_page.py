import streamlit as st
import pandas as pd
import numpy as np

st.markdown("#  Main Page")
st.sidebar.markdown("# Main Page")



# DROPDOWN MENU

encrypt = ["playfair", "vigenere"]
option = st.selectbox(
    'Choose your encryption technique',
    encrypt
)



# Vigenere Cipher (text, Key, transformation_type, transformed_text)

if option == "vigenere":
    st.text_input("Text", key = "text")    # st.session_state.text
    st.text_input("Key", key = "Key")    # st.session_state.Key
    transformation_type = st.radio(
        "",('Encrypt', 'Decrypt')
    )

    transformed_text = ""

    st.subheader("Details")
    st.write("Text: ", st.session_state.text)
    st.write("Key: ", st.session_state.Key)
    st.write("Transformed Text: ", transformed_text)







# HIDE 'hamburger-menu' AND 'made with streamlit'

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 