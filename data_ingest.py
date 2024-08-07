import sqlite3
import json

# Connect to SQLite database
conn = sqlite3.connect('prototype.db')
cursor = conn.cursor()

# Insert dummy data into existing tables

# Carrier Performance
cursor.execute('''
INSERT INTO carrier_performance (
    carrier_name, carrier_dot_number, operating_status, years_in_business, 
    no_of_drivers, no_of_vehicles, annual_miles, oos_date, safety_rating
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
('Example Carrier', '123456', 'Active', 10, 50, 30, 500000, '2023-01-01', 'Satisfactory'))

# Get the carrier_id of the inserted carrier
carrier_id = cursor.lastrowid

# Financial and Credit Scores
cursor.execute('''
INSERT INTO financial_and_credit_scores (
    carrier_id, revenue_usd, ebitda_usd, net_profit_usd, credit_score
) VALUES (?, ?, ?, ?, ?)''', 
(carrier_id, 1000000.0, 150000.0, 120000.0, 750))

# Commodity Matrix
commodities = [
    ('Electronics', 0.02, 0.01, 0.0, 0.0, 0.01, 0.0),
    ('Furniture', 0.01, 0.02, 0.0, 0.0, 0.01, 0.0),
    ('Food', 0.03, 0.01, 0.0, 0.05, 0.02, 0.01),
    ('Clothing', 0.01, 0.01, 0.0, 0.0, 0.01, 0.0),
    ('Automotive Parts', 0.02, 0.03, 0.0, 0.0, 0.01, 0.0)
]
cursor.executemany('''
INSERT INTO commodity_matrix (
    commodity, contamination_percentage, breakage_percentage, fire_percentage, 
    spoilage_percentage, theft_percentage, weather_damage_percentage
) VALUES (?, ?, ?, ?, ?, ?, ?)''', commodities)

# Driver Performance
cursor.execute('''
INSERT INTO driver_performance (
    unsafe_driving_measure, unsafe_driving_percentile, hours_of_service_measure, 
    hours_of_service_percentile, vehicle_maintenance_measure, vehicle_maintenance_percentile, 
    controlled_substances_measure, controlled_substances_percentile, driver_fitness_measure, 
    driver_fitness_percentile
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
(2.5, 30, 1.8, 25, 3.0, 20, 0.5, 15, 1.0, 10))

# Violations Summary
violations_summary = {
    "vehicle_violations": {
        "all_other_vehicle_defects": {"total": 26, "oos": 0},
        "brakes_all_other_violations": {"total": 25, "oos": 3},
        "brakes_out_of_adjustment": {"total": 4, "oos": 2},
        "emergency_equipment": {"total": 7, "oos": 0},
        "fuel_systems": {"total": 1, "oos": 0},
        "lighting": {"total": 24, "oos": 0},
        "periodic_inspection": {"total": 5, "oos": 2},
        "suspension": {"total": 2, "oos": 0},
        "tires": {"total": 21, "oos": 19},
        "wheels_studs_clamps_etc": {"total": 4, "oos": 0},
        "windshield": {"total": 4, "oos": 0}
    },
    "driver_violations": {
        "10_11_14_15_hours": {"total": 16, "oos": 4},
        "60_70_80_hours": {"total": 1, "oos": 1},
        "all_other_driver_violations": {"total": 50, "oos": 0},
        "all_other_hours_of_service": {"total": 15, "oos": 0},
        "disqualified_drivers": {"total": 2, "oos": 0},
        "failure_to_obey_traffic_control_device": {"total": 2, "oos": 0},
        "failure_to_yield_right_of_way": {"total": 1, "oos": 0},
        "false_log_book": {"total": 44, "oos": 19},
        "log_book_form_and_manner": {"total": 25, "oos": 0},
        "no_log_book_log_not_current_general_log_violations": {"total": 28, "oos": 0},
        "seat_belt": {"total": 4, "oos": 0},
        "size_and_weight": {"total": 8, "oos": 0},
        "speeding": {"total": 23, "oos": 0},
        "traffic_enforcement": {"total": 5, "oos": 0}
    },
    "hazmat_violations": {}
}

cursor.execute('''
INSERT INTO violations_summary (serious_violations) VALUES (?)''', 
(json.dumps(violations_summary),))

# Driver Data
drivers_data = [
    ('Driver 1: License checked against DMV, no disqualifications, 2 minor offences.',),
    ('Driver 2: License checked against DMV, 1 disqualification, 1 major offence.',),
    ('Driver 3: License checked against DMV, no disqualifications, no offences.',)
]
cursor.executemany('INSERT INTO driver_data (dmv_data) VALUES (?)', drivers_data)

# Natural Catastrophe Data
cursor.execute('''
INSERT INTO natural_catastrophe_data (wind_aggregation, wildfire_aggregation) 
VALUES (?, ?)''', 
(2.1, 1.3))

# Crime Data
crime_data = 'Crime data for postcode 12345: Increased burglary rates, moderate vandalism.'
cursor.execute('''
INSERT INTO crime_data (crime_aggregation) VALUES (?)''', 
(crime_data,))

# Static Locations Streetview
cursor.execute('''
INSERT INTO static_locations_streetview (location_image) VALUES (?)''', 
('https://maps.google.com/?q=12345&streetview',))

# Static Location Satellite View
cursor.execute('''
INSERT INTO static_location_satellite_view (location_satellite) VALUES (?)''', 
('https://maps.google.com/?q=12345&satellite',))

# Commit and close
conn.commit()
conn.close()

print("Dummy data inserted successfully.")
