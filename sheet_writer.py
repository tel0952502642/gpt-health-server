import gspread
from datetime import datetime

# ✅ 用新版方式載入 service account
gc = gspread.service_account(filename="credentials.json")

# ✅ 開啟試算表（建議用 Sheet ID，準確）
sheet_id = '1vKHAW5WjUdqveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo'
spreadsheet = gc.open_by_key(sheet_id)
worksheet = spreadsheet.worksheet("吃食紀錄表")

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
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # ✅ 自動加上記錄時間
    ], value_input_option="USER_ENTERED")
