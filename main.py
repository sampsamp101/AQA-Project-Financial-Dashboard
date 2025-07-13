#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# Load CSV file globally
csv_file = "financial_data.csv"
try:
    df = pd.read_csv(csv_file)
    if 'Sector' not in df.columns or 'EBITDA' not in df.columns:
        raise ValueError("Required columns missing in CSV.")
except Exception as e:
    print(f"❌ Error loading {csv_file}: {e}")
    df = pd.DataFrame()

@app.route("/DownloadCSV", methods = ["GET"])
def download_csv():
    if df.empty:
        return jsonify({"error": "CSV data not available"}), 500

    return send_file(
        csv_file,
        mimetype= "text/csv",
        as_attachment = True,
        download_name="financial_data.csv"
    )

@app.route("/")
def home():
    if df.empty:
        return jsonify({"error": "CSV data not available"}), 500

    summary = {
        sector: df[df['Sector'] == sector]['EBITDA'].dropna().tolist()
        for sector in df['Sector'].dropna().unique()
    }
    return jsonify(summary)

@app.route('/Sector', methods=['GET'])
def get_sectors():
    if df.empty:
        return jsonify({"error": "CSV data not available"}), 500

    sectors = df['Sector'].dropna().unique().tolist()
    return jsonify(sectors)

@app.route('/EBITDA', methods=['GET'])
def get_ebitda():
    if df.empty:
        return jsonify({"error": "CSV data not available"}), 500

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
