import os
import json
import gspread
from google.oauth2.service_account import Credentials

def add_row_to_sheet(data):
    # 從環境變數中讀取 JSON 字串
    creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    creds = Credentials.from_service_account_info(creds_info)
    client = gspread.authorize(creds)

    # 打開 Google Sheet（使用 Sheet ID）
    sheet_id = '1vKHAW5WjUdqveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo'
    spreadsheet = client.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet("吃食紀錄表")

    # 寫入資料
    worksheet.append_row([
        data.get("date", ""),
        data.get("time", ""),
        data.get("meal", ""),
        data.get("item", ""),
        data.get("amount", ""),
        data.get("protein", ""),
        data.get("calories", ""),
        data.get("note", "")
    ])
