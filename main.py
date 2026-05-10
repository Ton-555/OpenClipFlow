from inclusionAI import callInclusionAI 
from minmax import callMinMaxAI
from qwen import callQwenAI
import json
import sys

# Force UTF-8 for main.py
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

dataRawInput = """
หัวข้อ: การทำงานร่วมกันระหว่างมนุษย์และเอไอเอเจนท์ (Human-AI Agent Collaboration)

หัวข้อนี้ไม่ใช่แค่การพิมพ์แชทกับ AI ทั่วไป แต่เป็นการเรียนรู้วิธี "กำกับดูแล" และ "ร่วมงาน" กับ AI Agents ที่สามารถทำงานแทนเราได้โดยอัตโนมัติ (Autonomous Agents) ซึ่งเป็นทักษะที่สำคัญมากในปัจจุบัน

ขั้นตอนการเรียนรู้แบบเร่งรัด

ทำความรู้จัก AI Agents: ทำความเข้าใจความต่างระหว่าง AI ทั่วไป (Chatbot) กับ AI Agent (ระบบที่สามารถวางแผน ตัดสินใจ และใช้เครื่องมืออื่นๆ แทนเราได้)

การออกแบบ Agentic Workflow: ศึกษากระบวนการคิดของเอไอ เช่น การทำ Chain-of-Thought (การคิดเป็นลำดับขั้นตอน) และการตรวจสอบความถูกต้องด้วยตัวเอง (Self-reflection)

เครื่องมือที่ใช้: ลองสำรวจ Framework ยอดนิยม เช่น LangChain หรือ CrewAI ซึ่งใช้ในการสร้างทีมเอไอมาช่วยทำงานเฉพาะทาง

ความปลอดภัยและจริยธรรม (Agentic Security): เรียนรู้วิธีป้องกันไม่ให้เอไอทำงานผิดพลาดหรือถูกโจมตีผ่านคำสั่ง (Prompt Injection) ขณะที่มันกำลังทำงานอัตโนมัติ

"""

configPromt =""" [คำสั่ง: ช่วยแปลงข้อมูลที่ได้รับก่อนหน้านี้ให้เป็น JSON ที่มีโครงสร้างแบบนี้และผลลัพธ์ที่ได้คือ JSON เท่านั้น ห้ามมีข้อความอื่นพร้อม copy ได้.json และห้ามใช้ EMOJI ใดๆ ใน JSON !]
{
  "title": "สรุปสถานการณ์ Geopolitical Resiliency 2026",
  "scenes": [
    {
      "id": 1,
      "voiceover": "ในปัจจุบัน สหรัฐฯ กำลังเผชิญกับสภาวะ Geopolitical Resiliency หรือความยืดหยุ่นท่ามกลางวิกฤตภูมิรัฐศาสตร์ โดยมี AI และพลังงานเป็นแรงขับเคลื่อนสำคัญ",
      "visual_prompt": "Cinematic shot of a futuristic US map with glowing energy lines and digital AI data streams, high-tech command center background, deep blue and amber lighting, vertical 9:16 format, 8k resolution",
      "duration": null,
      "subtitle": "Geopolitical Resiliency: ความยืดหยุ่นท่ามกลางวิกฤตภูมิรัฐศาสตร์"
    },
    {
      "id": 2,
      "voiceover": "ความคืบหน้าของข้อตกลงหยุดยิงระหว่างสหรัฐฯ และอิหร่าน ช่วยให้ช่องแคบฮอร์มุซกลับมาเปิดได้อีกครั้ง แม้จะยังมีการปะทะย่อยๆ ในอ่าวเปอร์เซียอยู่บ้าง",
      "visual_prompt": "Aerial view of cargo ships moving through the Strait of Hormuz at sunset, naval escort ships in the distance, realistic cinematic style, warm lighting, vertical 9:16 format",
      "duration": null,
      "subtitle": "ข้อตกลงหยุดยิงสหรัฐฯ-อิหร่าน และการเปิดช่องแคบฮอร์มุซ"
    },

    {
      "id": 3,
      "voiceover": "ด้านการเมืองภายใน รัฐบาลภายใต้ประธานาธิบดีทรัมป์กำลังเผชิญกับการเลือกตั้งกลางเทอมในเดือนพฤศจิกายนนี้ ส่งผลให้โยบายการค้ามีความผันผวน",
      "visual_prompt": "The White House during twilight, American flags waving, digital overlay of election polling charts and tax symbols, professional news aesthetic, vertical 9:16 format",
      "duration": null,
      "subtitle": "การเมืองภายในและการเลือกตั้งกลางเทอมปี 2026"
    },
    {
      "id": 4,
      "voiceover": "ตลาดหุ้นสหรัฐฯ พุ่งทำจุดสูงสุดใหม่ โดย S&P 500 และ Nasdaq ได้แรงหนุนจากกลุ่มเทคโนโลยี AI และผลประกอบการบริษัทที่แข็งแกร่งเกินคาด",
      "visual_prompt": "Stock market dashboard showing S&P 500 and Nasdaq at 'All-Time High', glowing green numbers, financial District of New York in the background, bokeh effect, vertical 9:16 format",
      "duration": null,
      "subtitle": "S&P 500 และ Nasdaq ทำระดับสูงสุดเป็นประวัติการณ์"
    },
    {
      "id": 5,
      "voiceover": "ด้านนโยบายการเงิน คาดว่าธนาคารกลางสหรัฐฯ จะคงอัตราดอกเบี้ยไว้ที่ 3.50 ถึง 3.75 เปอร์เซ็นต์ ท่ามกลางตลาดแรงงานที่ยังคงแข็งแกร่ง",
      "visual_prompt": "Federal Reserve building with a digital interest rate graphic showing 3.50%-3.75%, stylized financial stability icons, clean corporate aesthetic, vertical 9:16 format",
      "duration": null,
      "subtitle": "Fed คาดคงดอกเบี้ยที่ 3.50% - 3.75% ถึงสิ้นปี"
    }
  ]
}
"""


print("selec model")
print("1. inclusion ai")
print("2. minmax")
print("3. qwen")
model = input("Enter your model: ")
if(model == "1"):
    jsonString = callInclusionAI(dataRawInput + configPromt)
    print(jsonString)
elif(model == "2"):
    jsonString = callMinMaxAI(dataRawInput + configPromt)
    print(jsonString)
elif(model == "3"):
    jsonString = callQwenAI(dataRawInput + configPromt)
    print(jsonString)
else:
    print("[ERROR] Model not found!")

print("suceesful!!")


if 'jsonString' in locals():

    cleaned_json = jsonString.strip()
    if cleaned_json.startswith("```json"):
        cleaned_json = cleaned_json[7:]
    elif cleaned_json.startswith("```"):
        cleaned_json = cleaned_json[3:]
    
    if cleaned_json.endswith("```"):
        cleaned_json = cleaned_json[:-3]
    
    cleaned_json = cleaned_json.strip()

    try:      
        json_data = json.loads(cleaned_json)
        with open("script.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        print("บันทึกไฟล์ script.json สำเร็จ!")
    except Exception as e:
        with open("script.json", "w", encoding="utf-8") as f:
            f.write(cleaned_json)
        print(f"คำเตือน: บันทึกเป็น Text ปกติ (เนื่องจากข้อมูลไม่ใช่ JSON ที่ถูกต้อง: {e})")

