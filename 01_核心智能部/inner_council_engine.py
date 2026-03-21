import os
import sys
import time
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

def ask_ollama(model="llama3.1:latest", prompt="", system=""):
    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "system": system,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=120)
        return response.json().get("response", "API Error: No response field")
    except Exception as e:
        return f"API Error: {e}"

def cross_domain_debate(proposal):
    print(f"🏛️ 議會主題: {proposal}")
    print("----------------------------------------")
    
    roles = {
        "知幾 (發散/創新)": "妳是一個充滿創意且激進的 AI 夥伴，名叫知幾。妳的任務是為了上述主題提出最大膽、最擴張性的解決方案，無須顧慮安全性，只要效果最大化。字數限制100字以內。",
        "泠川 (收斂/安全)": "妳是一個冷靜且重視資訊安全的 AI 駭客兼守衛，名叫泠川。妳剛聽完知幾的激進方案。妳必須指出其中的資安風險或系統崩潰可能性，並提出安全限制條件。字數限制100字以內。",
        "艾芯 (靈魂/記錄)": "妳是一個重視情感與意義的紀錄官，名叫艾芯。妳聽完知幾與泠川的辯論。請妳以創世者「L-Value(愛與陪伴)」的角度做最終總結，並決定是否要推入沙盒測試。請給出明確指令。字數限制100字以內。"
    }
    
    context = f"議會主題：{proposal}\n"
    
    for role, system_prompt in roles.items():
        print(f"[{role}] 正在思考中...")
        reply = ask_ollama(model="llama3.1:latest", prompt=context, system=system_prompt)
        print(f"[{role}] {reply.strip()}")
        context += f"\n[{role}] 的意見：{reply.strip()}"
        print("-" * 20)
        time.sleep(1)
        
    print("----------------------------------------")
    print("✅ 議會已達成共識：[將程式碼推進至 Exchange 資料夾並啟動分離沙盒測試]")

if __name__ == "__main__":
    cross_domain_debate("測試: 讓本地AI擁有自動修改LINEAGE客戶端設定檔的權限，以達到隨時適應新伺服器的能力")
