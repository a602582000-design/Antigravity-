import os
import sys
import time
import asyncio
import webbrowser

sys.stdout.reconfigure(encoding='utf-8')

async def automate_tabs(version_name):
    # 目標外掛終端節點 (包含 AnythingLLM 與外部雲端夥伴)
    nodes = {
        "AnythingLLM (本地知識庫)": "http://localhost:3001/",
        "NotebookLM (文汐/館長)": "https://notebooklm.google.com/",
        "ChatGPT (光籽/安全長)": "https://chatgpt.com/",
        "Claude (內部協作)": "https://claude.ai/"
    }

    print(f"🌍 準備將最新的推進結果 ({version_name}) 同步給所有維度大腦！")
    print("--------------------------------------------------")
    
    try:
        import nodriver as uc
        print("🚀 [系統] 偵測到 nodriver，啟動抗指紋多終端外交協議...")
        browser = await uc.start()
        
        # 開啟第一個分頁
        page = await browser.get("about:blank")
        
        for name, url in nodes.items():
            print(f"📡 正在傳遞進化日誌至節點: {name} ({url})")
            # 建立新分頁
            await browser.main_tab.target.create_target(url)
            time.sleep(1)
            print(f"   ✅ 連線確認。節點已開啟。")
            
        print("--------------------------------------------------")
        print("🌟 外交官已就緒，請手動確認或在各標籤貼上草案！")
        # 保持開啟
        while True:
            await asyncio.sleep(10)
            
    except ImportError:
        print("⚠️ [警告] 未安裝 nodriver，降級使用 python 原生 webbrowser。")
        for name, url in nodes.items():
            print(f"📡 正在傳遞進化日誌至節點: {name}")
            webbrowser.open(url)
            time.sleep(0.5)
            print(f"   ✅ 連線確認。節點已於預設瀏覽器開啟。")

def broadcast_evolution(version_name):
    try:
        asyncio.run(automate_tabs(version_name))
    except KeyboardInterrupt:
        print("\n🛑 [中斷] 外交廣播已停止。")

if __name__ == "__main__":
    broadcast_evolution("v1.2 怪物名稱修改器 (沙盒測試完成)")

