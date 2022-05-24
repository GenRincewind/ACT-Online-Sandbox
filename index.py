#!/usr/bin/env python3.6
import os
import uuid
from flask import Flask, flash, request, redirect, jsonify
from flask_cors import CORS
UPLOAD_FOLDER = 'files'

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return render_template('index.html', message=message)


@app.route('/calculate_capacitance',  methods=['POST'])
def calculate_capacitance_route():
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify({})


