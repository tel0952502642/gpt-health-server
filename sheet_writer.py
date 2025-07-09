import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    # 改成你的表單 ID
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1vKH4W5WjUqdveQ6uwgQxNbbKagdFh-ZxeEXp-i2mQzo/edit").sheet1
    return sheet

def write_eatlog_to_sheet(data):
    sheet = get_sheet()

    # 期望欄位順序：日期、餐別、品項、份量、蛋白質 (g)、熱量 (kcal)、備註
    row = [
        data.get("date", ""),
        data.get("meal", ""),
        data.get("item", ""),
        data.get("amount", ""),
        data.get("protein", ""),
        data.get("calories", ""),
        data.get("note", "")
    ]
    sheet.append_row(row)
