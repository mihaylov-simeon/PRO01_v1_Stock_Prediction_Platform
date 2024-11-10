import React, { useEffect, useState } from 'react';
import { ACCESS_TOKEN, USERNAME_KEY } from '../constants';
import '../styles/NavBar.css';

const Navbar = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        // Check if the access token exists in local storage to determine login state
        setIsLoggedIn(localStorage.getItem(ACCESS_TOKEN) !== null);
    }, []);

    const handleLogout = () => {
        // Clear tokens from local storage and update login state
        localStorage.removeItem(ACCESS_TOKEN);
        localStorage.removeItem(USERNAME_KEY);
        setIsLoggedIn(false);
        window.location.href = "/login";
    };

    return (
        <div className="navbar__container">
            <nav className="navbar">
                <div className="navbar-left">
                    <a href="/" className="logo">Stock Price Prediction</a>
                </div>
                <div className="navbar-right">
                    <ul className="nav-links">
                        {isLoggedIn && (
                            <>
                                <li><a href="/stock_prices">Stock Prices</a></li>
                                <li><a href="/alerts">Alerts</a></li>
                                <li><a href="/history_prices">History</a></li>
                                <li><a href="/profile">Profile</a></li>
                                <li><a href="/settings">Settings</a></li>
                            </>
                        )}
                        <li>
                            {isLoggedIn ? (
                                <a href="/" onClick={handleLogout}>Logout</a>
                            ) : (
                                <a href="/login">Login</a>
                            )}
                        </li>
                        {!isLoggedIn && (
                            <li>
                                <a href="/register">Register</a>
                            </li>
                        )}
                    </ul>
                </div>
            </nav>

        </div>
    );
};

export default Navbar;
