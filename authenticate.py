import streamlit as st

def class1_login():
    with st.form("my_form"):
        st.write("Workshop 1 : Building a Chatbot using OpenAI LLM API")
        course_code = st.text_input("Enter your course code")
        
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            if course_code == st.secrets['class1']:
                st.success("Authenticated Successfully!")
                return True
            else:
                st.error("Please enter a valid course code")
                return False

def class0_login():
    with st.form("my_form_0"):
        st.write("Workshop 0: Introduction to Python and Basics of Programming")
        course_code = st.text_input("Enter your course code")
        
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            if course_code == st.secrets['class0']:
                st.success("Authenticated Successfully!")
                return True
            else:
                st.error("Please enter a valid course code")
                return False