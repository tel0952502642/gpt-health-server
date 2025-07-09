from flask import Flask, request, jsonify
from sheet_writer import append_row

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ GPT Health Server is live!"

@app.route("/eatlog", methods=["POST"])
def eatlog():
    try:
        data = request.get_json(force=True)
        print(f"📩 收到資料: {data}")

        append_row(data)

        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
