import os
import sys
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Force UTF-8 encoding for stdout to handle Thai characters and symbols
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv(find_dotenv())

apiKey = os.getenv("API_MAKE_JSON_KEY2")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = apiKey
)

def callMinMaxAI(inputData):  
 full_response = "" # <--- สำคัญมาก: ต้องเพิ่มบรรทัดนี้เพื่อเริ่มสะสมคำตอบ
 completion = client.chat.completions.create(
 model="minimaxai/minimax-m2.7",
  messages=[{"role":"user","content":inputData}],
  temperature=0,
  top_p=0.95,
  max_tokens=8192,
  stream=True,
  response_format={"type": "json_object"}  
 )

 for chunk in completion:
   if not getattr(chunk, "choices", None):
     continue
   if chunk.choices[0].delta.content is not None:
     print(chunk.choices[0].delta.content, end="")
     full_response += chunk.choices[0].delta.content # 2. สะสมข้อความไว้

 return full_response
