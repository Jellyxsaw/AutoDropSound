import time

import requests

# 本地 API 端點
API_URL = "http://127.0.0.1:5000/queue/join"

text_list = [
    # 貨幣類
    "神聖石。。。辛苦你了", "機會石", "點金石", "富豪石", "混沌石", "崇高石", "鏡子", "無效石", "瓦爾寶珠", "完美工匠石", "高級工匠石", "寶石匠的稜鏡",

    # 機制類
    "精煉的情感", "精髓", "高階精髓", "碑牌", "遺物", "任務物品",

    # 裝備與道具類
    "傳奇裝備", "技能寶石", "預兆", "探險文物", "探險日誌",

    # 地圖與碎片類
    "高級地圖", "特殊地圖", "異域鑄幣", "城塞碎片", "幻像碎片", "裂痕碎片", "迷宮鑰匙",

    # 其他
    "該更新過濾器啦", "恭喜。你很幸運呢"
]

# 允許選擇角色 取決於你資料夾名稱 可以自己調整
character_model = "【崩铁】流萤"

# 儲存 API 回應結果
responses = []

# 逐條請求 API
for text in text_list:
    payload = {
        "data": [
            text,  # 0: 輸入文本
            character_model,  # 1: 角色模型
            "default",  # 2: 情感
            None,  # 3: 未知參數 (原始請求中的 `null`)
            "",  # 4: 空字串
            "auto",  # 5: 語言模式
            0.85,  # 6: 速度
            "auto",  # 7: 語言
            "cut5",  # 8: 按標點符號
            50,  # 9: 最大長度
            10,  # 10: 批量處理大小
            -1,  # 11: 隨機種子
            True,  # 12: 平行推理
            5,  # 13: 取樣 Top-k
            0.8,  # 14: Top-p
            0.8,  # 15: 溫度
            1.35  # 16: 重複懲罰
        ],
        "event_data": None,
        "fn_index": 3,  # 這是 API 必要的索引
        "trigger_id": 51,  # API 內部參數，可能會變動
        "session_hash": "auto"  # 自動產生 session_hash
    }

    # 發送 POST 請求
    print(f"🚀 發送請求: 文本='{text}'，角色='{character_model}'")
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        print(f"✅ 成功: {text}")
        responses.append({"text": text, "status": "成功", "response": response.json()})
    else:
        print(f"❌ 失敗: {text}, 狀態碼={response.status_code}")
        responses.append({"text": text, "status": "失敗", "error": response.text})

    # **避免 API 過載，加入短暫延遲**
    time.sleep(10)

# **輸出所有請求結果**
print("\n📜 **API 呼叫結果**")
for result in responses:
    print(f"- 文本: {result['text']}, 狀態: {result['status']}")