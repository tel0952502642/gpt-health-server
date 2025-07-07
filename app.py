
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

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/weight', methods=['POST'])
def add_weight():
    data = request.get_json()
    result = sheet_writer.add_weight(data)
    return jsonify(result)

@app.route('/weight/query', methods=['GET'])
def query_weight():
    date = request.args.get("date")
    result = sheet_writer.query_weight(date)
    return jsonify(result)

@app.route('/weight/update', methods=['POST'])
def update_weight():
    data = request.get_json()
    result = sheet_writer.update_weight(data)
    return jsonify(result)

@app.route('/weight/delete', methods=['POST'])
def delete_weight():
    data = request.get_json()
    result = sheet_writer.delete_weight(data)
    return jsonify(result)


@app.route('/poop', methods=['POST'])
def add_poop():
    data = request.get_json()
    result = sheet_writer.add_poop(data)
    return jsonify(result)

@app.route('/symptom', methods=['POST'])
def add_symptom():
    data = request.get_json()
    result = sheet_writer.add_symptom(data)
    return jsonify(result)

@app.route('/exercise', methods=['POST'])
def add_exercise():
    data = request.get_json()
    result = sheet_writer.add_exercise(data)
    return jsonify(result)


@app.route('/supplement', methods=['POST'])
def add_supplement():
    data = request.get_json()
    result = sheet_writer.add_supplement(data)
    return jsonify(result)
