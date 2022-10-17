import streamlit as st
import pandas as pd
import numpy as np

st.markdown("#  Encryption")
st.sidebar.markdown("# Encryption Techniques")


# SIDEBAR

with st.sidebar:
    # st.write("The following list won’t indent no matter what I try:")
    st.markdown("- Vigenère")
    st.markdown("- Playfair")
    st.markdown("- Railfence")


# DROPDOWN MENU

encrypt = ["Vigenère", "Playfair"]

option = st.selectbox(
    'Choose your encryption technique',
    encrypt
)



# Vigenere Cipher (text, Key, transformed_text)

if option == "Vigenère":

    st.caption(""" The Vigenère cipher is a method of encrypting alphabetic text by 
    using a series of interwoven Caesar ciphers, based on the letters of a keyword. 
    It employs a form of polyalphabetic substitution.
    """)



    # Text Area or File Upload

    st.text_area("Enter Text", key = "plain_text", placeholder="")    # st.session_state.text

    st.caption("OR")

    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)



    # Key

    col1, col2 = st.columns([2,3])
    with col1:
        Key = st.text_input("Key", value = "LEMON")    # Key
    with col2:
        pass



    # Submit Button

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1:
        pass
    with c2:
        pass
    with c3:
        pass
    with c4:
        pass
    with c5:
        pass
    with c6:
        btn_result = st.button("Submit")



    # Button Function

    if btn_result:
        cipher_text = "AFDFSF"
        st.write("Cipher Text")
        st.code(cipher_text)

    

    # st.subheader("Details")
    # st.write("Text: ", st.session_state.plain_text)
    # st.write("Key: ", Key)
    # st.write("Transformed Text: ", cipher_text)









# HIDE 'hamburger-menu' AND 'made with streamlit'

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 