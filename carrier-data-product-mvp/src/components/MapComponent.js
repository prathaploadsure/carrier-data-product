import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet'; // Import Leaflet directly for custom icon

// Create a custom marker icon (you can replace this with your own image)
const customIcon = new L.Icon({
  iconUrl: 'https://unpkg.com/leaflet@1.9.3/dist/images/marker-icon.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],   

  shadowUrl: 'https://unpkg.com/leaflet@1.9.3/dist/images/marker-shadow.png',
  shadowSize: [41, 41]
});

function MapComponent({ center, zoom, markersData }) {
  const [map, setMap] = useState(null);

  useEffect(() => {
    // If you have the map instance and markersData, you can add markers here
    if (map && markersData) {
      markersData.forEach(markerData => {
        L.marker([markerData.latitude, markerData.longitude], { icon: customIcon })
          .addTo(map)
          .bindPopup(markerData.popupContent);
      });
    }
  }, [map, markersData]);

  return (
    <MapContainer center={center} zoom={zoom} whenCreated={setMap} style={{ height: '400px' }}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"   

      />
      {/* Markers   
 will be added dynamically using useEffect */}
    </MapContainer>
  );
}

export default MapComponent;