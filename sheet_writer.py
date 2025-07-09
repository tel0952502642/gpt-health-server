import os, json
import gspread
from google.oauth2.service_account import Credentials

try:
    creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    creds = Credentials.from_service_account_info(creds_info)
    gc = gspread.authorize(creds)
    print("✅ 成功建立憑證與登入 Google Sheets")
except Exception as e:
    print("❌ 認證初始化失敗:", e)

SHEET_ID = "1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo"
SHEET_NAME = "吃食紀錄表"

def append_row(data):
    try:
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
    except Exception as e:
        print(f"❌ 寫入失敗：{e}")
