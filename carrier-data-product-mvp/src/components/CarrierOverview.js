import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchCarrierOverview } from '../actions/carrierActions'; // Assuming you have an actions file
import ChartComponent from './ChartComponent';
import MapComponent from './MapComponent';

function CarrierOverview() {
  const dispatch = useDispatch();
  const carrierOverview = useSelector(state => state.carrier.carrierOverview);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    dispatch(fetchCarrierOverview())
      .then(() => setIsLoading(false))
      .catch(error => console.error('Error fetching carrier overview:', error));
  }, [dispatch]); // Fetch data when the component mounts

  if (isLoading) {
    return <div>Loading...</div>; // Show loading indicator while fetching data
  }

  if (!carrierOverview) {
    return <div>Error: Carrier data not found.</div>; // Basic error handling
  }


  // Prepare data for financial snapshot chart (example)
  const financialSnapshotData = [
    {
      x: ['Revenue', 'Credit Score'],
      y: [carrierOverview.revenue_usd, carrierOverview.credit_score],
      type: 'bar'
    }
  ];

  const financialSnapshotLayout = {
    title: 'Financial Snapshot'
  };

  // Prepare data for location risk map (example)
  const mapCenter = [51.505, -0.09]; // Default center (London)
  const mapZoom = 13;
  const markersData = [
    { 
      latitude: 51.5, 
      longitude: -0.09, 
      popupContent: `
        <b>Location Risk</b><br>
        Wind: ${carrierOverview.natural_catastrophe?.wind_aggregation || 'N/A'}<br>
        Wildfire: ${carrierOverview.natural_catastrophe?.wildfire_aggregation || 'N/A'}<br>
        Crime: ${carrierOverview.crime_aggregation || 'N/A'}
      ` 
    }
  ];

  return (
    <div>
      <div className="row">
        <div className="col-md-6">
          <h2>{carrierOverview.carrier_name}</h2>
          <p>DOT Number: {carrierOverview.carrier_dot_number}</p>
          <p>Safety Rating: {carrierOverview.safety_rating}</p>
        </div>
        <div className="col-md-6">
          <ChartComponent data={financialSnapshotData} layout={financialSnapshotLayout} />
        </div>
      </div>

      {/* Add other sections for driver performance overview and commodity risk assessment */}

      <div className="mt-4">
        <h3>Location Risk</h3>
        <MapComponent center={mapCenter} zoom={mapZoom} markersData={markersData} />
        <div className="mt-2">
          <a href={carrierOverview.streetview_image} target="_blank" rel="noopener noreferrer">
            Street View
          </a> | 
          <a href={carrierOverview.satellite_image} target="_blank" rel="noopener noreferrer">
            Satellite View
          </a>
        </div>
      </div>
    </div>
  );
}

export default CarrierOverview;
