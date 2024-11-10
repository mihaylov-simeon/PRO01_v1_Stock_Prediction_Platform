import { useState } from 'react';
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN, USERNAME_KEY } from "../constants";
import "../styles/Form.css"

function Form({ route, method }) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const name = method === "login" ? "Login" : "Register";
    const isLoginMode = method === "login";
    const isRegisterMode = method === "register";

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (username === "" || password === "" || (!isLoginMode && confirmPassword === "")) {
            alert("Please enter your username/password/confirmPassword.");
            return;
        }

        if (isRegisterMode && password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        try {
            const response = await api.post(route, { username, password });

            if (isLoginMode) {
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
                localStorage.setItem(USERNAME_KEY, username);
                window.location.href = "/stock_prices";
            } else {
                alert("Registration successful! Please login.");
                window.location.href = "/login";
            }
        } catch (error) {
            alert("An error occurred: " + error.message);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit} className="form__container">
                <h1>{name}</h1>
                <input 
                    className="form__input"
                    type="text"
                    placeholder="Enter username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input 
                    className="form__input"
                    type="password"
                    placeholder="Enter password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)} // Fix applied here
                />
                {isRegisterMode && (
                    <input 
                        className="form__input"
                        type="password"
                        placeholder="Confirm password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                    />
                )}
                <button type="submit" className={`form__btn__${isLoginMode ? 'login' : 'register'}`} id="submit__btn">
                    {name}
                </button>
            </form>
        </div>
    );
}

export default Form;
