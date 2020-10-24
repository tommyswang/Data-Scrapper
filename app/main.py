#!/usr/bin/env python3

from flask import Flask
from flask import render_template

# format here is:
# from <relative module file name> import <class name>
from lib.parsers.demo_parser import DemoParser

app = Flask(__name__)

@app.route('/')
def hello_world():
    team_name = DemoParser.our_team_name()
    return render_template('index.html', team_name = team_name)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)

