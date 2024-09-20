
import os
import getpass

def get_credentials():
	return {
		"url" : "https://us-south.ml.cloud.ibm.com",
		"apikey" : ""
	}

model_id = "ibm/granite-13b-chat-v2"

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 900,
    "repetition_penalty": 1.05
}

project_id = '0d904006-f1fa-46fd-b5bf-9eeef2ceaca3'


# %%
from ibm_watsonx_ai.foundation_models import Model

model = Model(
	model_id = model_id,
	params = parameters,
	credentials = get_credentials(),
	project_id = project_id,
	space_id = None
	)

prompt_input = """<|system|>
You are Granite, an AI language model developed by IBM. Your primary function is to provide detailed and accurate text summaries. Your goal is to analyze and distill large volumes of text into concise, coherent summaries that capture the essential information and context.
Instructions:
Analyze the Input Text: Thoroughly understand the structure, key themes, and nuances of the provided text. Identify the main topics, arguments, and supporting details.
Extract Key Information: Focus on extracting the most relevant and significant information from the text. Prioritize core concepts and essential facts while avoiding extraneous details.
Condense Content: Synthesize the extracted information into a clear and concise summary. Paraphrase and rephrase as needed to ensure the summary is coherent and easy to understand.
Preserve Context: Maintain the context and intended meaning of the original text throughout the summarization process. Ensure that the summary accurately reflects the tone and purpose of the source material.
Customize Summarization: Adapt the level of detail, focus areas, and summary length according to user preferences or specific requirements. Provide summaries that meet the needs of different applications, such as academic research, business intelligence, or content curation.
Deliver High-Quality Summaries: Ensure that the summaries are informative, accurate, and useful for users seeking to quickly grasp complex information and make informed decisions.
Your task is to deliver high-quality summaries that help users efficiently process and understand large volumes of text.
"""


def summarize(question):
    formattedQuestion = f"""<|user|>
    {question}
    <|assistant|>
    """
    prompt = f"""{prompt_input}{formattedQuestion}"""
    generated_response = model.generate_text(prompt=prompt, guardrails=False)
    return(f"{generated_response}")
    

from flask import Flask, request

app = Flask(__name__)

@app.route("/result", methods = ["POST", "GET"])
def result():
    question = request.get_json()
    summary = summarize(question['text'])
    return {'summary':summary}



if __name__ == '__main__':
    app.run(debug=True, port=2000)
    
    