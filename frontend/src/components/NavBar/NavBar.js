import React from 'react';
import './NavBar.css';
import '@fortawesome/fontawesome-free/css/all.min.css'; // Ensure this is imported

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                <a href="/" className="logo">
                    Stock Price Prediction
                </a>
            </div>
            <div className="navbar-right">
                <ul className="nav-links">
                    <li>
                        <a href="/">Stock Prices</a>
                    </li>
                    <li>
                        <a href="/">Alerts</a>
                    </li>
                    <li>
                        <a href="/">History</a>
                    </li>
                    <li>
                        <a href="/" aria-label="Settings">
                            <i className="fas fa-cog"></i>
                        </a>
                    </li>
                    <li>
                        <a href="/" aria-label="User Profile">
                            <i className="fas fa-user"></i> {/* User Icon */}
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
    );
};

export default Navbar;
