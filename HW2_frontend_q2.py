'''import streamlit as st
import os
from HW2_backend_q2 import run_llm

st.title("Chatbot for finding news based on your mood")



input = st.text_area("Hello!")
generate_result = st.button("Tell Me!")
if generate_result:
    result = run_llm(str(input))
    
    
    st.write(str(result))

if generate_result:
    result = run_llm(str(input))
    
    
    st.write(str(result))
'''


import streamlit as st
import os
from HW2_backend_q2 import run_llm, run_llm2

st.title("Bot for finding news based on your mood")

# Initialize session state
if "first_press" not in st.session_state:
    st.session_state.first_press = True  # First press state

input_text = st.text_area("Hello!")
generate_result = st.button("Tell Me!")

if generate_result:
    if st.session_state.first_press:
        result = run_llm()  # First press runs run_llm()
        st.session_state.first_press = False  # Set to False after first use
    else:
        result = run_llm2(str(input_text))  # Use user input for subsequent presses
    
    st.write(str(result))  # Display the result
