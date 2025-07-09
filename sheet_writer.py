def add_row_to_sheet(data):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    sheet = gspread.authorize(creds)

    sheet_url = '1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo'
    spreadsheet = sheet.open_by_key(spreadsheet_id)

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
