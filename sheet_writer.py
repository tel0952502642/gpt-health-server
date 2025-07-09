def add_row_to_sheet(data):
    import os, json
    import gspread
    from google.oauth2.service_account import Credentials

    creds_info = json.loads(os.environ["GOOGLE_CREDENTIALS"])
    creds = Credentials.from_service_account_info(creds_info)
    gc = gspread.authorize(creds)

    sheet_id = '1vKHAW5WjUdqveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo'
    spreadsheet = gc.open_by_key(1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo)
    worksheet = spreadsheet.worksheet("吃食紀錄表")

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

    print(f"✅ 寫入資料：{data}")  # ← 這行是為了 debug 回傳
