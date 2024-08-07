from flask import Flask, jsonify
import sqlite3
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('prototype.db')
    conn.row_factory = sqlite3.Row
    return conn

# Carrier Overview Endpoint
@app.route('/api/carrier_overview')
def carrier_overview():
    conn = get_db_connection()
    carrier_data = conn.execute('SELECT * FROM carrier_performance').fetchone()
    financial_data = conn.execute('SELECT * FROM financial_and_credit_scores').fetchone()
    conn.close()
    return jsonify({
        'carrier': dict(carrier_data),
        'financial': dict(financial_data)
    })

# Driver Performance Endpoint
@app.route('/api/driver_performance')
def driver_performance():
    conn = get_db_connection()
    driver_performance_data = conn.execute('SELECT * FROM driver_performance').fetchone()
    driver_data = conn.execute('SELECT * FROM driver_data').fetchall()
    violations_summary = conn.execute('SELECT * FROM violations_summary').fetchone()
    conn.close()

    # Process violations summary JSON
    violations_data = json.loads(violations_summary['serious_violations'])

    return jsonify({
        'performance': dict(driver_performance_data),
        'driver_data': [dict(row) for row in driver_data],
        'violations': violations_data
    })

# Commodity Risk Endpoint
@app.route('/api/commodity_risk')
def commodity_risk():
    conn = get_db_connection()
    commodities = conn.execute('SELECT * FROM commodity_matrix').fetchall()
    conn.close()
    return jsonify([dict(row) for row in commodities])

# Location Risk Endpoint
@app.route('/api/location_risk')
def location_risk():
    conn = get_db_connection()
    natural_catastrophe_data = conn.execute('SELECT * FROM natural_catastrophe_data').fetchone()
    crime_data = conn.execute('SELECT * FROM crime_data').fetchone()
    streetview_image = conn.execute('SELECT * FROM static_locations_streetview').fetchone()
    satellite_image = conn.execute('SELECT * FROM static_location_satellite_view').fetchone()
    conn.close()
    return jsonify({
        'natural_catastrophe': dict(natural_catastrophe_data),
        'crime': crime_data['crime_aggregation'],  # Assuming crime data is text
        'streetview_image': streetview_image['location_image'],
        'satellite_image': satellite_image['location_satellite']
    })

if __name__ == '__main__':
    app.run(debug=True)
