def add_row_to_sheet(data):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    sheet = gspread.authorize(creds)

    sheet_url = 'https://docs.google.com/spreadsheets/d/1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo/edit'
    spreadsheet = sheet.open_by_url(sheet_url)
    worksheet = spreadsheet.worksheet("吃食紀錄表")  # 正確的工作表名稱

    worksheet.append_row([
        data["date"],
        "14:00",               # 暫時固定時間
        data["meal"],
        data["item"],
        data["amount"],
        data["protein"],
        data["calories"],
        data.get("note", "")   # 備註應該在最後
    ])
