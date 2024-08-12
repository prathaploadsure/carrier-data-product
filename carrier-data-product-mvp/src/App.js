import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import   
 CarrierOverview from './components/CarrierOverview';
import DriverPerformance from './components/DriverPerformance';

function App() {
  return (
    <Router>
      <div className="container">
        <Navbar />
        <Routes>
          <Route path="/" element={<CarrierOverview />} />
          <Route path="/driver-performance" element={<DriverPerformance />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;