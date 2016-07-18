from flask import Flask, url_for, jsonify
import json
app = Flask(__name__)

@app.route('/')
def api_root():
	with open('GAME_MASTER_v0_1.json') as data_file:    
		data = json.load(data_file)
	return jsonify(data["Items"][90])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)