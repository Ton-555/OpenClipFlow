import os
import sys
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv(find_dotenv())

apiKey = os.getenv("API_MAKE_JSON_KEY3")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = apiKey
)
def callQwenAI(inputData):
 full_response = ""
 completion = client.chat.completions.create(
  model="qwen/qwen3-coder-480b-a35b-instruct",
  messages=[{"role":"user","content":inputData}],
  temperature=0.7,
  top_p=0.8,
  max_tokens=4096,
  stream=True
 )

 for chunk in completion:
   if chunk.choices and chunk.choices[0].delta.content is not None:
     print(chunk.choices[0].delta.content, end="")
     full_response += chunk.choices[0].delta.content # 2. สะสมข้อความไว้

 return full_response