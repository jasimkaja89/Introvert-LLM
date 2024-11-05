import os
import requests
import gradio as gr
import random

# Define the Hugging Face API URL and retrieve the API key from environment variables
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Define the fixed question
QUESTION = "Create a creative advertisement about a new solution to the storrowing problem."

# Nuanced introvert prompts
introvert_prompts = [
    f"{QUESTION} Offer a quiet, reflective message.",
    f"{QUESTION} Develop a subtle, insightful ad.",
    f"{QUESTION} Provide a calm and thought-provoking promotional angle.",
    f"{QUESTION} Share an introspective, thoughtful ad message.",
    f"{QUESTION} Present a serene, deep advertisement concept.",
    f"{QUESTION} Propose a gentle, introspective advertisement idea.",
    f"{QUESTION} Craft a soothing and thoughtful promotional message.",
    f"{QUESTION} Design an understated, reflective ad."
] * 50  

# Function to query the Hugging Face API
def query_huggingface():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    prompt = random.choice(introvert_prompts)
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code}, {response.text}"

# Create Gradio interface
def create_introvert_interface():
    return gr.Interface(
        fn=query_huggingface,
        inputs=None,
        outputs="text",
        title="Introvert Profile",
        description="This interface provides an introverted, thoughtful response to the fixed question below.\n\n" + QUESTION
    )

# Launch interface
create_introvert_interface().launch(server_name="0.0.0.0", server_port=7865)



