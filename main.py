import streamlit as st
from tabnanny import check
import resources.caesar as cs
import resources.playfair as pf
import resources.rsa as rsa
import resources.vigenere as vig
import resources.railfence as rf


st.markdown("# ELLIPTICS")


# SIDEBAR

selected_type = st.sidebar.selectbox("Select a type", ("Encryption", "Decryption"))
selected_technique = st.sidebar.selectbox("Select a technique", ("Vigenère", "PlayFair", "Caesar",  "RSA", "Rail Fence"))



# Vigenere Cipher (text, Key, transformed_text)

if selected_technique == "Vigenère":

    st.caption(""" Vigenère cipher is a method of encrypting alphabetic text by 
    using a series of interwoven Caesar ciphers, based on the letters of a keyword. 
    It employs a form of polyalphabetic substitution.
    """)


    # Text Area or File Upload

    key = st.text_area(
            "Enter key:", help="The key text for encryption.", height=45)

    input_type_text = st.selectbox(
        label="Select input type for TEXT",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )

    if input_type_text == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The text file to encrypt.")
        if file is not None:
            text = file.getvalue().decrypt("utf-8")


    # Start Button

    if st.button("Start"):
        if text.strip() != "":
            
            if selected_type == "Encryption":
                "Encrypted Text"
                print(key,text)
                st.code(vig.Encryption(text,key))    
            else: 
                "Decrypted Text"
                print(key,text)
                st.code(vig.Decryption(text,key))

        else:
            st.error("Please enter text.")

if selected_technique == "Caesar":

    st.caption(""" Caesar cipher is a is a type of substitution cipher 
    in which each letter in the plaintext is replaced by a letter some 
    fixed number of positions down the alphabet.
    """)


    # Text Area or File Upload

    input_type = st.selectbox(
        label="Select input type",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )

    if input_type == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The file to encrypt.")
        if file is not None:
            text = file.getvalue().decrypt("utf-8")


    # Shift Value

    col1, col2 = st.columns([2,3])
    with col1:
        shift_by = st.number_input(
        label="Enter a shift value:", step=1, help="Number of bits to shift each bit with."
    )
    with col2:
        pass

    
    # Start Button

    if st.button("Start"):
        if text.strip() != "":
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(cs.encrypt(text, shift_by))    
            else: 
                "Decrypted Text"
                st.code(cs.decrypt(text, shift_by))
        else:
            st.error("Please enter text.")


if selected_technique == "PlayFair":

    st.caption(""" Playfair cipher is a manual symmetric encryption technique 
    and was the first literal digram substitution cipher.
    """)


    # Text Area or File Upload

    
    key = st.text_area(
            "Enter key:", help="The key text for encryption.", height=45)

    input_type_text = st.selectbox(
        label="Select input type for TEXT",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )

    if input_type_text == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The text file to encrypt.")
        if file is not None:
            text = file.getvalue().decrypt("utf-8")


    # Start Button

    if st.button("Start"):
        if text.strip() != "":
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(pf.encrypt(key, text))    
            else: 
                "Decrypted Text"
                st.code(pf.decrypt(key, text))

        else:
            st.error("Please enter text.")

if selected_technique == 'RSA':

    st.caption(""" RSA is a public-key cryptosystem that is widely used for 
    secure data transmission. It is also one of the oldest.
    """)

    # P and Q Value

    col1, col2, col3 = st.columns(3)
    with col1:
        p = st.number_input(
        label="P value:", step=1, help="Number of bits to shift each bit with.")
    with col2:
        q = st.number_input(
        label="Q value:", step=1, help="Number of bits to shift each bit with.")
    with col3:
        val = (p-1)*(q-1)
        e = st.number_input(
        label="E value:", step=1, help=f"Enter e such that it is co-prime to {val}. eg: {val+1}")

    # phi = (p-1)*(q-1)
    # def gcd(a, b):
    #     while b != 0:
    #         a, b = b, a % b
    #     return a
    # e = random.randrange(1, phi)
    # res = gcd(e, phi)

    # while res != 1:
    #     e = random.randrange(1, phi)
    #     res = gcd(e, phi)
    
    # Text Area or File Upload

    input_type = st.selectbox(
        label="Select input type for text",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )

    if input_type == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45   )
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The file to encrypt.")
        if file is not None:
            text = file.getvalue().decrypt("utf-8")

    # Start Button

    if st.button("Start"):
        check_p = rsa.prime_check(p)
        check_q = rsa.prime_check(q)
        check_e = rsa.co_prime_check(e,p,q)
        if(p == q):
            st.error("Value of P and Q should not be equal")
        if(check_p==False):
            st.error("Please enter prime value of P.")
        if(check_q==False):
            st.error("Please enter prime value of Q.")
        if(check_e==False):
            st.error(f"Please enter co-prime value of E. Eg: {(p-1)*(q-1)+1}")

        if text.strip() != "":
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(rsa.Encrypt(p,q,e,text))    
            else: 
                "Decrypted Text"
                st.code(rsa.Decrypt(p,q,e,text))
        else:
            st.error("Please enter text.")


if selected_technique == "Rail Fence":
    # st.markdown("# Rail Fence")
    st.caption(""" The rail fence cipher is a classical type of transposition cipher. 
    It derives its name from the manner in which encryption/decryption is performed, 
    in analogy to a fence built with horizontal rails.
    """)


    # Text Area or File Upload

    input_type = st.selectbox(
        label="Select input type",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )

    if input_type == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The file to encrypt.")
        if file is not None:
            text = file.getvalue().decode("utf-8")


    # Shift Value

    col1, col2 = st.columns([2,3])
    with col1:
        shift_by = st.number_input(
        label="Enter a integer key:", step=1, help="Number of rows."
    )
    with col2:
        pass

    
    # Start Button

    if st.button("Start"):
        if text.strip() != "":
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(rf.encrypt(text, shift_by))    
            else: 
                "Decrypted Text"
                st.code(rf.decrypt(text, shift_by))
        else:
            st.error("Please enter text.")



# HIDE 'hamburger-menu' AND 'made with streamlit'

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)