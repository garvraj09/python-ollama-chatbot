import ollama

print("Chat with Llama3.2 (type 'exit' to quit)")
print("-" * 40)

messages = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )
    
    reply = response.message.content
    
    messages.append({
        "role": "assistant",
        "content": reply
    })
    
    print(f"Llama: {reply}")
    print()