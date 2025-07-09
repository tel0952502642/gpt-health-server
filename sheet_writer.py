import gspread
import os, json
from datetime import datetime
from google.oauth2.service_account import Credentials

# ✅ 從環境變數讀取 service account 憑證
creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = Credentials.from_service_account_info(creds_info)
gc = gspread.authorize(creds)

# ✅ 開啟試算表
sheet_id = '1vKHAW5WjUdqveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo'
spreadsheet = gc.open_by_key(sheet_id)
worksheet = spreadsheet.worksheet("吃食紀錄表")

# ✅ 寫入資料
def add_row_to_sheet(data):
    worksheet.append_row([
        data.get("date", ""),
        data.get("time", ""),
        data.get("meal", ""),
        data.get("item", ""),
        data.get("amount", ""),
        data.get("protein", ""),
        data.get("calories", ""),
        data.get("note", ""),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ], value_input_option="USER_ENTERED")
