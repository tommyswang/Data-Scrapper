from flask import Blueprint, send_file, send_from_directory
import os
import pathlib


controller = Blueprint('download', __name__)


@controller.route('/files/<file_name>', methods=['GET'])
def download(file_name):
    root_path = pathlib.Path(__file__).resolve().parents[1]
    full_path = os.path.join(root_path, 'files')
    return send_from_directory(full_path, filename=file_name)
