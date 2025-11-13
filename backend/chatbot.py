# backend/chatbot.py
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load the DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text-generation pipeline
chatbot_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_response(user_input, max_length=100):
    """
    Generates a chatbot response for a given user input.
    
    Args:
        user_input (str): The user's message.
        max_length (int): Maximum length of generated response.
    
    Returns:
        str: The chatbot's reply.
    """
    response = chatbot_pipeline(user_input, max_length=max_length, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    return response[0]['generated_text']
