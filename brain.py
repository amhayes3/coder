from gpt_response import gpt_response
from settings_to_system_prompt import settings_to_system_prompt

def brain(messages, settings, api_key):
    internal_messages = messages
    
    original_system_instructions = settings_to_system_prompt(settings)

    prompt = (
        f"System instructions: \n {original_system_instructions} \n --------------------\n"
        f"Consider the previous message history. Were the instructions followed?"
        f""
        f""
    )
    
    

    messages.append({"role": "system", "content": prompt})

    
    response = gpt_response(prompt)
    return system_message