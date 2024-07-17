def aishit(prompt):
    import os
    from mistralai.client import MistralClient
    from mistralai.models.chat_completion import ChatMessage

    # Replace 'your_api_key' with your actual API key
    api_key = "APIKEY"
    model = "mistral-large-latest"

    client = MistralClient(api_key=api_key)

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt+"\n##########\nkeep your answer within 40 words MAX and try to aim for smaller messages please")]
    )

    print(chat_response.choices[0].message.content)

    return (chat_response.choices[0].message.content)
