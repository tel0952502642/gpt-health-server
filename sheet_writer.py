import os
import json
import gspread
from google.oauth2.service_account import Credentials

# 讀取環境變數中的 JSON 認證資訊
creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = Credentials.from_service_account_info(creds_info)
gc = gspread.authorize(creds)

# Google Sheet ID 與工作表名稱
SHEET_ID = "1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo"
SHEET_NAME = "吃食紀錄表"

def append_row(data):
    worksheet = gc.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
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
    worksheet.append_row(row)
    print(f"✅ 寫入資料：{row}")
