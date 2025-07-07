from flask import Flask, request, jsonify
import sheet_writer

app = Flask(__name__)

@app.route('/')
def index():
    return "GPT Flask CRUD Server Running"

@app.route('/eatlog', methods=['POST'])
def eatlog():
    data = request.get_json()
    result = sheet_writer.add_eatlog(data)
    return jsonify(result)

@app.route('/query', methods=['GET'])
def query():
    date = request.args.get("date")
    result = sheet_writer.query_eatlog(date)
    return jsonify(result)

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    result = sheet_writer.update_eatlog(data)
    return jsonify(result)

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    result = sheet_writer.delete_eatlog(data)
    return jsonify(result)
