#!/usr/bin/env python
# encoding: utf-8
import pandas as pd
import json as jsonify
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory

app = Flask(__name__)

#load CSV file once globally
csv_file = "financial_data.csv"
try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print(f"Error loading {csv_file}: {e}")
    df = pd.DataFrame()

@app.route("/")
def home():
    all_sectors = df['Sector'].dropna().unique().tolist()
    summary = {
        sector: df[df['Sector'] == sector]['EBITDA'].dropna().tolist()
        for sector in all_sectors
    }
    return jsonify(summary)

@app.route('/Sector', methods=['GET'])
def get_sector():
    if df.empty:
        return jsonify({"error": "CSV data not available"}), 500
    sectors = df['Sector'].dropna().unique().tolist()
    return jsonify(sectors)

@app.route('/EBITDA', methods=['GET'])
def get_ebitda_by_sector():
    sector = request.args.get('Sector')
    if not sector:
        return jsonify({"error": "Missing 'Sector' parameter"}), 400

    sector_data = df[df['Sector'] == sector]
    if sector_data.empty:
        return jsonify({"error": f"No data found for sector: {sector}"}), 404

    ebitda_values = sector_data['EBITDA'].dropna().tolist()
    return jsonify(ebitda_values)

if __name__ == '__main__':
    app.run(debug=True)

