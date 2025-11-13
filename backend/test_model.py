from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def test_hf_model():
    model_name = "microsoft/DialoGPT-medium"

    # Load tokenizer and model
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Create a text-generation pipeline
    chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

    # Test a simple input
    test_input = "Hello MindEase!"
    print(f"Sending test input: {test_input}")
    response = chatbot(test_input, max_length=50, do_sample=True)

    print("Model response:")
    print(response[0]['generated_text'])

if __name__ == "__main__":
    test_hf_model()
