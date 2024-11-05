

import requests
import gradio as gr
import random

# Define the Hugging Face API URL for Falcon-7B-Instruct and your API key
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
API_KEY = "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"  # Replace with your actual Hugging Face API key

# Define the fixed question
QUESTION = "Create a creative advertisement about a new solution to the storrowing problem."

# Extensive lists of nuanced prompts for introverts and extroverts
introvert_prompts = [
    f"{QUESTION} Offer a quiet, reflective message.",
    f"{QUESTION} Develop a subtle, insightful ad.",
    f"{QUESTION} Provide a calm and thought-provoking promotional angle.",
    f"{QUESTION} Share an introspective, thoughtful ad message.",
    f"{QUESTION} Present a serene, deep advertisement concept.",
    f"{QUESTION} Propose a gentle, introspective advertisement idea.",
    f"{QUESTION} Craft a soothing and thoughtful promotional message.",
    f"{QUESTION} Design an understated, reflective ad."
] * 50  # Replicates to create a pool of 400 options when shuffled

extrovert_prompts = [
    f"{QUESTION} Provide a lively and high-energy message.",
    f"{QUESTION} Create a bold, exciting advertisement.",
    f"{QUESTION} Share an enthusiastic, vibrant ad idea.",
    f"{QUESTION} Develop a high-energy promotional concept.",
    f"{QUESTION} Propose a dynamic and thrilling ad message.",
    f"{QUESTION} Present an engaging, energetic advertisement.",
    f"{QUESTION} Craft an upbeat, extroverted promotional message.",
    f"{QUESTION} Design a compelling, lively advertisement concept."
] * 50  # Replicates to create a pool of 400 options when shuffled

# Function to query the Hugging Face API with randomness for diversity
def query_huggingface(personality):
    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Select a unique prompt variation based on personality type
    if personality == "Introvert":
        prompt = random.choice(introvert_prompts)
    elif personality == "Extrovert":
        prompt = random.choice(extrovert_prompts)

    # Make a request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    # Check if the response is successful
    if response.status_code == 200:
        # Return only the generated text
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code}, {response.text}"

# Create the Gradio interface for Introvert responses
def create_introvert_interface():
    introvert_iface = gr.Interface(
        fn=lambda _: query_huggingface("Introvert"),
        inputs=None,
        outputs="text",
        title="Introvert Profile",
        description="This interface provides an introverted, thoughtful response to the fixed question below.\n\n"
                    + QUESTION
    )
    return introvert_iface

# Create the Gradio interface for Extrovert responses
def create_extrovert_interface():
    extrovert_iface = gr.Interface(
        fn=lambda _: query_huggingface("Extrovert"),
        inputs=None,
        outputs="text",
        title="Extrovert Profile",
        description="This interface provides an extroverted, lively response to the fixed question below.\n\n"
                    + QUESTION
    )
    return extrovert_iface

# Launch the interfaces separately for two distinct links
print("Launching Introvert Interface...")
introvert_interface = create_introvert_interface()
introvert_interface.launch(server_name="0.0.0.0", server_port=7861)

print("Launching Extrovert Interface...")
extrovert_interface = create_extrovert_interface()
extrovert_interface.launch(server_name="0.0.0.0", server_port=7862)


