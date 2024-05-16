import streamlit as st
import openai
import asyncio
from initialize_session_state import initialize_session_state
from stream_response import stream_response
from load_custom_html import load_custom_html
from get_key import get_key
from gpt_response import gpt_response
#from brain import brain
 
openai.api_key = get_key()

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'run' not in st.session_state:
    st.session_state.run = False

async def handle_streamed_input(user_input, settings):
    response_placeholder = st.empty()
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.run = True

    messages = [{"role": "user", "content": user_input}]
    full_response = ""
    
    # First streaming process with initial user input
    async for chunk in process_chunks(messages, settings, openai.api_key):
        new_content = chunk["content"][len(full_response):]
        full_response += new_content
        response_placeholder.markdown(full_response)
    
    
    #system_message = brain()
    #st.session_state.messages.append({"role": "system", "content": system_message})
    #full_response = brain(messages, api_key)
    
    ''''
    processed_string = post_process_response(full_response)
    # Second streaming process with the processed string
    messages = [{"role": "user", "content": processed_string}]
    '''
    
    
    async for chunk in process_chunks(messages, settings, openai.api_key):
        new_content = chunk["content"][len(full_response):]
        full_response += new_content
        response_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    st.session_state.run = False
    
async def process_chunks(messages, settings, api_key):    
    async for chunk in stream_response(messages, api_key):
        yield chunk

def send_message(settings):
    prompt = st.chat_input("Challenge me")
    if prompt:
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop = asyncio.get_event_loop()

        loop.run_until_complete(handle_streamed_input(prompt, settings))

def display_msgs_right_col(messages):
    for message in messages:
        st.markdown(f"##### {message['content']}")
                    
def display_messages(messages):
    skip_first_assistant = True
    for i, message in enumerate(reversed(messages)):
        if message['role'] == 'assistant':
            if skip_first_assistant:
                skip_first_assistant = False
                continue
            expander_label = f"Response {len(messages) - i}"
            with st.expander(expander_label, expanded=False):
                st.markdown(message['content'])
        elif message['role'] == 'user':
            with st.expander("You:", expanded=False):
                st.markdown(message['content'])
                                        
def main():
    settings = load_custom_html()
    initialize_session_state()

    left_column, right_column = st.columns([7, 3])

    with left_column:
        send_message(settings)
        display_messages(st.session_state.messages)

    with right_column:
        st.write("")
        custom_messages = [
            {"role": "system", "content": "Welcome! Alex built this."},
        ]
        display_msgs_right_col(custom_messages)

if __name__ == "__main__":
    main()
