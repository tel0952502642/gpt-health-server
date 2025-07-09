def add_row_to_sheet(data):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    sheet = gspread.authorize(creds)

    # 開啟表單（用 URL ID）
    sheet_url = 'https://docs.google.com/spreadsheets/d/1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo/edit'
    spreadsheet = sheet.open_by_url(sheet_url)

    worksheet = spreadsheet.worksheet("吃食紀錄表")  # ✅ 指定正確的工作表分頁

    worksheet.append_row([
        data["date"],
        "14:00",  # 時間目前先固定
        data["meal"],
        data["item"],
        data["amount"],
        data["protein"],
        data["calories"],
        data.get("note", "")
    ])
