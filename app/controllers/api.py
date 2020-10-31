import csv

from pathlib import Path

import requests
from flask import Blueprint, render_template, request, send_file, safe_join
controller = Blueprint('api', __name__, )

def getFhirResource(url):
    response = requests.get(url = url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "error"

@controller.route('/api/download', methods=['POST'])
def downloadFile():
    print("Args")
    print(request.args.get('safe_path'))
    safe_path = request.args.get('safe_path')

    return send_file(safe_path, as_attachment=True)

@controller.route('/api', methods=['GET'])
def api():
    return render_template("api.html")


@controller.route('/api', methods=['POST'])
def create_api_job():
    print("Hello")
    print(request.form['url'])
    URL = request.form['url']
    try:
        data = getFhirResource(URL)
    except:
        return render_template("api.html", error = True)
    if data == "error":
        return render_template("api.html", error = True)

    print(data.keys())
    path = Path(controller.root_path).parent
    uploadPath = str(Path.joinpath(path, 'static/client'))
    print(uploadPath)
    data_file = open(uploadPath + '/data_file.csv', 'w')
    csv_writer = csv.writer(data_file)
    header = data.keys()
    csv_writer.writerow(header)

    # Writing data of CSV file
    csv_writer.writerow(data.values())

    data_file.close()
    print(data_file)
    safe_path = safe_join(uploadPath, 'data_file.csv')
    return render_template("api.html", error = False, safe_path = safe_path)
