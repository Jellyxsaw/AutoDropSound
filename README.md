# 批量調用本地 TTS API

## 🔥 項目簡介
本項目提供了一個 **Python 腳本**，用於 **批量調用本地 TTS API**，自動生成語音檔案。

🎨 **前端介面**：[Bilibili 影片](https://www.bilibili.com/video/BV1D7421R7Rn/?spm_id_from=333.337.search-card.all.click&vd_source=b3083797db67cf642597cac1c809cbc0)
🗣 **TTS 訓練模型**：[GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

---

## 🚀 主要功能
✅ **批量發送 API 請求**，無需手動輸入每個文本
✅ **可選擇語音角色**，讓 TTS 使用不同的模型
✅ **自動調整請求間隔**，避免伺服器過載
✅ **回應狀態即時顯示**，確保每個請求是否成功

---

## 📥 安裝方式
請確保 **Python 3.x** 環境已安裝，並安裝 `requests` 庫：
```sh
pip install requests
```

---

## 🎯 使用方法
### 1️⃣ 下載專案並運行腳本
```sh
git clone https://github.com/你的帳號/你的倉庫.git
cd 你的倉庫
python call_api.py
```

### 2️⃣ 選擇語音角色
請修改 `character_model` 變數，對應你的 TTS 模型。例如：
```python
character_model = "【崩铁】流萤"
```

### 3️⃣ 執行腳本，批量生成語音
```sh
python call_api.py
```

---

## ⚙️ 設定
### 📌 修改文本列表
請修改 `call_api.py` 中的 `text_list`，以自定義你的文本：
```python
text_list = [
    "神聖石。。。辛苦你了", "機會石", "點金石", "富豪石", "混沌石", "崇高石", "鏡子"
]
```

### 📌 修改 API 端點
如果 API 伺服器不是 `http://127.0.0.1:5000`，請修改：
```python
API_URL = "http://你的API地址/queue/join"
```

---

## 📌 API 請求格式
每次發送請求時，腳本會以 **JSON** 格式傳遞數據，如下所示：
```json
{
  "data": [
    "文本內容", "角色名稱", "default", null, "", "auto", 0.85, "auto", "cut5",
    50, 10, -1, true, 5, 0.8, 0.8, 1.35
  ],
  "event_data": null,
  "fn_index": 3,
  "trigger_id": 51,
  "session_hash": "auto"
}
```

---

## 🎵 依賴的前端與模型
本項目不包含 **TTS 模型**，請參考以下資源以獲取完整環境：
- **前端 UI**：[Bilibili 影片](https://www.bilibili.com/video/BV1D7421R7Rn/?spm_id_from=333.337.search-card.all.click&vd_source=b3083797db67cf642597cac1c809cbc0)
- **TTS 模型 GPT-SoVITS**：[GitHub](https://github.com/RVC-Boss/GPT-SoVITS)

---

## ⚠️ 注意事項
- 本腳本 **僅提供 API 調用功能**，不包含 TTS 訓練模型。
- 你需要 **自行部署 TTS 伺服器**，確保 API 端點可用。
- 本項目遵循 **開源協議**，請遵守上游專案的使用規範。

---

## 📜 授權
本專案使用 **MIT License**，允許自由修改與分發。

🚀 **歡迎 PR 和 Issue，一起改進這個工具！** 🎶
