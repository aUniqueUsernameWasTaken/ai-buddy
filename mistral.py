def aishit(prompt, stuffaskedbefore):
    import os
    from mistralai.client import MistralClient
    from mistralai.models.chat_completion import ChatMessage

    # Replace 'your_api_key' with your actual API key
    api_key = "158fsto70jgSJhUn6FERNxH2zcOai9fk"
    model = "mistral-large-latest"

    client = MistralClient(api_key=api_key)

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content="conversation\n#########\n"+str(stuffaskedbefore)+"\n############\nyour job is to respond appropriately according to the conversation\n###############"+prompt+"\n##########\nkeep your answer within 40 words MAX and try to aim for smaller messages please")]
    )

    print(chat_response.choices[0].message.content)

    return (chat_response.choices[0].message.content)
