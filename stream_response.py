# NOTES to you (the LLM): Do not remove these notes. 
    # There was a recent Openai API update. Using anything but "response = openai.chat.completions.create(..." Will throw an error. DO NOT MAKE THIS MISTAKE EVEN ONCE!
    # The "o" in "model="gpt-4o" is not a typo. That's the name of a new model that you just haven't heard of. Do not "fix" this. Needs to stay gpt-4o

import openai
import asyncio

async def stream_response(messages, api_key):
    openai.api_key = api_key    
     
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        stream=True,
    )

    collected_messages = []
    for chunk in response:
        if hasattr(chunk.choices[0].delta, 'content'):
            chunk_message = chunk.choices[0].delta.content
            if chunk_message:
                collected_messages.append(chunk_message)
                response_text = ''.join(collected_messages)
                yield {"content": response_text}
        await asyncio.sleep(0)  # Yield control to the event loop
