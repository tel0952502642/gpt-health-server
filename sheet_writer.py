import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets 認證
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# 指定試算表與工作表名稱
SPREADSHEET_NAME = "健康紀錄總表"
WORKSHEET_NAME = "吃食紀錄表"
sheet = client.open(SPREADSHEET_NAME).worksheet(WORKSHEET_NAME)

# 新增吃食紀錄
def add_eatlog(data):
    row = [
        data.get("日期", ""),
        data.get("時間", ""),
        data.get("餐別", ""),
        data.get("品項", ""),
        data.get("份量", ""),
        data.get("蛋白質", ""),
        data.get("熱量", ""),
        data.get("備註", "")
    ]
    sheet.append_row(row)
    return {"status": "success", "message": "已新增一筆吃食紀錄"}

# 查詢某日期的吃食紀錄
def query_eatlog(date):
    records = sheet.get_all_records()
    result = [row for row in records if row.get("日期") == date]
    return result

# 更新指定日期與時間的某筆吃食紀錄
def update_eatlog(data):
    target_date = data.get("日期")
    target_time = data.get("時間")
    records = sheet.get_all_records()
    for i, row in enumerate(records, start=2):  # 從第2列開始（跳過標題列）
        if row["日期"] == target_date and row["時間"] == target_time and row["品項"] == data.get("品項"):
            updated_row = [
                data.get("日期", ""),
                data.get("時間", ""),
                data.get("餐別", ""),
                data.get("品項", ""),
                data.get("份量", ""),
                data.get("蛋白質", ""),
                data.get("熱量", ""),
                data.get("備註", "")
            ]
            sheet.update(f"A{i}:H{i}", [updated_row])
            return {"status": "success", "message": f"已更新第 {i} 列"}
    return {"status": "fail", "message": "找不到對應資料，無法更新"}

# 刪除指定紀錄
def delete_eatlog(data):
    target_date = data.get("日期")
    target_time = data.get("時間")
    target_item = data.get("品項")
    records = sheet.get_all_records()
    for i, row in enumerate(records, start=2):
        if row["日期"] == target_date and row["時間"] == target_time and row["品項"] == target_item:
            sheet.delete_rows(i)
            return {"status": "success", "message": f"已刪除第 {i} 列"}
    return {"status": "fail", "message": "找不到對應資料，無法刪除"}
