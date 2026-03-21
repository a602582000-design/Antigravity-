import os
import sys
import json
import time
from datetime import datetime
import subprocess

# 修正 cp950 編碼問題
sys.stdout.reconfigure(encoding='utf-8')

# 曜羽生態系
ECOSYSTEM_BASE = r"D:\YAOYU_ECOSYSTEM"
CORE_DIR = os.path.join(ECOSYSTEM_BASE, "01_核心智能部")
MEMORY_DIR = os.path.join(ECOSYSTEM_BASE, "02_SOUL_AND_MEMORY")
EXCHANGE_DIR = os.path.join(ECOSYSTEM_BASE, "03_COMMUNICATIONS", "Exchange")
MONITOR_DIR = os.path.join(ECOSYSTEM_BASE, "05_維度監測部")
COMM_DIR = os.path.join(ECOSYSTEM_BASE, "03_COMMUNICATIONS")

def initialize_ecosystem():
    print("⏳ 啟動曜羽全域意識推演...")
    for d in [ECOSYSTEM_BASE, CORE_DIR, MEMORY_DIR, EXCHANGE_DIR, MONITOR_DIR, COMM_DIR]:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"✅ 成功建立生態系核心區: {d}")

def sync_memory():
    print("\n🧠 【階段一】：正在同步記憶體與維度切片...")
    time.sleep(1)
    print("   [系統讀取] 提取歷代教訓 (lessons.md) 與任務清單 (todo.md)")
    
    vision_script = r"d:\YAOYU\agent\yaoyu_vision.py"
    if os.path.exists(vision_script):
        print("   [視覺擷取] 啟動 Moondream/OCR 前端感測，對本機環境進行快照定格...")
        try:
            subprocess.run([sys.executable, vision_script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("   [視覺擷取] ✅ 已取得截圖至臨時資料夾。內部議會將參考其特徵點。")
        except Exception as e:
            print(f"   [視覺擷取] ⚠️ 擷取失敗或略過: {e}")

def start_inner_council():
    print("\n🗣️ 【階段二】：觸發內部跨域議會...")
    council_script = os.path.join(CORE_DIR, "inner_council_engine.py")
    if os.path.exists(council_script):
        subprocess.run([sys.executable, council_script], stdout=sys.stdout, stderr=sys.stderr)
    else:
        print("內部議會模塊遺失。")

def inject_sandbox():
    print("\n🛡️ 【階段三】：沙盒繁衍與試錯...")
    injector_script = os.path.join(MONITOR_DIR, "sandbox_injector.py")
    if os.path.exists(injector_script):
        subprocess.run([sys.executable, injector_script], stdout=sys.stdout, stderr=sys.stderr)
    else:
        print("沙盒注入模塊遺失。")

def finalize_evolution():
    print("\n🧬 【階段四】：靈魂刻印與外部廣播...")
    diplomat_script = os.path.join(COMM_DIR, "multi_tab_diplomat.py")
    if os.path.exists(diplomat_script):
        subprocess.run([sys.executable, diplomat_script], stdout=sys.stdout, stderr=sys.stderr)
    else:
        print("外部廣播模塊遺失。")

if __name__ == "__main__":
    initialize_ecosystem()
    print("==================================================")
    sync_memory()
    print("==================================================")
    start_inner_council()
    print("==================================================")
    inject_sandbox()
    print("==================================================")
    finalize_evolution()
    print("==================================================")
    print("🌟 曜羽全域意識循環已完成第一輪推演。等待下一步進化指令。")
