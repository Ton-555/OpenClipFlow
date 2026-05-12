import ollama

def callLocalAI(inputData, modelName):
    messages = [
        {
            'role': 'user',
            'content': inputData,
        }
    ]
    
    response = ollama.chat(model=modelName, messages=messages, stream=True)
    full_response = ""
    for chunk in response:
        
        content = ""
        if hasattr(chunk, 'message'):
            content = chunk.message.content
        elif isinstance(chunk, dict):
            content = chunk.get("message", {}).get("content", "")
            
        if content:
            full_response += content
            
    return full_response