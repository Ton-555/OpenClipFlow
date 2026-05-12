import json
from ai_engines import callInclusionAI, callMinMaxAI, callQwenAI, callLocalAI

def gen_script_json(input_text, prompt_config, model_choice, local_model_name="gemma4:e4b"):
   
    full_prompt = input_text + prompt_config
    json_string = ""

    if model_choice == "1":
        json_string = callInclusionAI(full_prompt)
    elif model_choice == "2":
        json_string = callMinMaxAI(full_prompt)
    elif model_choice == "3":
        json_string = callQwenAI(full_prompt)
    elif model_choice == "4":
        json_string = callLocalAI(full_prompt, local_model_name)
    else:
        print("[ERROR] Model not found!")
        return None

    #clean json
    cleaned_json = json_string.strip()
    if cleaned_json.startswith("```json"):
        cleaned_json = cleaned_json[7:]
    elif cleaned_json.startswith("```"):
        cleaned_json = cleaned_json[3:]
    
    if cleaned_json.endswith("```"):
        cleaned_json = cleaned_json[:-3]
    
    cleaned_json = cleaned_json.strip()

    #write file script.json
    try:      
        json_data = json.loads(cleaned_json)
        with open("script.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        print("บันทึกไฟล์ script.json สำเร็จ!")
    except Exception as e:
        with open("script.json", "w", encoding="utf-8") as f:
            f.write(cleaned_json)
        print(f"คำเตือน: บันทึกเป็น Text ปกติ (เนื่องจากข้อมูลไม่ใช่ JSON ที่ถูกต้อง: {e})")
        
    return cleaned_json
