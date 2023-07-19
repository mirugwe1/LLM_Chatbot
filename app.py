import os
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

from langchain.llms import OpenAI


os.environ['OPENAI_API_KEY'] = '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'


# Set page configuration
st.set_page_config(page_title="Healthcare Chatbot powered by LLM")

# Sidebar
with st.sidebar:
    st.title('Healthcare Chatbot')
    st.markdown(
        '''
        Introducing our healthcare LLM-powered chatbot, specifically designed for the Ugandan context. 
        This innovative solution aims to revolutionize the way healthcare information and support are accessed 
        and delivered in Uganda. By leveraging the power of artificial intelligence and natural language processing, 
        our chatbot offers an intuitive and user-friendly interface for individuals seeking reliable healthcare guidance.
        
        This chatbot has been meticulously trained on a vast array of medical knowledge, encompassing local healthcare 
        practices, regulations, and culturally relevant information specific to Uganda. It provides personalized assistance, 
        answering questions, addressing concerns, and offering accurate medical advice in real-time. Whether it's general 
        health inquiries, medication guidance, or information on local healthcare providers and services, our chatbot 
        is here to empower Ugandan individuals with timely and reliable healthcare support.
        '''
    )
    add_vertical_space(3)
    st.write('Made with ❤️ by [Alex Mirugwe](https://www.mirugwe.com/)')

# Main content
st.title('⚕️ Healthcare Chatbot 🩺')
colored_header(label='', description='', color_name='blue-80')

input_container = st.container()
response_container = st.container()


input_text = st.text_input("What would you like to know?", "", key="input")



llm = OpenAI(temperature=0.1)

if input_text:
    response = llm(input_text)
    st.write(response)


