import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

apiKey = os.getenv("API_MAKE_JSON_KEY")

if not apiKey:
    print("[ERROR] API_MAKE_JSON_KEY not found!")
    
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=apiKey,
)

def callInclusionAI(inputData):
 response = client.chat.completions.create(
  model="inclusionai/ring-2.6-1t:free",
  messages=[
          {
            "role": "user",
            "content": inputData
          }
        ],
  extra_body={"reasoning": {"enabled": True}}
 )
 
 print("--- Token Usage (รอบแรก) ---")
 print(f"Prompt Tokens: {response.usage.prompt_tokens}") 
 print(f"Completion Tokens: {response.usage.completion_tokens}")
 print(f"Total Tokens: {response.usage.total_tokens}\n")
 response = response.choices[0].message
 return response.content


 
 

 