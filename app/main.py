from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__,template_folder='template', static_folder='static', static_url_path='')
app.config.from_object(__name__)


@app.route('/')
def server_index():
    return render_template("index.html")

CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
