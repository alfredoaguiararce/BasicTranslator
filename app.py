import streamlit as st
import openai
import os
from dotenv import load_dotenv, find_dotenv
import json
import pandas as pd

_ = load_dotenv(find_dotenv()) # read local .env file

# You can use other name defined in the .env file
key_name = 'OPENAI_API_KEY'
openai.api_key  = os.getenv(key_name)

# Prompts
_input_text = None

# The `_inferring_prompt` variable is a string that prompts the user to determine the sentiment of a
# given text. The text is represented by the variable `_txt_inferring`, which is enclosed in triple
# backticks.
def get_translation(input_text):
    return  f"""
                What is the translation to English, Spanish, Chinese and korean in that order for the text
                which is delimited with triple backticks? please response in json format

                text: '''{input_text}'''
                """

def get_completion(prompt, model="gpt-3.5-turbo-16k", temperature=0):
    """
    This function uses OpenAI's chat completion API to generate a response to a given prompt using a
    specified model and temperature.
    
    :param prompt: The text prompt or message that you want to send to the OpenAI chatbot for completion
    :param model: The name of the OpenAI language model being used for text generation. In this case, it
    is set to "gpt-3.5-turbo-16k", defaults to gpt-3.5-turbo-16k (optional)
    :param temperature: The temperature parameter controls the degree of randomness or creativity in the
    model's output. A higher temperature value will result in more diverse and unexpected responses,
    while a lower temperature value will result in more conservative and predictable responses. The
    default value is 0, which means the model will always output the most likely, defaults to 0
    (optional)
    :return: The function `get_completion` returns a string, which is the response generated by the
    OpenAI chatbot model based on the given prompt.
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

st.header("Message GenGpt")
st.divider()
_input_text = st.text_area('Write your message : ', '')

if st.button('Translate'):
    st.divider()
    try:
        with st.spinner('Wait for it...'):
            response = get_completion(get_translation(_input_text), temperature=0)
            # Parse the JSON object
            st.success('Done!')

            translations = json.loads(response)

            # Convert the data to a DataFrame for easy display
            df = pd.DataFrame(translations.items(), columns=["Language", "Translation"])

            # Streamlit app
            st.title("Translation Table")
            # Display the table
            st.write(df)
            
            st.title("Json response")
            st.write(translations)
        
    except Exception as e:
        st.error(f'This is an error : {e}', icon="🚨")

