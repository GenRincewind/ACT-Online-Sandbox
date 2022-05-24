#!/usr/bin/env python3.6
import os
import uuid
from flask import Flask, flash, request, redirect, jsonify, render_template
from flask_cors import CORS
from act_executor import execute_act_prsim_code
UPLOAD_FOLDER = 'files'

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return render_template('index.html', message='Yes')


@app.route('/act_code',  methods=['POST'])
def calculate_capacitance_route():
    content = dict(request.json)
    actcode = content["actcode"]
    prsimcode = content["prsimcode"]
    with open('test_act.act', "w") as f:
        f.write(actcode)

    with open('test_act.act', "r") as f:
        print(f.read())

    with open('test_prsim.prsim', "w") as f:
        f.write(prsimcode)

    with open('test_prsim.prsim', "r") as f:
        print(f.read())
        
    outp, outerr = execute_act_prsim_code('test_act.act', 'test_prsim.prsim')

    return jsonify({"result": f'Code Output:\n\t {outp}', "errors":outerr})
