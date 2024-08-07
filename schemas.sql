DROP TABLE IF EXISTS carrier_performance;
CREATE TABLE carrier_performance (
    carrier_id INTEGER PRIMARY KEY,
    carrier_name TEXT,
    carrier_dot_number TEXT,
    operating_status TEXT,
    years_in_business INTEGER,
    no_of_drivers INTEGER,
    no_of_vehicles INTEGER,
    annual_miles INTEGER,
    oos_date DATE,
    safety_rating TEXT
);

DROP TABLE IF EXISTS financial_and_credit_scores;
CREATE TABLE financial_and_credit_scores (
    carrier_id INTEGER,
    revenue_usd REAL,
    ebitda_usd REAL,
    net_profit_usd REAL,
    credit_score INTEGER,
    FOREIGN KEY (carrier_id) REFERENCES carrier_performance(carrier_id)
);

DROP TABLE IF EXISTS commodity_matrix;
CREATE TABLE commodity_matrix (
    commodity TEXT,
    contamination_percentage REAL,
    breakage_percentage REAL,
    fire_percentage REAL,
    spoilage_percentage REAL,
    theft_percentage REAL,
    weather_damage_percentage REAL
);

DROP TABLE IF EXISTS driver_performance;
CREATE TABLE driver_performance (
    unsafe_driving_measure REAL,
    unsafe_driving_percentile INTEGER,
    hours_of_service_measure REAL,
    hours_of_service_percentile INTEGER,
    vehicle_maintenance_measure REAL,
    vehicle_maintenance_percentile INTEGER,
    controlled_substances_measure REAL,
    controlled_substances_percentile INTEGER,
    driver_fitness_measure REAL,
    driver_fitness_percentile INTEGER
);

DROP TABLE IF EXISTS violations_summary;
CREATE TABLE violations_summary (
    serious_violations INTEGER
);

DROP TABLE IF EXISTS driver_data;
CREATE TABLE driver_data (
    dmv_data TEXT
);

DROP TABLE IF EXISTS natural_catastrophe_data;
CREATE TABLE natural_catastrophe_data (
    wind_aggregation REAL,
    wildfire_aggregation REAL
);

DROP TABLE IF EXISTS crime_data;
CREATE TABLE crime_data (
    crime_aggregation REAL
);

DROP TABLE IF EXISTS static_locations_streetview;
CREATE TABLE static_locations_streetview (
    location_image BLOB
);

DROP TABLE IF EXISTS static_location_satellite_view;
CREATE TABLE static_location_satellite_view (
    location_satellite BLOB
);
