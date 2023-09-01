# Streamlit Translation App Documentation

This is a Streamlit web application for translating text messages into English, Spanish, Chinese, and Korean simultaneously using the OpenAI GPT-3.5 Turbo language model. Users can input a message, and the app will provide translations in multiple languages.

## Prerequisites

Before using this application, ensure you have the following:

- Python installed on your system.
- Required Python packages installed. You can install them using `pip install -r requirements.txt`, which will install the packages listed in the `requirements.txt` file.

## Getting Started

1. Clone or download the script to your local machine.

2. Create a `.env` file in the same directory as the script and add your OpenAI API key as follows:

    ```plaintext
    OPENAI_API_KEY=your_api_key_here
    ```

3. Install the required packages by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app by executing the script using the command :

    ```bash
    streamlit run app.py
    ```

## Application Usage

### Input

- Write your message in the provided text area.

### Translation

- Click the "Translate" button to initiate the translation process.

### Output

The app will display the translations in two formats:

1. **Translation Table**: A table displaying translations in different languages.

2. **Json response**: The raw JSON response containing translations.

## Function Documentation

### `get_translation(input_text)`

This function generates a prompt for translation based on the input text.

- `input_text` (str): The text that the user wants to translate.

### `get_completion(prompt, model="gpt-3.5-turbo-16k", temperature=0)`

This function uses the OpenAI chat completion API to generate a response to a given prompt using a specified model and temperature.

- `prompt` (str): The text prompt or message to send to the OpenAI chatbot for completion.
- `model` (str, optional): The name of the OpenAI language model being used for text generation. Default is "gpt-3.5-turbo-16k".
- `temperature` (float, optional): The degree of randomness or creativity in the model's output. Default is 0.

## Acknowledgments

- This application uses the OpenAI GPT-3.5 Turbo language model for text translation.
- It was created using the Streamlit framework.

---

**Note**: Please keep your OpenAI API key confidential and do not share it with others.
