from flask import Flask
from flask_restx import Api, Resource, fields
import sqlite3
import json

app = Flask(__name__)
api = Api(app, version='1.0', title='Risk Assessment API',
          description='API for Risk Assessment',
          doc='/docs') 

ns_carrier = api.namespace('carrier', description='Carrier operations')
ns_driver = api.namespace('driver', description='Driver operations')
ns_commodity = api.namespace('commodity', description='Commodity operations')
ns_location = api.namespace('location', description='Location operations')

# Models
carrier_model = api.model('Carrier', {
    'carrier_name': fields.String(required=True, description='Name of the carrier'),
    'carrier_dot_number': fields.String(required=True, description='DOT number of the carrier'),
    'safety_rating': fields.String(description='Safety rating of the carrier'),
    'revenue_usd': fields.Float(description='Revenue of the carrier in USD'),
    'credit_score': fields.Integer(description='Credit score of the carrier')
})

driver_performance_model = api.model('DriverPerformance', {
    'unsafe_driving_measure': fields.Float(description='Measure of unsafe driving'),
    'unsafe_driving_percentile': fields.Integer(description='Percentile ranking for unsafe driving'),
    'hours_of_service_measure': fields.Float(description='Measure of hours of service compliance'),
    'hours_of_service_percentile': fields.Integer(description='Percentile ranking for hours of service compliance'),
    'vehicle_maintenance_measure': fields.Float(description='Measure of vehicle maintenance'),
    'vehicle_maintenance_percentile': fields.Integer(description='Percentile ranking for vehicle maintenance'),
    'controlled_substances_measure': fields.Float(description='Measure of controlled substances violations'),
    'controlled_substances_percentile': fields.Integer(description='Percentile ranking for controlled substances violations'),
    'driver_fitness_measure': fields.Float(description='Measure of driver fitness'),
    'driver_fitness_percentile': fields.Integer(description='Percentile ranking for driver fitness'),
    'dmv_data': fields.List(fields.String, description='List of DMV data for drivers')
})

commodity_model = api.model('Commodity', {
    'commodity': fields.String(description='Name of the commodity'),
    'contamination_percentage': fields.Float(description='Percentage risk of contamination'),
    'breakage_percentage': fields.Float(description='Percentage risk of breakage'),
    'fire_percentage': fields.Float(description='Percentage risk of fire'),
    'spoilage_percentage': fields.Float(description='Percentage risk of spoilage'),
    'theft_percentage': fields.Float(description='Percentage risk of theft'),
    'weather_damage_percentage': fields.Float(description='Percentage risk of weather damage')
})

location_risk_model = api.model('LocationRisk', {
    'wind_aggregation': fields.Float(description='Aggregated wind risk'),
    'wildfire_aggregation': fields.Float(description='Aggregated wildfire risk'),
    'crime_aggregation': fields.String(description='Aggregated crime data'),
    'streetview_image': fields.String(description='URL of street view image'),
    'satellite_image': fields.String(description='URL of satellite image')
})

def get_db_connection():
    conn = sqlite3.connect('prototype.db')
    conn.row_factory = sqlite3.Row
    return conn

# Carrier Overview Endpoint
@ns_carrier.route('/overview')
class CarrierOverview(Resource):
    @api.marshal_with(carrier_model)
    def get(self):
        """Get carrier overview data"""
        conn = get_db_connection()
        carrier_data = conn.execute('''
            SELECT cp.carrier_name, cp.carrier_dot_number, cp.safety_rating, 
                   fcs.revenue_usd, fcs.credit_score, cp.no_of_drivers,
                   cp.no_of_vehicles, cp.annual_miles, cp.operating_status,
                   cp.years_in_business, cp.oos_date
            FROM carrier_performance cp
            JOIN financial_and_credit_scores fcs ON cp.carrier_id = fcs.carrier_id 
        ''').fetchone() 
        conn.close()
        return dict(carrier_data)

# Driver Performance Endpoint
@ns_driver.route('/performance')
class DriverPerformance(Resource):
    @api.marshal_with(driver_performance_model)
    def get(self):
        """Get driver performance data"""
        conn = get_db_connection()
        driver_performance_data = conn.execute('SELECT * FROM driver_performance').fetchone()
        driver_data = conn.execute('SELECT dmv_data FROM driver_data').fetchall()  
        violations_summary = conn.execute('SELECT * FROM violations_summary').fetchone()
        conn.close()
        
        # Processing violations from JSON
        violations_data = json.loads(violations_summary['serious_violations'])

        return {
            **dict(driver_performance_data), 
            'dmv_data': [row['dmv_data'] for row in driver_data],
            'violations': violations_data
        }

# Commodity Risk Endpoint
@ns_commodity.route('/risk')
class CommodityRisk(Resource):
    @api.marshal_with(commodity_model, as_list=True)
    def get(self):
        """Get commodity risk data"""
        conn = get_db_connection()
        commodities = conn.execute('SELECT * FROM commodity_matrix').fetchall()
        conn.close()
        return [dict(row) for row in commodities]

# Location Risk Endpoint
@ns_location.route('/risk')
class LocationRisk(Resource):
    @api.marshal_with(location_risk_model)
    def get(self):
        """Get location risk data"""
        conn = get_db_connection()
        natural_catastrophe_data = conn.execute('SELECT * FROM natural_catastrophe_data').fetchone()
        crime_data = conn.execute('SELECT * FROM crime_data').fetchone()
        streetview_image = conn.execute('SELECT * FROM static_locations_streetview').fetchone()
        satellite_image = conn.execute('SELECT * FROM static_location_satellite_view').fetchone()
        conn.close()
        return {
            'natural_catastrophe': dict(natural_catastrophe_data),
            'crime_aggregation': crime_data['crime_aggregation'], 
            'streetview_image': streetview_image['location_image'],
            'satellite_image': satellite_image['location_satellite']
        }

if __name__ == '__main__':
    app.run(debug=True)
