import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import store from './store'; // Updated store.js using configureStore
import Navbar from './components/Navbar';
import CarrierOverview from './components/CarrierOverview';
import DriverPerformance from './components/DriverPerformance';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="container">
          <Navbar />
          <Routes>
            <Route path="/" element={<CarrierOverview />} />
            <Route path="/driver-performance" element={<DriverPerformance />} />
          </Routes>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
