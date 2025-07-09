from flask import Flask, request, jsonify
from sheet_writer import add_row_to_sheet

app = Flask(__name__)

@app.route('/')
def home():
    return '👋 Health Logger is alive.'

@app.route('/eatlog', methods=['POST'])
def eatlog():
    try:
        # 強制解析 JSON（避免 Content-Type 設錯）
        data = request.get_json(force=True)
        print("📥 收到資料：", data)

        # 若資料為空，回傳錯誤
        if not data:
            return jsonify({"status": "error", "message": "No JSON received"}), 400

        # 寫入 Google Sheet
        add_row_to_sheet(data)
        print("✅ 成功寫入 Google Sheet！")

        # 回傳成功訊息
        return jsonify({
            "status": "success",
            "data": data
        }), 200

    except Exception as e:
        print("❌ 錯誤：", str(e))
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
