
# 這只是範例結構，實際需串接 Google Sheets API 或 GAS endpoint
def add_eatlog(data):
    # TODO: 寫入資料到 Google Sheets
    return {"status": "success", "action": "add", "data": data}

def query_eatlog(date):
    # TODO: 從 Google Sheets 查詢資料
    return {"status": "success", "action": "query", "date": date, "data": []}

def update_eatlog(data):
    # TODO: 根據條件更新 Google Sheets 中指定資料
    return {"status": "success", "action": "update", "data": data}

def delete_eatlog(data):
    # TODO: 根據條件刪除 Google Sheets 中指定資料
    return {"status": "success", "action": "delete", "data": data}

def add_weight(data):
    return {"status": "success", "action": "add_weight", "data": data}

def query_weight(date):
    return {"status": "success", "action": "query_weight", "date": date, "data": []}

def update_weight(data):
    return {"status": "success", "action": "update_weight", "data": data}

def delete_weight(data):
    return {"status": "success", "action": "delete_weight", "data": data}


def add_poop(data):
    return {"status": "success", "action": "add_poop", "data": data}

def add_symptom(data):
    return {"status": "success", "action": "add_symptom", "data": data}

def add_exercise(data):
    return {"status": "success", "action": "add_exercise", "data": data}


def add_supplement(data):
    return {"status": "success", "action": "add_supplement", "data": data}
