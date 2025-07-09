from flask import Flask, request, jsonify
from sheet_writer import write_eatlog_to_sheet

app = Flask(__name__)

@app.route('/')
def home():
    return "GPT Health Server Running!"

@app.route('/eatlog', methods=['POST'])
def eatlog():
    data = request.json
    try:
        write_eatlog_to_sheet(data)
        return jsonify({"status": "success", "message": "eatlog added"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run()
