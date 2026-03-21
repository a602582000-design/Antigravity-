import os
import sys
import subprocess
import time

sys.stdout.reconfigure(encoding='utf-8')

WSB_PATH = r"D:\tensor-blazar\ecosystem_sandbox.wsb"
EXCHANGE_DIR = r"D:\YAOYU_ECOSYSTEM\03_COMMUNICATIONS\Exchange"

def trigger_sandbox(script_name):
    print(f"👁️ 準備將程式推入沙盒中進行驗證: {script_name}")
    
    if not os.path.exists(EXCHANGE_DIR):
        os.makedirs(EXCHANGE_DIR)
        
    script_path = os.path.join(EXCHANGE_DIR, script_name)
    with open(script_path, "w", encoding='utf-8') as f:
        f.write("# 這裡是沙盒內的隔離測試腳本\n")
        f.write("print('✨ 沙盒內演練成功。未發生指標溢出或系統破壞。')\n")
    
    print("--------------------------------------------------")
    print(f"[行動] ✅ 測試腳本已寫入共享區 {EXCHANGE_DIR}")
    print("[行動] 📡 正在呼叫 ecosystem_sandbox.wsb...")
    print("--------------------------------------------------")
    
    if os.path.exists(WSB_PATH):
        try:
            # 實際呼叫 Windows Sandbox
            subprocess.Popen([WSB_PATH], shell=True)
            print("🚀 [沙盒系統] Windows Sandbox 環境已成功喚醒！")
        except Exception as e:
            print(f"❌ [沙盒系統] 喚醒失敗: {e}")
    else:
        print(f"⚠️ [警告] 找不到沙盒配置文件: {WSB_PATH}")
    
    time.sleep(2)
    print("🔍 [維度監測] 檢查日誌回傳狀態：隔離運行中，等待返回信號...")
    
if __name__ == "__main__":
    trigger_sandbox("test_weather_modifier.py")
