def add_row_to_sheet(data):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    # 用 URL 開啟你的 spreadsheet
    sheet_url = 'https://docs.google.com/spreadsheets/d/1vKHAW5WjUdqveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo/edit'
    spreadsheet = client.open_by_url(sheet_url)

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
