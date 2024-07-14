from transformers import pipeline

# Initialize the text generation pipeline with my model
conversation = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# Prepare the input for the model
input_text = "Hey Franek, how are you?"

# Generate a response
response = conversation(input_text, max_length=100, do_sample=True)

# Print the generated response
print(response[0]['generated_text'].strip())
