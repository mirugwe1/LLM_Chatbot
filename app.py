import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat



st.set_page_config(page_title="Healthcare Chatbot powered by LLM")

with st.sidebar:
    st.title('Healthcare Chatbot')
    st.markdown('''
    Introducing our healthcare LLM-powered chatbot, specifically designed for the Ugandan context. This innovative solution aims to revolutionize the way healthcare information and support are accessed and delivered in Uganda. By leveraging the power of artificial intelligence and natural language processing, our chatbot offers an intuitive and user-friendly interface for individuals seeking reliable healthcare guidance.

This chatbot has been meticulously trained on a vast array of medical knowledge, encompassing local healthcare practices, regulations, and culturally relevant information specific to Uganda. It provides personalized assistance, answering questions, addressing concerns, and offering accurate medical advice in real-time. Whether it's general health inquiries, medication guidance, or information on local healthcare providers and services, our chatbot is here to empower Ugandan individuals with timely and reliable healthcare support.
    ''')
    add_vertical_space(5)
    st.write('Made with by [Alex Mirugwe](<https://www.mirugwe.com/>)')


if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm Ask me anything, How may I help you?"]

if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

st.title('⚕️🔗 Healthcare Chatbot')

input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()



def get_text():
    input_text = st.text_input("What would you like to know: ", "", key="input")
    return input_text

with input_container:
    user_input = get_text()


def generate_response(prompt):
    chatbot = hugchat.ChatBot()
    response = chatbot.chat(prompt)
    return response


with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))