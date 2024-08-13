import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchCarrierOverview } from '../actions/carrierActions';
import ChartComponent from './ChartComponent';
import MapComponent from './MapComponent';
import ErrorBoundary from './ErrorBoundary';

function CarrierOverview() {
  const dispatch = useDispatch();
  const carrierOverview = useSelector(state => state.carrier?.carrierOverview);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true; // Track whether the component is mounted

    dispatch(fetchCarrierOverview())
      .then(() => {
        if (isMounted) {
          setIsLoading(false);
        }
      })
      .catch(error => {
        console.error('Error fetching carrier overview:', error);
        if (isMounted) {
          setError(error);
          setIsLoading(false);
        }
      });

    return () => {
      isMounted = false; // Cleanup to avoid setting state on unmounted component
    };
  }, [dispatch]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>; // Display the actual error message
  }

  if (!carrierOverview) {
    return <div>Error: Carrier data not found.</div>;
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
          <ErrorBoundary>
            <ChartComponent data={financialSnapshotData} layout={financialSnapshotLayout} />
          </ErrorBoundary>
        </div>
      </div>

      {/* Add other sections for driver performance overview and commodity risk assessment */}

      <div className="mt-4">
        <h3>Location Risk</h3>
        <ErrorBoundary>
          <MapComponent center={mapCenter} zoom={mapZoom} markersData={markersData} />
        </ErrorBoundary>
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
