# Text Summarization API

This repository contains a Flask-based API that provides text summarization using IBM Watsonx's Granite language model (`ibm/granite-13b-chat-v2`). The API accepts text input, processes it through the Granite model, and returns a concise summary of the provided text.

## Features
- **Text Summarization**: Condenses large volumes of text into coherent and concise summaries.
- **IBM Watsonx AI**: Utilizes IBM's Granite model for high-quality and context-aware summarization.
- **Customizable Summarization**: Summarization can be adapted for different use cases like academic research, business intelligence, or content curation.

## Requirements

- Python 3.x
- IBM Watsonx AI SDK
- Flask

Install the necessary packages by running:

```bash
pip install flask ibm-watsonx-ai
```

## Configuration

Update the `get_credentials()` function with your IBM Cloud API key:

```python
def get_credentials():
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": "<your-api-key-here>"
    }
```
The model used is `ibm/granite-13b-chat-v2`. <br>
<br>
**Parameters**: The model uses specific parameters for generating the text:
```python
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 900,
    "repetition_penalty": 1.05
}
```
Replace the project id with your own:
```python
project_id = '0d904006-f1fa-46fd-b5bf-9eeef2ceaca3'
```
**Once the credentials and model configuration are set, the summarization function can be used to generate summaries based on input text.**
