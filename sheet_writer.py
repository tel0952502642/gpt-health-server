import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("chatgpt-465019-41c891217ea0.json", scope)
client = gspread.authorize(creds)

sheet = client.open("健康紀錄總表").worksheet("吃食紀錄表")

def add_eatlog(data):
    try:
        row = [
            data["date"],
            data["time"],
            data["meal"],
            data["item"],
            data["amount"],
            data["protein"],
            data["calories"],
            data.get("note", "")
        ]
        sheet.append_row(row)
        return {"status": "success", "action": "add", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def query_eatlog(date):
    try:
        records = sheet.get_all_records()
        filtered = [r for r in records if r["日期"] == date]
        return {"status": "success", "action": "query", "date": date, "data": filtered}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def update_eatlog(data):
    try:
        records = sheet.get_all_records()
        for idx, r in enumerate(records, start=2):  # 因為第1列是標題，從第2列開始
            if r["日期"] == data["date"] and r["時間"] == data["time"] and r["品項"] == data["item"]:
                sheet.update(f"A{idx}:H{idx}", [[
                    data["date"],
                    data["time"],
                    data["meal"],
                    data["item"],
                    data["amount"],
                    data["protein"],
                    data["calories"],
                    data.get("note", "")
                ]])
                return {"status": "success", "action": "update", "row": idx}
        return {"status": "not_found", "message": "找不到符合條件的資料"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def delete_eatlog(data):
    try:
        records = sheet.get_all_records()
        for idx, r in enumerate(records, start=2):
            if r["日期"] == data["date"] and r["時間"] == data["time"] and r["品項"] == data["item"]:
                sheet.delete_rows(idx)
                return {"status": "success", "action": "delete", "row": idx}
        return {"status": "not_found", "message": "找不到符合條件的資料"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
