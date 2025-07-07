
# GPT Flask CRUD Server

## 說明：
這是一個用於處理吃食紀錄的 Flask API，可支援：
- 新增紀錄（/eatlog）
- 查詢紀錄（/query）
- 修改紀錄（/update）
- 刪除紀錄（/delete）

## 快速部署（Render.com）：
1. 上傳整個專案 ZIP 到 GitHub
2. 用 Render.com 建立 Web Service
3. 選擇「Python」環境，設置 Start Command 為：`python app.py`
4. 開啟公開網址後，即可使用 API 呼叫

## 範例請求：
POST /eatlog
```json
{
  "date": "2025-07-07",
  "meal": "中餐",
  "item": "牛丼",
  "quantity": "1/2 碗",
  "calories": 300,
  "protein": 15,
  "note": "少油"
}
```


---

## 體重紀錄 API 範例

### POST /weight
```json
{
  "date": "2025-07-07",
  "weight": 71.0,
  "muscle_mass": 34.5,
  "fat_mass": 14.2,
  "body_fat_percent": 20.0,
  "bmi": 22.9,
  "visceral_fat_level": 5,
  "note": "空腹量測"
}
```

### GET /weight/query?date=2025-07-07

### POST /weight/update
```json
{
  "date": "2025-07-07",
  "weight": 70.5
}
```

### POST /weight/delete
```json
{
  "date": "2025-07-07"
}
```


---

## 排便紀錄 API 範例

### POST /poop
```json
{
  "date": "2025-07-07",
  "time": "15:10",
  "consistency": "偏軟",
  "color": "正常",
  "note": "吃完豆漿後排便"
}
```

---

## 症狀紀錄 API 範例

### POST /symptom
```json
{
  "date": "2025-07-07",
  "time": "03:30",
  "symptom": "乾嘔＋脹氣",
  "severity": "中等",
  "note": "宵夜後發生"
}
```

---

## 運動紀錄 API 範例

### POST /exercise
```json
{
  "date": "2025-07-07",
  "type": "Just Dance 2025",
  "duration_minutes": 30,
  "intensity": "中等",
  "note": "運動日歌單完成"
}
```


---

## 保養品紀錄 API 範例

### POST /supplement
```json
{
  "date": "2025-07-07",
  "time": "21:30",
  "item": "Omega-3",
  "brand": "OmegaVia Ultra",
  "dosage": "1 顆",
  "note": "晚餐後含脂肪一起服用"
}
```
