import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">Risk Assessment</Link>
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link className="nav-link" to="/">Carrier Overview</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/driver-performance">Driver Performance</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;