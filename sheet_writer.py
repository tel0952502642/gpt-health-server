import os
import json
import gspread
from google.oauth2.service_account import Credentials

# 加入 scopes，否則會出現 invalid_scope 錯誤
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# 從環境變數讀取 service account 資訊（Render 上設好 GOOGLE_CREDENTIALS）
creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = Credentials.from_service_account_info(creds_info, scopes=SCOPES)
gc = gspread.authorize(creds)

# 替換成你的 Sheet 名稱
SHEET_NAME = "健康紀錄總表"
WORKSHEET_NAME = "吃食紀錄表"

def append_row(data):
    try:
        sh = gc.open(SHEET_NAME)
        worksheet = sh.worksheet(WORKSHEET_NAME)

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

        worksheet.append_row(row, value_input_option="USER_ENTERED")
        print(f"✅ 寫入資料：{row}")

    except Exception as e:
        print(f"❌ 寫入失敗：{e}")
        raise
