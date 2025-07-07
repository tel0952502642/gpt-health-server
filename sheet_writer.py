import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 設定授權範圍
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("chatgpt-465019-41c891217ea0.json", scope)
client = gspread.authorize(creds)

# 用試算表名稱打開（你要改成你實際的表單名稱）
sheet = client.open("你的Google Sheet表單名稱").sheet1

def write_eatlog(data):
    # 假設你表單欄位順序是：日期、餐別、品項、份量
    sheet.append_row([data["date"], data["meal"], data["item"], data["amount"]])
