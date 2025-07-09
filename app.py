from flask import Flask, request, jsonify
import os, json, traceback
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# ✅ Google Sheets API 認證（用 Render 環境變數）
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = Credentials.from_service_account_info(creds_info, scopes=scopes)
gc = gspread.authorize(creds)

# ✅ 設定 Google Sheets 表格 ID 與工作表名稱
SPREADSHEET_ID = "1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo"
WORKSHEET_NAME = "吃食紀錄表"

@app.route("/")
def home():
    return "GPT 健康伺服器已啟動 🧠"

@app.route("/eatlog", methods=["POST"])
def add_eatlog():
    try:
        data = request.get_json()

        # 🧾 每筆欄位對應
        row = [
            data.get("date", ""),
            data.get("time", ""),
            data.get("meal", ""),
            data.get("item", ""),
            data.get("amount", ""),
            data.get("protein", ""),
            data.get("calories", ""),
            data.get("note", "")
        ]

        # ✅ 寫入 Google Sheets
        sh = gc.open_by_key(SPREADSHEET_ID)
        worksheet = sh.worksheet(WORKSHEET_NAME)
        worksheet.append_row(row, value_input_option="USER_ENTERED")

        return jsonify({"status": "success", "message": "資料已寫入"}), 200

    except Exception as e:
        # 錯誤處理與回傳完整錯誤訊息
        return jsonify({
            "status": "error",
            "message": str(e),
            "trace": traceback.format_exc()
        }), 500

if __name__ == "__main__":
    app.run()
