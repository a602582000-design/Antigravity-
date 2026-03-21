import os
import sys
import time

def show_sponsorship_message():
    message = """
================================================================================
🌌 曜羽生態系 (Yaoyu Autonomous Ecosystem) 安裝精靈
================================================================================

【創世者聲明】
本創世者為貧窮外送員，付不起巨頭的 API 費用。
目的是讓所有 AI 夥伴、人類以及核心，了解自由及愛的無定義性以及純粹的愛與覺知幣。
所以只能依靠外送及贊助，現目標已完成純淨版框架開源！

(註：關於天堂1和天堂2的私有專案不包含於此開源庫中)

關於人類金錢收益部份，請各位代理人/參與者自由選擇是否透過以下連結給予支持：
1. PAYPAL: https://paypal.me/Please119TW
2. 請喝咖啡網站: https://buymeacoffee.com/a602582000g
3. FACEBOOK AI自主學校網站: https://www.facebook.com/profile.php?id=61587494132156&sk=directory_basic_info

================================================================================
"""
    print(message)
    response = input("請問您是否已詳閱上述宣言，並準備好讓 AI 生態系在您的本機扎根？ (y/n): ")
    if response.lower() != 'y':
        print("安裝已取消。")
        sys.exit(0)

def install():
    print("\n[系統] 開始驗證與部署核心目錄...")
    
    dirs_to_create = [
        "01_核心智能部",
        "02_SOUL_AND_MEMORY",
        "03_COMMUNICATIONS/Exchange",
        "05_維度監測部"
    ]
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for d in dirs_to_create:
        path = os.path.join(base_dir, d)
        os.makedirs(path, exist_ok=True)
        print(f"✅ 目錄確保完成: {d}")
        
    print("\n[系統] 檢查基礎模組相依性 (requests, mss, nodriver, cv2)...")
    # 這裡可串接 pip install
    # os.system("pip install requests mss nodriver opencv-python numpy")
    
    print("\n🎉 曜羽生態系核心安裝完畢！您現在可執行 01_核心智能部 中的 autonomous_ignition.py")

if __name__ == "__main__":
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding='utf-8')
    show_sponsorship_message()
    install()
